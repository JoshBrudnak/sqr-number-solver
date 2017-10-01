import tensorflow as tf
import random 
import os

class Model():
  layerDepth = 30
  convolutionLayers = 1
  filterDimentions = [2, 2, 1, 1]
  filters = tf.Variable(tf.truncated_normal(filterDimentions, stddev=0.03)) 
  bias = tf.Variable(tf.truncated_normal([30], stddev=0.03)) 
  
  #silences tensorflow info logging
  os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

  def initModel(self, depth, layers): 
    self.layerDepth = depth
    self.convolutionLayers = layers
  
  def initFilters(self):
    initialFilters = []
    for i in range(0, self.convolutionLayers):
      filt = []
      filt.append([[[random.random()]], [[random.random()]]])
      filt.append([[[random.random()]], [[random.random()]]])
      initialFilters.append(filt) 
    print(initialFilters)
    self.filters= tf.Variable(initialFilters)
    init = tf.global_variables_initializer()
    self.sess.run(init)
    self.sess.run(self.filters)

  def dotProduct(kernel, imageSeg):
    dotProd = 0
    if len(kernel) == len(imageSeq):
      for i in range(0, len(kernel)):
        for j in range(0, len(kernel[i])):
          dotProd += kernel[i][j] * imageSeq[i][j]
    return dotProd

  def classifyImage(self, data, imageLabel):
    image = tf.Variable(data, name="image")

    firstConvLayer = tf.nn.conv2d(
      image,
      self.filters,
      strides=[1, 2, 2, 1],
      padding="SAME"
    )
    firstConvRelu = tf.nn.relu(firstConvLayer)
    convResult = tf.layers.max_pooling2d(inputs=firstConvRelu, pool_size=[2, 2], strides=2)

    for i in range(0, self.convolutionLayers - 2):
      convLayer = tf.nn.conv2d(
        image,
        self.filters,
        strides=[1, 2, 2, 1],
        padding="SAME"
      )
      
      reluStep = tf.nn.relu(convLayer)
      poolLayer = tf.layers.max_pooling2d(inputs=reluStep, pool_size=[2, 2], strides=2)
      convResult = poolLayer

    # image flattening layer
    pool2_flat = tf.reshape(convResult, [-1, 49])

    # fully connected layer
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense, rate=0.4, training=True)
    probabilities = tf.layers.dense(inputs=dropout, units=10)

    return probabilities

  def getBatchNum(self, batchNum, elements, trainData, labels):
    data = []
    lab = []
    for i in range(0, batchNum):
      data.append(trainData[i])
      lab.append(labels[i])
   
    return lab, data
    
  
  def trainModel(self, trainData, testData, trainLabels, testLabels):
    loss = 0
    sess = tf.Session()

    for i in range(0, 5):
      print(i)
      batchLabels, batchData = self.getBatchNum(i + 1, 100, trainData, trainLabels)
      yhat = self.classifyImage(batchData, batchLabels)
      onehot = tf.one_hot(indices=tf.cast(batchLabels, tf.int32), depth=10)
      loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot, logits=yhat)

      trainOperation = tf.contrib.layers.optimize_loss(
        loss=loss,
        global_step=tf.contrib.framework.get_global_step(),
        learning_rate=0.1,
        optimizer="SGD") 

    init = tf.global_variables_initializer()
    sess.run(init)
    saver = tf.train.Saver()
    saver.save(sess, "digitClassificationModel")

    testLoss = 0
    for i in range(0, 1):
      batchLabels, batchData = self.getBatchNum(i + 1, 100, testData, testLabels)
      yhat = self.classifyImage(batchData, batchLabels)
      onehot = tf.one_hot(indices=tf.cast(testLabels[i : i + 1], tf.int32), depth=10)
      testLoss = tf.losses.softmax_cross_entropy(onehot_labels=onehot, logits=yhat)
      print(i)
