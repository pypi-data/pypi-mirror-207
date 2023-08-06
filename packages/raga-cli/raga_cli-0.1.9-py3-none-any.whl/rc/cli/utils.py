import logging
import os
from pathlib import Path
from pydoc import stripid
import json
import subprocess
import time
import sys
from rc.utils import DEBUG
from multiprocessing import cpu_count
from pathlib import Path
import pathlib
import re
from datetime import datetime
from rc.utils.config import get_config_value
import glob

from rc.utils.request import dataset_upload_web, get_commit_repo, get_config_value_by_key, get_repo_version, model_upload_web

logger = logging.getLogger(__name__)

class RctlValidSubprocessError(Exception):
    def __init__(self, msg, *args):
        assert msg
        self.msg = msg
        logger.error(msg)
        super().__init__(msg, *args)

def fix_subparsers(subparsers):
    subparsers.required = True
    subparsers.dest = "cmd"

def get_git_url(cwd):
    result = subprocess.run('git config --get remote.origin.url', capture_output=True, shell=True, cwd=cwd)    
    stdout = str(result.stdout, 'UTF-8')
    return stripid(stdout)

def get_repo():
    result = subprocess.run('git config --get remote.origin.url', capture_output=True, shell=True)    
    stdout = str(result.stdout, 'UTF-8').split("/")[-1].replace('.git', '')
    return stdout.strip()

def trim_str_n_t(str):
    return ' '.join(str.split())

def get_dvc_data_status(path):
    logger.debug("Compare on PATH : {}".format(path))
    result = subprocess.run('dvc status {}'.format(path), capture_output=True, shell=True)    
    stdout = str(result.stdout, 'UTF-8').strip()
    logger.debug(stdout)
    # stdout_line = stdout.splitlines()
    # stdout_line = list(map(trim_str_n_t, stdout_line))
    if stdout.find('modified') != -1:
        return True  
    if stdout.find('Data and pipelines are up to date') != -1:
        return False  
    return False

def get_new_dvc_data_status(path):
    if not get_dvc_data_status(path) and not compare_dot_dvc_file(path):
        return True
    return False



def dataset_current_version(paths, repo):
    current_version = 0 if not get_repo_version(repo) else int(get_repo_version(repo))
    for path in paths:
        if not compare_dot_dvc_file(path):
            return current_version+1
        if get_dvc_data_status(path):
            return current_version+1
    return 1 if not current_version else current_version


def model_current_version(repo):
    current_version = 0 if not get_repo_version(repo) else int(get_repo_version(repo))
    return 1 if not current_version else current_version+1

def server_repo_commit_status(ids):
    elastic_processes = []
    for id in ids:
        elastic_processes.append(get_commit_repo(id)['check_elastic_process'])
    logger.debug("ELASTIC PROCESS {}".format(elastic_processes))
    return all(elastic_processes)

def current_commit_hash(cwd=None):
    if cwd:
        result = subprocess.run('git rev-parse HEAD', capture_output=True, shell=True, cwd=cwd)
    else:
        result = subprocess.run('git rev-parse HEAD', capture_output=True, shell=True)
    stdout = str(result.stdout, 'UTF-8')
    logger.debug(f"COMMIT HASH: {stdout.strip()}")
    return stdout.strip()

def current_branch():
    result = subprocess.run('git rev-parse --abbrev-ref HEAD', capture_output=True, shell=True)    
    stdout = str(result.stdout, 'UTF-8')
    return stdout.strip()

def branch_commit_checkout(branch,commitId):
    result = subprocess.run('git checkout {0} -b {1}'.format(commitId,branch), capture_output=True, shell=True)    
    stdout = str(result.stdout, 'UTF-8')
    return stdout.strip()

def is_repo_exist_in_gh(repo):
    logger.debug("Check existence of repo in GIT HUB : {}".format(repo))
    result = subprocess.run('gh repo view {}'.format(repo), capture_output=True, shell=True)    
    stdout = str(result.stdout, 'UTF-8').strip()
    stderr = str(result.stderr, 'UTF-8').strip()
    logger.debug(f"STD OUT: {stdout}")
    logger.debug(f"STD ERR: {stderr}")
    match = re.search(r'Could not resolve to a Repository with the name', stderr)
    if match:
        logger.debug("Repo not found in GH")
        return False  
    logger.debug("Repo found in GH")
    return True


def check_push_left():
    logger.debug("Check PUSH left")
    result = subprocess.run('git status', capture_output=True, shell=True)    
    stdout = str(result.stdout, 'UTF-8').strip()
    stderr = str(result.stderr, 'UTF-8').strip()
    logger.debug(f"STD OUT: {stdout}")
    logger.debug(f"STD ERR: {stderr}")
    if re.search(r'(use "git push" to publish your local commits)', stdout):
        logger.debug("Push left")
        return True  
    elif re.search(r'(use "git push" to publish your local commits)', stderr):
        logger.debug("Push left")
        return True  
    logger.debug("Clean PUSH")
    return False

