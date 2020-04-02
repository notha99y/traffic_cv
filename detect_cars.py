"""
Runs car detections on images
"""
import sys
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm
sys.path.append("keras_yolo")
from keras_yolo.yolo import YOLO

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder_dir", help="folder_directory")

    args = parser.parse_args()

    image_paths = list(Path(args.folder_dir).glob("*.jpg"))
    od = YOLO()
    for p in tqdm(image_paths):
        print(p)
        image = Image.open(p)
        image, detections = od.detect_image(image)
        plt.imshow(image)
        plt.show()
