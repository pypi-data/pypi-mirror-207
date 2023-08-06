
import json
import yaml

def get_dict_value(data, key, default=None):
    current_value = data       
    if isinstance(current_value, dict):
        if key in current_value:
            current_value = current_value[key]
        else:
            return default
    elif isinstance(current_value, list):
        try:
            index = int(key)
            current_value = current_value[index]
        except (ValueError, IndexError):
            return default
    else:
        return default
    return current_value

def merge_images_annotations(images, annotations):
    merged_data = []

    # Create a dictionary to store images by id
    images_dict = {image['id']: image for image in images}

    # Iterate over annotations and merge with corresponding image
    for annotation in annotations:
        image_id = annotation['image_id']
        if image_id in images_dict:
            image = images_dict[image_id]

            # Copy the image to preserve the original
            merged_image = image.copy()

            # Insert annotations into the matched image
            if 'annotations' in merged_image:
                merged_image['annotations'].append(annotation)
            else:
                merged_image['annotations'] = [annotation]

            merged_data.append(merged_image)

    return merged_data

def match_annotations_with_images(images, annotations):
    # Merge images with corresponding annotations
    merged_data = merge_images_annotations(images, annotations)

    # Create a dictionary to store images by id
    images_dict = {image['id']: image for image in merged_data}

    # Iterate over annotations and insert into corresponding image
    for annotation in annotations:
        image_id = annotation['image_id']
        if image_id in images_dict:
            image = images_dict[image_id]
            if 'annotations' not in image:
                image['annotations'] = []
            image['annotations'].append(annotation)

    return merged_data


def convert_to_new_format(data):
    from rc.cli.utils import datetime_to_nanoseconds
    new_data = []

    for item in data:
        new_item = {
            "projectId": 2,
            "input": [item["file_name"]],
            "attributes": {},
            "capture_time": datetime_to_nanoseconds(item["date_captured"]),
            "source": "",
            "event_index": None,
            "output_type": None,
            "model_id": None,
            "output": {
                "frame_id": 1,
                "detections": item["annotations"]["bbox"]
            },
            "image_embedding": None,
            "caption": None
        }
        new_data.append(new_item)


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")
            return None

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
            




