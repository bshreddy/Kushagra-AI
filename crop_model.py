import io
import json

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models
from PIL import Image

with open("crops.json") as json_file:
    crop_class_names = json.load(json_file)

crop_model_path = "models/crop_classifier-resnet50-ft-1577380661-10-0.9200"
crop_model = models.resnet50(pretrained=True)
crop_fc_in_ftrs = crop_model.fc.in_features
crop_fc_out_ftrs = len(crop_class_names)
crop_model.fc = nn.Linear(crop_fc_in_ftrs, crop_fc_out_ftrs)
crop_model.load_state_dict(torch.load(crop_model_path, map_location=torch.device('cpu')))
crop_model.eval()

def crop_transform_image(image_bytes):
    img_transforms = transforms.Compose([
        transforms.Resize(480),
        transforms.CenterCrop(320),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(io.BytesIO(image_bytes))
    return img_transforms(image).unsqueeze(0)

def get_crop_prediction(image_bytes):
    tensor = crop_transform_image(image_bytes)
    outputs = crop_model.forward(tensor).squeeze(0)
    _, pred = outputs.max(0)
    outputs = F.softmax(outputs, dim=0)
    preds = [float(f"{outputs[i].item():.4f}") for i in range(len(crop_class_names))]
    return {"pred": pred.item(), "cnf": preds}