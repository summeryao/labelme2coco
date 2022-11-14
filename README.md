# labelme2coco
you can convert labelme data to coco format data
# How to run
The "/first/dir /second/dir1/dir2" are labelme folders which you want to be dealed.  
labelme2coco.py can Walk through all files that under these folders.  
coco.json is the saved file.  
```bash
python labelme2coco.py /first/dir /second/dir1/dir2 --output coco.json
```
# expend
1. 本项目是基于https://github.com/Tony607/labelme2coco 做了些优化，提升了速度，降低了运行内存。
2. 主要是将json替换成了ujson。不导入labelme包

