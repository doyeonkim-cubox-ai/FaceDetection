import torch
import torch.nn as nn
import torchvision
import ultralytics
from ultralytics import YOLO, settings
import wandb


def main():
    model = YOLO("yolo11n.pt")
    res = model.train(data="Face.yaml", epochs=100, device=0,
                      optimizer='Adam', project="FaceDetection", name="yolo11")
    model.predict("https://ultralytics.com/images/bus.jpg", save=True)


if __name__ == '__main__':
    main()
