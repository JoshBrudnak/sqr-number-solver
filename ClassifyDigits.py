import csv
from Model import Model
import tensorflow as tf

class ClassifyDigits():

  def parseTrainingData(self, csvFile, imageSize):
    data = []
    labels = []
    reader = csv.reader(csvFile)

    for row in reader:
      if(len(data) <= 1000):
        floatRow = []
        labels.append(int(row[0]))
        for i in range(1, len(row)):
          floatRow.append(float(row[i]))
       
        image = []
        for i in range(0, 28):
          index = imageSize * i
          imageRow = []
          for j in range(0, 28):
            imageRow.append([floatRow[index + j]])
          image.append(imageRow)
        data.append(image)
      else:
        break

    return labels, data

  def convertImage(imageName):
    imageFile = tf.read_file(im_dir+im_name)
    image = tf.image.decode_png(im_content, channels=3)
    image = tf.cast(image, tf.float32) / 255.
    image = tf.image.resize_images(image, 28, 28)
  
    return image

  def train(self):
    model = Model()
    trainFile = open("mnist_train.csv")
    testFile = open("mnist_test.csv")

    trainingLabels, trainingData = self.parseTrainingData(trainFile, 28)
    testingLabels, testingData = self.parseTrainingData(testFile, 28) 
 
    #model.initModel(30, 3)
    model.trainModel(trainingData, testingData, trainingLabels, testingLabels)
 

  def imageToFloat(self, images):
    floatImages = []
    for i in range(0, len(images)):
      newimage = []
      for j in range(0, len(images[i])):
        imageRow = []
        for k in range(0, len(images[i][j])):
          imageRow.append([abs(float(images[i][j][k]) - 255)])
        newimage.append(imageRow)
      floatImages.append(newimage)
    return floatImages
 
  def classifyDigitArray(self, images):
    model = Model()
    #model.initModel(30, 2)
    self.train()
    newImages = self.imageToFloat(images)

    probList = [] 
    for i in range(0, len(newImages)):
      numbers = model.classifyImage([newImages[i]])
      session = tf.Session()
      init = tf.global_variables_initializer()
      session.run(init)
      probList.append(session.run(numbers).tolist()[0])
      print(i) 

    foundNumbers = []
    for i in range(0, len(probList)):
      highProb = 0.0
      probIndex = 0
      for j in range(0, len(probList[i])):
        if probList[i][j] > highProb:
          hightProb = probList[i][j]
          probIndex = j
      
      foundNumbers.append(probIndex) 
      
    print(foundNumbers)
    print(len(foundNumbers))
    return foundNumbers
