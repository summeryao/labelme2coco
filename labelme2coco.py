<<<<<<< HEAD
import os
import ujson 
import numpy as np
import json

class labelme2coco(object):
    def __init__(self, labelme_json=[], save_json_path="./coco.json"):
        """
        :param labelme_json: the list of all labelme json file paths
        :param save_json_path: the path to save new json
        """
        self.labelme_json = labelme_json
        self.save_json_path = save_json_path
        self.images = []
        self.categories = []
        self.annotations = []
        self.label = []
        self.annID = 1
        self.height = 0
        self.width = 0
        self.save_json()
    def data_transfer(self):
        for num, json_file in enumerate(self.labelme_json):
            print(json_file)
            with open(json_file,"r") as f:
                data = ujson.load(f)
                imageDealed = self.deal_image(data, num)           
                self.images.append(imageDealed)
                for shapes in data["shapes"]:
                    label = shapes["label"]
                    if label not in self.label:
                        self.label.append(label)
                        categoryDealed = self.deal_category(label)
                        self.categories.append(categoryDealed)
                    points = shapes["points"]
                    height = data["imageHeight"]
                    width = data["imageWidth"]
                    self.annotations.append(self.deal_annotation(points, label, num, height, width))
                    self.annID += 1            
            
            
    def deal_image(self, data, num):
        image={}
        image["height"] = data["imageHeight"]
        image["width"] = data["imageWidth"]
        image["id"] = num
        image["file_name"] = data["imagePath"]
        return image
    def deal_category(self,label):
        category = {}
        category["supercategory"] = label
        category["id"] = len(self.categories)
        category["name"] = label
        return category      
    def deal_annotation(self,points,label,num,height,width):
        annotation = {}
        contour = np.array(points)
        x = contour[:, 0]
        y = contour[:, 1]
        area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
        annotation["segmentation"] = [list(np.asarray(points).flatten())]
        annotation["iscrowd"] = 0
        annotation["area"] = area
        annotation["image_id"] = num

        annotation["bbox"] = self.getbbox(points)
        annotation["category_id"] = self.getcatid(label)
        annotation["id"] = self.annID
        return annotation

    def getcatid(self, label):
        for category in self.categories:
            if label == category["name"]:
                return category["id"]
        print("label: {} not in categories: {}.".format(label, self.categories))
        exit()
        return -1

    def getbbox(self, points):
        rows=[x[0] for x in points]
        clos=[x[1] for x in points]

        left_top_r = float(int(np.min(rows))) # y
        left_top_c = float(int(np.min(clos)))  # x

        right_bottom_r = int(np.max(rows))
        right_bottom_c = int(np.max(clos))

        return [
            left_top_r,
            left_top_c,
            float(right_bottom_r - left_top_r),
            float(right_bottom_c - left_top_c),        
        ]
    def data2coco(self):
        data_coco = {}
        data_coco["images"] = self.images
        data_coco["categories"] = self.categories
        data_coco["annotations"] = self.annotations
        return data_coco

    def save_json(self):
        
        self.data_transfer()
        result = self.data2coco()
        print("save coco path: ",self.save_json_path)
        os.makedirs(
            os.path.dirname(os.path.abspath(self.save_json_path)), exist_ok=True
        )
        with open(self.save_json_path, "w") as f:
            json.dump(result,f,indent=4)
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="labelme annotation to coco data json file."
    )
    parser.add_argument(
        "labelme_images",
        help="Directory to labelme images and annotation json files.",
        type=str,
        nargs="+"
    )
    parser.add_argument(
        "--output", help="Output json file path.", default="trainval.json"
    )
    args = parser.parse_args()
    labelme_json= []


    for item in args.labelme_images:
        for curDir, dirs, files in os.walk(item):
            for file in files:
                if file.endswith(".json"):
                    labelme_json.append(os.path.join(curDir, file))
    labelme2coco(labelme_json, args.output)


