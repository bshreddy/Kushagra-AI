# Rurathon AI Inference Server on Flask

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