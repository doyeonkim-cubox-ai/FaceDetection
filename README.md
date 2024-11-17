# FaceDetection
Face detection with yolo v11 using pytorch

### Introduction

YOLO v11 모델을 얼굴 데이터셋에 fine tuning 하여 얼굴 인식을 수행하고자 했습니다.
학습 데이터셋은
[Face-Detection-Dataset](https://www.kaggle.com/datasets/fareselmenshawii/face-detection-dataset)
을 사용했습니다.

### Requirements
After cloning the repo, run this line below:
```
pip install -r requirements.txt
```

### Usage
```
# wandb setting
wandb login <API key>
yolo settings wandb=True

# train
python -m FaceDetection.model
```

### Statistics

##### 1. train info

optimizer: Adam(lr=0.01, momentum=0.937)
total epochs: 100
params: 2.5M
GFLOPs: 6.3

##### 2. plots

<img src="./result/plots.png" width="600" height="300">

<img src="./result/PR_curve.png" width="450" height="300">
<img src="./result/confusion_matrix_normalized.png" width="450" height="300">

##### 3. inference result

<img src="./result/output.png" width="810" height="1080">

