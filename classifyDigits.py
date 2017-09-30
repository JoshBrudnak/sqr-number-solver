import tensorflow as tf
import os
import csv
import math 

class classifyDigits():
  
  #silences tensorflow info logging
  os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

  # TODO get csv mnist parsing working
  def parseTrainingData(self, csvFile, imageSize):
    data = []
    labels = []
    reader = csv.reader(csvFile)

    for row in reader:
      if(len(data) <= 1000):
        intRow = []
        labels.append(int(row[0]))
        for i in range(1, len(row)):
          intRow.append(int(row[i]))
       
        image = []
        for i in range(0, 28):
          index = imageSize * i
          image.append(intRow[index : index + imageSize])
        
        data.append(image)
      else:
       break

    print(len(data))
    return labels, data

  def convertImage(imageName):
    imageFile = tf.read_file(im_dir+im_name)
    image = tf.image.decode_png(im_content, channels=3)
    image = tf.cast(image, tf.float32) / 255.
    image = tf.image.resize_images(image, 28, 28)
  
    return image

  def trainModel(self):
    trainFile = open("mnist_train.csv")
    testFile = open("mnist_test.csv")

    trainingLabels, trainingData = self.parseTrainingData(trainFile, 28)
    testingLabels, testingData = self.parseTrainingData(testFile, 28) 

train = classifyDigits()
train.trainModel()
