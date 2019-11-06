# YOLOv3 Object Detection

This project implements an image and video UAVs(unmanned aerial vehicle) detection classifier using new trained yolov3 model. The yolov3 models are taken from the official yolov3 paper which was released in 2018. The yolov3 implementation is from darknet.

## How to use?

By following https://github.com/pjreddie/darknet installation steps, you could start using yolo models. By training a new model on the dataset that is uploaded here. You could have a new model which could detect uavs. Moreover, for using yolo v3 to create your own model, Follow these steps after installing darknet framework:

- Collect your dataset (this a good [source ](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/)to follow for collecting dataset from google)
- Start labeling your images using [labelImg tool](https://github.com/tzutalin/labelImg)
- Download Pretrained Convolutional Weights by wget https://pjreddie.com/media/files/darknet53.conv.74
- Clone this repository
- Split your dataset using generate.py after editting pathes to your dataset
- Now you are ready, start training your model using this command :
 ./darknet detector train cfg/path-to-your-data-file cfg/path-to-your-cfg-file backup/path-to-save-model ./path-to-darknet53-file/darknet53.conv.74 -> train.log
 
 
 - using plotTrainLoss.py, you can plot train.log which is the training loss
 - using yolo_opencv.py, you could test your model 

