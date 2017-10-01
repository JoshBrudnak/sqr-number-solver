import csv
from Model import Model

class ClassifyDigits():

  # TODO get csv mnist parsing working
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
 
    model.initModel(30, 3)
    model.trainModel(trainingData, testingData, trainingLabels, testingLabels)
 
train = ClassifyDigits()
train.train()
