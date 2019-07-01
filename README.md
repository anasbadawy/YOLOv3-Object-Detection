Training YOLOv3 Object Detector - Snowman

1. make sure libraries (numpy ,matplotlib, argparse ,imutils)

if not install by

`sudo pip install numby
......` 

2. put your data set in the folder "JPEGImages" , then create a new folder called "labels" at the same place where the folder "JPEGImages" is.

3. create labels file of each image by selecting the object required in each image by runing the code:
python labelscreator.py in the directory where "JPEGImages" and "labels" are.

- drawing the box should be from up left corner to down right corner.

- after drawing the box click 'space key' double for moving to next image / or space then 'esc key' to select another object in the same image .. then so on for continue or selecting another one.


5. Create the train-test split

	edit the bath for h folder in the line below

`python3 splitTrainAndTest.py //h/JPEGImages`

Give the correct path to the data JPEGImages folder. The 'labels' folder should be in the same directory as the JPEGImages folder.

4. check and correct the pathes in the file darknet.data

6. Install Darknet and compile it.
```
cd ~
git clone https://github.com/pjreddie/darknet
cd darknet
make
```
7. Get the pretrained model

`wget https://pjreddie.com/media/files/darknet53.conv.74 -O ~/darknet/darknet53.conv.74`


8. Start the training as below, by giving the correct paths to all the files being used as arguments

`cd ~/darknet`

`./darknet detector train //h/darknet.data  //h/darknet-yolov3.cfg ./darknet53.conv.74 > //h/train.log`


9. use code below to graph the loss function : stop the training when loss function is equal to zero for a while

 python3 plotTrainLoss.py /full/path/to/train.log

10. Give the correct path to the modelConfiguration and modelWeights files in object_detection_yolo.py and test any image or video for snowman detection, e.g.
test your new model

`python3 object_detection_yolo.py --image=snowmanImage.jpg`

