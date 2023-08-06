import os
import onnxruntime as ort
import numpy as np
import cv2
from PIL import Image

# '''
# 版本：v2023-04-12
# 模型：helmet_single_20230412_640.onnx
# '''
class CommonInferenceService:
    def __init__(self,model_path):
        self.use_gpu = True
        providers = ["CPUExecutionProvider"]
        if self.use_gpu:
            providers = ['CUDAExecutionProvider', "CPUExecutionProvider"]
        # "F:\PycharmProjects\ZH-YH\devlop\weights-use\people-norm-v20230305.onnx"
        self.model_path =model_path
        self.inter_onnx_model=ort.InferenceSession(self.model_path,providers=providers)
        self.inter_input_name=[i.name for i in self.inter_onnx_model.get_inputs()][0]
        self.inter_output_name=[i.name for i in self.inter_onnx_model.get_outputs()]
        self.inter_nms_thr=0.45
        self.inter_score_thr=0.45
        self.inter_class_names=['people']
        self.inter_keep_names=['people']
        self.numer = 5

    def rectangle(self,img, boxes):
        tmp = np.copy(img)
        for i in range(len(boxes)):
            box = boxes[i]
            xmin, ymin, xmax, ymax = box["box"]
            text = box["label"] + str(i) + '_' + str(box["conf"])
            cv2.putText(tmp, text, (int(xmin), int(ymin)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            cv2.rectangle(tmp, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 255), 1, lineType=cv2.LINE_AA)
        return Image.fromarray(tmp[..., ::-1])

    def nms(self, boxes, scores, nms_thr):
        """Single class NMS implemented in Numpy."""
        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]

        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        order = scores.argsort()[::-1]

        keep = []
        while order.size > 0:
            i = order[0]
            keep.append(i)
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])

            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            ovr = inter / (areas[i] + areas[order[1:]] - inter + 0.000001)

            inds = np.where(ovr <= nms_thr)[0]
            order = order[inds + 1]
        return keep

    def multiclass_nms(self, boxes, scores, nms_thr, score_thr):
        """Multiclass NMS implemented in Numpy"""
        final_dets = []
        num_classes = scores.shape[1]
        for cls_ind in range(num_classes):
            cls_scores = scores[:, cls_ind]
            valid_score_mask = cls_scores > score_thr
            if valid_score_mask.sum() == 0:
                continue
            else:
                valid_scores = cls_scores[valid_score_mask]
                valid_boxes = boxes[valid_score_mask]
                keep = self.nms(valid_boxes, valid_scores, nms_thr)
                if len(keep) > 0:
                    cls_inds = np.ones((len(keep), 1)) * cls_ind
                    dets = np.concatenate(
                        [valid_boxes[keep], valid_scores[keep, None], cls_inds], 1
                    )
                    final_dets.append(dets)
        if len(final_dets) == 0:
            return None
        return np.concatenate(final_dets, 0)

    def resize_image(self, image, input_size, mean, std, swap=(2, 0, 1)):
        if len(image.shape) == 3:
            padded_img = np.ones((input_size[0], input_size[1], 3)) * 114.0
        else:
            padded_img = np.ones(input_size) * 114.0
        img = np.array(image)
        r = min(input_size[0] / img.shape[0], input_size[1] / img.shape[1])
        resized_img = cv2.resize(
            img,
            (int(img.shape[1] * r), int(img.shape[0] * r)),
            interpolation=cv2.INTER_LINEAR,
        ).astype(np.float32)
        padded_img[: int(img.shape[0] * r), : int(img.shape[1] * r)] = resized_img

        padded_img = padded_img[:, :, ::-1]
        padded_img /= 255.0
        if mean is not None:
            padded_img -= mean
        if std is not None:
            padded_img /= std
        padded_img = padded_img.transpose(swap)
        return padded_img, r

    def pic_percent(self, box1, box2):
        x, y, w, h = box1
        area1 = (w - x) * (h - y)
        x, y, w, h = box2
        area2 = (w - x) * (h - y)
        percent = round(area2 / area1, 3)
        return percent

    def LowerCount(self, a, b):
        num = 0
        for i in a:
            if i < b:
                num += 1

        return num

    def yolov6(self,cv2_img,score_thr=0.5,nms_thr=0.45,class_names=None,keep_names=None,imgsz=(640,640),interMap=False,fp16=True):
        if interMap:
            model=self.inter_onnx_model
            input_name=self.inter_input_name
            output_name=self.inter_output_name
        else:
            model=self.onnx_model
            input_name = self.input_name
            output_name = self.output_name
        h, w, c = cv2_img.shape
        img, ratio = self.resize_image(cv2_img, imgsz, None, None)
        if fp16:
            img = np.ascontiguousarray(img, dtype=np.float16)
        else:
            img = np.ascontiguousarray(img, dtype=np.float32)
        if fp16:
            predictions = model.run(output_name, {input_name: np.array([img])})
        else:
            predictions = model.run(None, {input_name: np.array([img])})

        predictions = predictions[0][0]
        predictions = predictions.astype("float32")
        boxes = predictions[:, :4]
        scores = predictions[:, 4:5] * predictions[:, 5:]
        boxes_xyxy = np.ones_like(boxes)
        boxes_xyxy[:, 0] = boxes[:, 0] - boxes[:, 2] / 2.
        boxes_xyxy[:, 1] = boxes[:, 1] - boxes[:, 3] / 2.
        boxes_xyxy[:, 2] = boxes[:, 0] + boxes[:, 2] / 2.
        boxes_xyxy[:, 3] = boxes[:, 1] + boxes[:, 3] / 2.
        boxes_xyxy /= ratio
        dets = self.multiclass_nms(boxes_xyxy, scores, nms_thr=nms_thr, score_thr=score_thr)
        boxes=[]
        if dets is not None:
            final_boxes, final_scores, final_cls_inds = dets[:, :4], dets[:, 4], dets[:, 5]
            for i in range(len(final_boxes)):
                box = final_boxes[i]
                cls_id = int(final_cls_inds[i])
                score = final_scores[i]
                x0 = max(0, int(box[0]))
                y0 = max(0, int(box[1]))
                x1 = int(box[2])
                y1 = int(box[3])
                zd_pos = [x0, y0, x1, y1]  # 预测框坐标
                # if (x1 - x0) > 0.8 * w or (y1 - y0) > 0.8 * h:
                #     continue
                if class_names[cls_id] in keep_names:

                    boxes.append({"label":class_names[cls_id],"box":zd_pos,"conf":score})
        return boxes

    def inference(self, data):
        def get_IOU(point1, point2):
            x1, y1, w1, h1 = point1
            x2, y2, w2, h2 = point2
            if (abs(x1 - x2) < ((w1 + w2) / 2.0)) and (abs(y1 - y2) < ((h1 + h2) / 2.0)):
                left = max((x1 - (w1 / 2.0)), x2 - (w2 / 2.0))
                upper = max((y1 - (h1 / 2.0)), y2 - (h2 / 2.0))
                right = min((x1 + (w1 / 2.0)), x2 + (w2 / 2.0))
                bottom = min((y1 + (h1 / 2.0)), y2 + (h2 / 2.0))

                inter_w = abs(right - left)
                inter_h = abs(bottom - upper)
                inter_area = inter_h * inter_w
                sum_area = (w1 * h1) + (w2 * h2) - inter_area
                calIOU = inter_area / (w1 * h1)
                return calIOU
            else:
                return None
        camera_id = str(data['camera_id'])
        result = {"data_name": data['data_name']}
        result['predictions'] = list()
        # detect_pos =data["points"]
        pts = []
        for item in data["points"]:
            p = []
            for i in range(len(item)):
                p.append((item[i]['cor_x'], item[i]["cor_y"]))
            # print(p)  #得到区域点集
            pts.append(p)
        # print(pts)  # 得到多个区域点集

        if os.path.exists(data['data_path']):
            cv2_img = cv2.imread(data['data_path'])
            #站人检测
            # stand_boxes=self.yolov6(cv2_img,score_thr=self.score_thr,nms_thr=self.nms_thr,class_names=self.class_names,keep_names=self.keep_names,imgsz=self.imgsz,interMap=False)
            people_boxes=self.yolov6(cv2_img,score_thr=self.inter_score_thr,nms_thr=self.inter_nms_thr,class_names=self.inter_class_names,keep_names=self.inter_keep_names,imgsz=(640,640),interMap=True)
            newboxes=[]
            if len(people_boxes)>0:
                for sbox in people_boxes:
                    x0,y0,x1,y1=sbox["box"]
                    x0=max(0,int(x0))
                    y0=max(0,int(y0))
                    x1=min(cv2_img.shape[1],int(x1))
                    y1=min(cv2_img.shape[0],int(y1))
                    if x0>=x1 or y0>=y1:
                        continue
                    cx1 = (x0 + x1) / 2
                    cy1 = (y0 + y1) / 2
                    w1 = abs(x0 - x1)
                    h1 = abs(y0 - y1)
                    point1 = (cx1, cy1, w1, h1)
                    newboxes.append(sbox)
                    result['predictions'].append(sbox)
            # if len(newboxes)>0:
            #     newboxes=sorted(newboxes,key=lambda x:x["conf"])
            #     result['predictions'].append(newboxes[0:-1])
        return result
#
# if __name__ == "__main__":
#     server = CommonInferenceService()
#     print('模型初始化成功')
#     #批量
#     data_box = []
#     paths = glob(r'F:\PycharmProjects\ZH-YH\stand\1.jpg')
#     save_path = r"F:\PycharmProjects\ZH-YH\VideoC"
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)
#         # os.makedirs(save_path+"you\\")
#         # os.makedirs(save_path + "wu\\")
#     print(paths)
#     for p in paths:
#         data = {"camera_id": "4c357184-0b4f-46eb-a123", "data_name": os.path.basename(p), "points": data_box,
#                             "data_path": p}
#         re = server.inference(data)
#         print(re)
#         img = cv2.imread(p)
#         if re['predictions'] != []:
#             tmp = rectangle(img, re['predictions'])
#             tmp.show()
#             tmp.save(save_path + '\\' + os.path.basename(p))
#         else:
#             Image.fromarray(img[..., ::-1]).show()
#             Image.fromarray(img[..., ::-1]).save(save_path + "\\" + os.path.basename(p))