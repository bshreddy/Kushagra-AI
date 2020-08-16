# Kushagra - AI-powered Mobile App - Inference Server

An AI-powered mobile crop advisory app for farmers, gardeners that can provide information about crops using an image taken by the user. This supports 10 crops and 37 kinds of crop diseases. The AI model is a ResNet network that has been fine-tuned using crop images that were collected by web-scraping from Google Images and Plant-Village Dataset.

This repository is the Inference Server that performs image classification on images captured by the user.

Main Project Repo: [https://github.com/SaiHemanthBR/Kushagra](https://github.com/SaiHemanthBR/Kushagra)

## Endpoints
  * [POST] `/crop` - classifies image into one of 10 crop classes. <br>
    ```Content-Type: multipart/form-data```
    
    Query Parameters <br>
    |Parameter|Description|Type|
    |---------|-----------|----|
    |img|Image of the crop that needs to be classfied.|Image File|
    
    <br>

    Response Object <br>
    |Object|Data Type|Description|
    |------|---------|-----------|
    |pred|integer|Index of Predicted Class. (Index of largest element in `cnf` array.)|
    |cnf|array[double]|Confidence of prediction for each index. values of Softmax of last layer of the ResNet model.|
    |kind|string|Value: `"crop"`<br>Kind of prediction. (crop\|disease)|


    <br><br>

  * [POST] `/disease` - classifies image into one of 37 crop diseases. <br>
    ```Content-Type: multipart/form-data```
    
    Query Parameters <br>
    |Parameter|Description|Type|
    |---------|-----------|----|
    |img|Image of the crop that needs to be classfied.|Image File|

    <br>

    Response Object <br>
    |Object|Data Type|Description|
    |------|---------|-----------|
    |pred|integer|Index of Predicted Class. (Index of largest element in `cnf` array.)|
    |cnf|array[double]|LogSoftmax values of last layer of the ResNet model.|
    |kind|string|Value: `"disease"`<br>Kind of prediction. (crop\|disease)|

    <br><br>

## Installation (Docker) (Recommended)
  1. To Build: <br />
      `docker build -t crop-prediction -f docker/Dockerfile .`
    
  2. To Run:<br />
      `docker run -d --rm -p 8000:8000 --name crop-prediction crop-prediction`

## Installation
  1. Install required packages <br />
      `pip3 install -r requirements.txt`

  2. Download models <br />
      `python3 download_models.py`

  3. Run Server <br />
      `python3 app.py`

<br><br>

> For more implementation details, please read the report at [github.com/SaiHemanthBR/Kushagra-Report](https://github.com/SaiHemanthBR/Kushagra-Report)

## Contributers
  * [SaiHemanthBR](https://github.com/SaiHemanthBR/)