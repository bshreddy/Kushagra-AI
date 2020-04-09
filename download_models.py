import os
import requests
from tqdm import tqdm

models_dir = "models"
files = {"crop_classifier-resnet50-ft-1577380661-10-0.9200": "https://firebasestorage.googleapis.com/v0/b/rurathon-cvr-2019.appspot.com/o/models%2Fcrop_classifier-resnet50-ft-1577380661-10-0.9200?alt=media",
         "disease_classifier-resnet152-1577506685-38-0.9481": "https://firebasestorage.googleapis.com/v0/b/rurathon-cvr-2019.appspot.com/o/models%2Fdisease_classifier-resnet152-1577506685-38-0.9481?alt=media",
         "resnet50-19c8e357.pth": "https://download.pytorch.org/models/resnet50-19c8e357.pth",
         "resnet152-b121ed2d.pth": "https://download.pytorch.org/models/resnet152-b121ed2d.pth"}

if not os.path.exists(models_dir):
    os.mkdir(models_dir)

for filename, fileurl in files.items():
    req = requests.get(fileurl, stream=True)
    file_size = int(req.headers["content-length"])
    chunk_size = 1000

    with open(os.path.join(models_dir, filename), "wb") as f:
        with tqdm(desc=f"Fetching {filename}", total=file_size, unit_scale=True) as pbar:
            for chunk in req.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                pbar.update(chunk_size)