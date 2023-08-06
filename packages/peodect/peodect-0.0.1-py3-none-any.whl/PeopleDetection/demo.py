from detector import CommonInferenceService
from glob import glob
import os
import cv2
from PIL import Image

# 初始化模型
server = CommonInferenceService(model_path=r"F:\PycharmProjects\ZH-YH\devlop\weights-use\people-norm-v20230305.onnx")
data_box = []
path = r'F:\PycharmProjects\ZH-YH\stand\1.jpg'

data = {"camera_id": "4c357184-0b4f-46eb-a123", "data_name": os.path.basename(path), "points": data_box,
            "data_path": path}
re = server.inference(data)
print(re)
