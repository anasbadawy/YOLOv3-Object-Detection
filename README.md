Training YOLOv3 Object Detector - emaraic

1. collecting Dataset (.jpg) and generating labels for it.

2. create (train.txt - test.txt) 

	- edit the path of "generate.py" file  ( dataset_path = '/path/to/Dataset/JPEGImages')

	- python3 generate.py


3. git clone https://github.com/pjreddie/darknet
	cd darknet
	make

4. download darknet53.conv.74 file as weights

5. after editing pathes start training = >  
	./darknet detector train /home/enganas1997/yolo-custom-object-detector/custom/trainer.data /home/enganas1997/yolo-custom-object-detector/custom/yolov3-tiny.cfg  ./darknet53.conv.74

6. Testing after editing pathes of .names, .weights and .cfg
	python3 yolo_opencv.py

notice that we already have yolov3.cfg file, trainer.data and objects.name inside "custom" folder
