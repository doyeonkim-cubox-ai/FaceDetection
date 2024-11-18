import ultralytics
from ultralytics import YOLO


def main():
    model = YOLO("./FaceDetection/yolo11/weights/best.pt")
    model.predict("https://ultralytics.com/images/bus.jpg", save=True, project="./result", name="yolo11")


if __name__ == '__main__':
    main()