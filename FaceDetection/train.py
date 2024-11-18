import ultralytics
from ultralytics import YOLO, settings
import wandb


def main():
    model = YOLO("yolo11n.pt")
    res = model.train(data="Face.yaml", epochs=100, device=0,
                      optimizer='Adam', project="FaceDetection", name="yolo11")
    metrics = model.val()
    print(metrics.results_dict)


if __name__ == '__main__':
    main()
