FROM ubuntu:18.04

COPY . /app

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && \
    pip3 install -r requirements.txt && \
    pip3 install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

RUN mkdir -p /root/.cache/torch/checkpoints/ && \
    mv models/resnet50-19c8e357.pth /root/.cache/torch/checkpoints/resnet50-19c8e357.pth && \
    mv models/resnet152-b121ed2d.pth /root/.cache/torch/checkpoints/resnet152-b121ed2d.pth

EXPOSE 8000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]