def is_current_version_stable():
    from rc.utils.request import get_commit_version, get_repo_version
    repo = get_repo()
    commit_id = current_commit_hash()
    repo_version = get_repo_version(repo)
    commit_version = get_commit_version(commit_id)
    if not commit_version and not repo_version:
        return True

    if commit_version == repo_version:
        return True
    else:
        logger.debug("Local repo version is not stable")
        print("Unable to upload from older version. Please use `rc get` to get the latest version and try again.")
        return False

def get_min_cpu():
    process = 2
    cpu = cpu_count()
    if cpu>4:
        process = int(cpu/4)
    return process        

def get_dir_file(path):
    dvc_file = Path(f'{path}.dvc')
    if not dvc_file.is_file():
        logger.debug("DVC file not found.")
        print("Something went wrong")
        sys.exit(50)
    dvc_read = open(dvc_file, "r")
    md5_dir = ''
    for line in dvc_read.readlines():
        if line.find('- md5') != -1:
            md5_dir = line.split(":")[-1].strip()
    if not md5_dir:
        logger.error(".dir file not found.")
        sys.exit(50)
    return md5_dir

def get_only_valid_dir(dir):
    if not dir.startswith("."):
        return True
    else:
        return False

def trim_slash(str):
    if str.endswith("/"):
        str = str.rsplit("/", 1)[0] 
    return str

def valid_cwd_rc():
    cwd = os.getcwd()   # get the current working directory
    rc_dir = os.path.join(cwd, ".rc")   # create a path to the .rc directory
    if not os.path.isdir(rc_dir):   # check if the path is a directory
        print("Your current location is not a rc repo directory location.")
        sys.exit()
    return True

def find_dvc_files():
    files = []
    cwd = os.getcwd()   # get the current working directory
    for file in os.listdir(cwd):   # iterate through the files in the current directory
        if file.endswith(".dvc") and not os.path.isdir(os.path.join(cwd, file)):   # check if the file has a .dvc extension and is not a directory
            files.append(os.path.join(cwd, file))
    return files

def match_and_delete_files(dir_list, file_list):
    dir_names = [os.path.basename(d) for d in dir_list]   # get the names of the directories in the first list
    for file in file_list:   # iterate through the files in the second list
        filename = pathlib.Path(file).stem   # get the filename from the full path
        if filename not in dir_names:   # check if the filename is not in the list of directory names
            logger.debug(f"REMOVE DVC FILE : {filename}")
            os.remove(file)   # delete the file if it does not have a matching directory name

def check_extensions(extensions=["requirements.txt", ".pth"]):
    found_extensions = set()
    for extension in extensions:
        extension_found = False
        for subdir, dirs, filenames in os.walk("."):
            for filename in filenames:
                if filename.endswith(extension):
                    found_extensions.add(extension)
                    extension_found = True
                    break
            if extension_found:
                break
        if not extension_found:
            print(f"{extension} file not found.")
            sys.exit()
    return True

def valid_dot_dvc_with_folder(dirs):
    files = find_dvc_files()
    match_and_delete_files(dirs, files)
    
def get_all_data_folder():
    directory = os.getcwd()
    dirs = next(os.walk(directory))[1]
    filtered = list(filter(get_only_valid_dir, dirs))
    return filtered

def compare_dot_dvc_file(dir_path):
    dvc_file = Path(f'{dir_path}.dvc')
    if dvc_file.is_file():
        return True
    return False
    
def back_slash_trim(dirs):
    filtered = list(map(trim_slash, dirs))
    return filtered

def valid_git_connection(str, command = None):
    if command and (command.find('git push') != -1 or command.find('git clone')):
        if str.find("Permission denied (publickey)") != -1:            
            print("git@github.com: Permission denied (publickey). Please make sure you have the correct access rights and the repository exists on git.")
            sys.exit(50)   
        elif str.find("ERROR: Repository not found") != -1:            
            print("Repository not found. Please make sure you have the correct access rights and the repository exists on git.")
            sys.exit(50) 
    return True

def run_command_on_subprocess(command, cwd=None, err_skip=False):
    logger.debug(command)
    if cwd:
        result = subprocess.run(command, capture_output=True, shell=True, cwd=cwd)
        stderr = str(result.stderr, 'UTF-8')
        stdout = str(result.stdout, 'UTF-8')        
        if stdout:      
            valid_git_connection(stdout, command)                  
            logger.debug("STD OUT {}".format(stdout)) 

        if stderr:            
            valid_git_connection(stderr, command)    
            logger.debug("STD ERR {}".format(stderr))                
                
    else:
        result = subprocess.run(command, capture_output=True, shell=True)
        stderr = str(result.stderr, 'UTF-8')
        stdout = str(result.stdout, 'UTF-8')        
        if stdout:                        
            valid_git_connection(stdout, command)    
            logger.debug("STD OUT {}".format(stdout)) 

        if stderr:        
            valid_git_connection(stderr, command)        
            logger.debug("STD ERR {}".format(stderr))
                
                

