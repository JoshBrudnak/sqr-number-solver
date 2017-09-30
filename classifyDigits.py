import tensorflow as tf
import os
from tensorflow.examples.tutorials.mnist import input_data

class classifyDigits():
  inputs = tf.placeholder(tf.float32, [None, 784])
  outputs = tf.placeholder(tf.float32, [None, 10])
  weights = tf.Variable(tf.zeros([784, 10]))
  biases = tf.Variable(tf.zeros([10]))
  
  #silences tensorflow info logging
  os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

  # TODO get csv mnist parsing working
  def parseTrainingData(self):
    trainingData = []
    testingData = []
    trainingLabels = []
    testingLabels = []
    
    trainFile = open("mnist_train.csv")
    testFile = open("mnist_train.csv")
    trainFile.seek(0)

    for line in trainFile:
      reader = tf.TextLineReader()
      trainLabel, trainIm = reader.read(line)
      trainingData.append(trainIm)
      trainingLabels.append(trainLabel)

    for line in testFile:
      reader = tf.TextLineReader()
      testLabel, testIm = reader.read(testFile)
      testingData.append(testIm)
      testingLabels.append(testLabel)

    print(trainLabel)
 
    defaults = [[""],[0]]
    trainData, trainLabels = tf.decode_csv(image, record_defaults=defaults)
    trainImages = tf.image.decode_png(trainData, channels=3)

  def convertImage(imageName):
    imageFile = tf.read_file(im_dir+im_name)
    image = tf.image.decode_png(im_content, channels=3)
    image = tf.cast(image, tf.float32) / 255.
    image = tf.image.resize_images(image, 28, 28)
  
    return image

  def classifyImage(self, data):
    y = tf.matmul(self.inputs, self.weights) + self.biases
    session = tf.Session()
    session.run(y)
    yhat = self.classifyImage()
    print(yhat)

    return y

  def trainModel(self):
    mnistData = input_data.read_data_sets("MNIST_data", one_hot=True)
    self.classifyImage(mnistData)
    #train = tf.train.GradientDescentOptimizer(0.3).minimize(crossEntropy)

    #for _ in range(100):
    #  dataPart = mnist.train.next_batch(100)
    #  train.run(feed_dict={x: dataPart[0], y: dataPart[1]})

    #correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    #accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    #print(accuracy.eval(feed_dict={x: mnist.test.images, y: mnist.test.labels}))
 

digits = classifyDigits()
digits.trainModel()
