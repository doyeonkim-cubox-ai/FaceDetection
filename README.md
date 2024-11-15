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

##### 1. Usage
```
# wandb setting
wandb login <API key>
yolo settings wandb=True

# train
python -m FaceDetection.model
```

##### 2. statistics
(TBD)

##### 3. plots
(TBD)

##### 4. inference result
(TBD)