=======
import os
import ujson 
import numpy as np
import json

class labelme2coco(object):
    def __init__(self, labelme_json=[], save_json_path="./coco.json"):
        """
        :param labelme_json: the list of all labelme json file paths
        :param save_json_path: the path to save new json
        """
        self.labelme_json = labelme_json
        self.save_json_path = save_json_path
        self.images = []
        self.categories = []
        self.annotations = []
        self.label = []
        self.annID = 1
        self.height = 0
        self.width = 0
        self.save_json()
    def data_transfer(self):
        for num, json_file in enumerate(self.labelme_json):
            #print(json_file)
            with open(json_file,"r") as f:
                data = ujson.load(f)
                imageDealed = self.deal_image(data, num)           
                self.images.append(imageDealed)
                for shapes in data["shapes"]:
                    label = shapes["label"]
                    if label not in self.label:
                        self.label.append(label)
                        categoryDealed = self.deal_category(label)
                        self.categories.append(categoryDealed)
                    points = shapes["points"]
                    height = data["imageHeight"]
                    width = data["imageWidth"]
                    self.annotations.append(self.deal_annotation(points, label, num, height, width))
                    self.annID += 1            
            
            
    def deal_image(self, data, num):
        image={}
        image["height"] = data["imageHeight"]
        image["width"] = data["imageWidth"]
        image["id"] = num
        image["file_name"] = data["imagePath"]
        return image
    def deal_category(self,label):
        category = {}
        category["supercategory"] = label
        category["id"] = len(self.categories)
        category["name"] = label
        return category      
    def deal_annotation(self,points,label,num,height,width):
        annotation = {}
        contour = np.array(points)
        x = contour[:, 0]
        y = contour[:, 1]
        area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
        annotation["segmentation"] = [list(np.asarray(points).flatten())]
        annotation["iscrowd"] = 0
        annotation["area"] = area
        annotation["image_id"] = num

        annotation["bbox"] = self.getbbox(points)
        annotation["category_id"] = self.getcatid(label)
        annotation["id"] = self.annID
        return annotation

    def getcatid(self, label):
        for category in self.categories:
            if label == category["name"]:
                return category["id"]
        print("label: {} not in categories: {}.".format(label, self.categories))
        exit()
        return -1

    def getbbox(self, points):
        rows=[x[0] for x in points]
        clos=[x[1] for x in points]

        left_top_r = float(int(np.min(rows))) # y
        left_top_c = float(int(np.min(clos)))  # x

        right_bottom_r = int(np.max(rows))
        right_bottom_c = int(np.max(clos))

        return [
            left_top_r,
            left_top_c,
            float(right_bottom_r - left_top_r),
            float(right_bottom_c - left_top_c),        
        ]
    def data2coco(self):
        data_coco = {}
        data_coco["images"] = self.images
        data_coco["categories"] = self.categories
        data_coco["annotations"] = self.annotations
        return data_coco

    def save_json(self):
        
        self.data_transfer()
        result = self.data2coco()
        print("save coco path: ",self.save_json_path)
        os.makedirs(
            os.path.dirname(os.path.abspath(self.save_json_path)), exist_ok=True
        )
        with open(self.save_json_path, "w") as f:
            json.dump(result,f,indent=4)
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="labelme annotation to coco data json file."
    )
    parser.add_argument(
        "labelme_images",
        help="Directory to labelme images and annotation json files.",
        type=str,
        nargs="+"
    )
    parser.add_argument(
        "--output", help="Output json file path.", default="trainval.json"
    )
    args = parser.parse_args()
    labelme_json= []


    for item in args.labelme_images:
        for curDir, dirs, files in os.walk(item):
            for file in files:
                if file.endswith(".json"):
                    labelme_json.append(os.path.join(curDir, file))
    labelme2coco(labelme_json, args.output)


>>>>>>> e97ebd577065ad2bcc0d6a1cca390a9c382b34b1
