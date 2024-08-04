import json

annotations_file = "annotations.json"

def save_annotation(document_id, annotation):
    try:
        with open(annotations_file, "r") as file:
            annotations = json.load(file)
    except FileNotFoundError:
        annotations = {}

    if document_id not in annotations:
        annotations[document_id] = []

    annotations[document_id].append(annotation)

    with open(annotations_file, "w") as file:
        json.dump(annotations, file)

def get_annotations(document_id):
    try:
        with open(annotations_file, "r") as file:
            annotations = json.load(file)
        return annotations.get(document_id, [])
    except FileNotFoundError:
        return []
