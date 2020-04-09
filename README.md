# Rurathon AI Inference Server on Flask

CropPrediction is an Image Classification model, created by fine-tuning ResNet, that can identify 10 different crops and 37 plant diseases. This repo is the Inference Server that can be used by Web Apps or Mobile Apps. Apps send multipart/form-data and receive a response as JSON.

  * Server IP: `<your-computer-ip>:8000`

  * ## Installation
    
    * Install required packages <br />
      `pip3 install -r requirements.txt`

    * Download models <br />
      `python3 download_models.py`

    * Run Server <br />
      `python3 app.py`

  * ## Installation (Docker) (recommended)

    * To Build: <br />
      `docker build -t crop-prediction -f docker/Dockerfile .`
    
    * To Run:<br />
      `docker run -d --rm -p 8000:8000 --name crop-prediction crop-prediction`