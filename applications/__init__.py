import sys
import os


root = os.path.realpath(
    os.path.dirname(os.path.dirname(__file__)))
module_path = os.path.join(root, 'detect/yolov5')
sys.path.insert(0, module_path)
