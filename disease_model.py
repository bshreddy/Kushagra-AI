import os
import io
import json

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models
from PIL import Image

with open(os.path.join("json", "diseases.json")) as json_file:
    diseases_class_names = json.load(json_file)

disease_model_path = "models/disease_classifier-resnet152-1577506685-38-0.9481"
disease_model = models.resnet152(pretrained=True)
disease_fc_in_ftrs = disease_model.fc.in_features
disease_fc_out_ftrs = len(diseases_class_names)
disease_model.fc = nn.Sequential(nn.Linear(disease_fc_in_ftrs, 512),
                         nn.ReLU(),
                         nn.Linear(512, disease_fc_out_ftrs),
                         nn.LogSoftmax(dim=1))
disease_model.load_state_dict(torch.load(disease_model_path, map_location=torch.device('cpu')))
disease_model.eval()

def disease_transform_image(image_bytes):
    img_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(io.BytesIO(image_bytes))
    return img_transforms(image).unsqueeze(0)

def get_disease_prediction(image_bytes):
    tensor = disease_transform_image(image_bytes)
    outputs = disease_model.forward(tensor).squeeze(0)
    _, pred = outputs.max(0)
    preds = [float(f"{outputs[i].item():.4f}") for i in range(len(diseases_class_names))]
    return {"pred": pred.item(), "cnf": preds, "kind": "disease"}