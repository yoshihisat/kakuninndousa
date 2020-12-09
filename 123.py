import os
import time
import sys
import cv2

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observers
BASEDIR = os.path.abspath(os.path.dirname(__file__))
OUT_OIR = "./"


def get_ext(filename):
    return os.path.splitext(filename)[-1].lower()


def process(filepath):
    out_filename = os.path.basename(filepath)
    img_bgr = cv2.imread(filepath)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BAYER_BG2GRAY)

    cv2.imwrite(OUT_OIR + out_filename,img_gray)

    