def repo_name_valid(name):
    for c in name:        
        if c == '_':
            raise RctlValidSubprocessError("Error: Bucket name contains invalid characters")
    if len(name) <3 or len(name)>63:
        raise RctlValidSubprocessError("Error: Bucket names should be between 3 and 63 characters long")   
    
def path_to_dict(path):
    name = os.path.basename(path)
    if name == ".rc" or name == ".git":
        return None
    d = {'name': name}
    if os.path.isdir(path):
        d['type'] = "directory"
        children = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
        d['children'] = [c for c in children if c is not None]
    else:
        d['type'] = "file"
        d['last_updated'] = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
    return d

def get_infra_file():
    json_files = glob.glob("executions" + '/*.json')
    if json_files:
        if len(json_files) > 1:
            print("Execution file can not be grater than 1")
            sys.exit()
        logger.debug(f"Infra file: {json_files[0]}")
        return json_files[0]
    print("Executions dir or execution json file does not exists.")
    sys.exit()


def upload_infra_json(version, cwd = None):
    if cwd:
        owd = os.getcwd()
        os.chdir(f"{owd}/{cwd}") 
    model_version = int(version)-1 if version else 1
    logger.debug("INFRA FILE UPLOADING")
    import botocore.session   
    infra_file = get_infra_file()
    CLOUD_STORAGE_BUCKET = get_config_value_by_key('bucket_name')
    CLOUD_STORAGE_DIR = get_config_value_by_key('cloud_storage_dir')
    AWS_SECRET = get_config_value_by_key('remote_storage_secret_key')
    AWS_ACCESS = get_config_value_by_key('remote_storage_access_key')
    repo = get_repo()
    dest = f"{CLOUD_STORAGE_DIR}/{repo}/versions/{model_version}/result.json"
    # Create a botocore session with the AWS access key and secret key
    session = botocore.session.Session()
    session.set_credentials(AWS_ACCESS, AWS_SECRET)

    # Create an S3 client using the botocore session
    s3 = session.create_client('s3')

    # Upload the file to S3
    with open(infra_file, 'rb') as file:
        s3.put_object(Bucket=CLOUD_STORAGE_BUCKET, Key=dest, Body=file)          

    if cwd:
        os.chdir(owd)


def upload_model_file_list_json(version, cwd = None):
    if cwd:
        owd = os.getcwd()
        os.chdir(f"{owd}/{cwd}") 
    logger.debug("MODEL FILE UPLOADING")
    import botocore.session   
    model_file_list = json.loads(json.dumps(path_to_dict('.')))
    CLOUD_STORAGE_BUCKET = get_config_value_by_key('bucket_name')
    CLOUD_STORAGE_DIR = get_config_value_by_key('cloud_storage_dir')
    AWS_SECRET = get_config_value_by_key('remote_storage_secret_key')
    AWS_ACCESS = get_config_value_by_key('remote_storage_access_key')
    repo = get_repo()
    dest = f"{CLOUD_STORAGE_DIR}/{repo}/model_files/{version}.json"
    # Create a botocore session with the AWS access key and secret key
    session = botocore.session.Session()
    session.set_credentials(AWS_ACCESS, AWS_SECRET)

    # Create an S3 client using the botocore session
    s3 = session.create_client('s3')

    with open(f'{version}.json', 'w', encoding='utf-8') as cred:    
        json.dump(model_file_list, cred, ensure_ascii=False, indent=4)  

    # Upload the file to S3
    with open(f'{version}.json', 'rb') as file:
        s3.put_object(Bucket=CLOUD_STORAGE_BUCKET, Key=dest, Body=file)          
    pathlib.Path(f'{version}.json').unlink(missing_ok=True)

    if cwd:
        os.chdir(owd)
    
def retry(ExceptionToCheck, tries=4, delay=3, backoff=2):
    """
    Retry calling the decorated function using an exponential backoff.

    Args:
        ExceptionToCheck (Exception): the exception to check. When an exception of this type is raised, the function will be retried.
        tries (int): number of times to try before giving up.
        delay (int): initial delay between retries in seconds.
        backoff (int): backoff multiplier (e.g. value of 2 will double the delay each retry).

    Example Usage:
    ```
    @retry(Exception, tries=4, delay=3, backoff=2)
    def test_retry():
        # code to retry
    ```
    """
    logger.debug("RETRYING")
    def deco_retry(f):
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    print(f"Got exception '{e}', retrying in {mdelay} seconds...")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)
        return f_retry
    return deco_retry


def folder_exists(folder_name):
    current_dir = os.getcwd()
    folder_path = os.path.join(current_dir, folder_name)
    return os.path.exists(folder_path) and os.path.isdir(folder_path)

def upload_model(model, version):
    model_version = int(version)-1 if version else 1
    model_name = f"{model}:version{model_version}"
    model_upload_web(model_name, 2)

def upload_dataset(dataset, version):
    dataset_name = f"{dataset}:version{version}"
    media_path = f"{get_config_value('remote_bucket_location')}/{get_config_value('repo')}"
    dataset_upload_web(dataset_name, 2, media_path)