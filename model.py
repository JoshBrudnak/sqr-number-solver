import tensorflow as tf
import os

class Model():
  inputs = 1 
  outputs = 1 
  layerDepth = 1 
  convolutionLayers = 1 
  
  #silences tensorflow info logging
  os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

  def initModel(self, inputs, outputs, depth, layers): 
    self.inputs = inputs
    self.outputs = outputs
    self.layerDepth = depth
    self.convolutionLayers = layers

  def dotProduct(kernel, imageSeg):
    dotProd = 0
    if len(kernel) == len(imageSeq):
      for i in range(0, len(kernel)):
        for j in range(0, len(kernel[i])):
          dotProd += kernel[i][j] * imageSeq[i][j]
    return dotProd
       
  def getNodeResult():
    

  def classifyImage(self, data, imageLabel):
    image = tf.Variable(data, name="image")
    label = tf.Variable(label, name="label")

    convResult = 0
    for i in range(0, convolutionLayers):
      convLayer = tf.layers.conv2d(
        inputs=image,
        filters=10,
        kernel_size=[2, 2],
        padding="same",
        activation=tf.nn.relu)
      poolLayer = tf.layers.max_pooling2d(inputs=convLayer, pool_size=[2, 2], strides=2)
      convResult = poolLayer
    
    pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.layers.dropout(
      inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN) 
    
    logits = tf.layers.dense(inputs=dropout, units=10)
    probabilities = tf.nn.softmax(logits, name="softmax_tensor")

    return probabilities 

  def trainModel(self, trainData, testData, trainLabels, testLabels):
    for i in range(0, len(trainData)):
      self.classifyImage(trainData[i], trainLabels[i])
 

digits = classifyDigits()
digits.trainModel()
