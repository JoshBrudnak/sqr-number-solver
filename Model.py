import tensorflow as tf
import os

class Model():
  layerDepth = 1
  convolutionLayers = 1
  
  #silences tensorflow info logging
  os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

  def initModel(self, depth, layers): 
    self.layerDepth = depth
    self.convolutionLayers = layers

  def dotProduct(kernel, imageSeg):
    dotProd = 0
    if len(kernel) == len(imageSeq):
      for i in range(0, len(kernel)):
        for j in range(0, len(kernel[i])):
          dotProd += kernel[i][j] * imageSeq[i][j]
    return dotProd

  def classifyImage(self, data, imageLabel):
    image = tf.Variable([data], name="image")
    label = tf.Variable(imageLabel, name="label")
    sess = tf.Session()
    #for i in range(0, 28):
      #print(data[i])

    firstConvLayer = tf.layers.conv2d(
      inputs=image,
      filters=30,
      kernel_size=[2, 2],
      padding="same",
      strides=(2, 2),
      data_format="channels_last",
      activation=tf.nn.relu
    )
    convResult = tf.layers.max_pooling2d(inputs=firstConvLayer, pool_size=[2, 2], strides=2)

    for _ in range(0, self.convolutionLayers - 2):
      convLayer = tf.layers.conv2d(
        inputs=convResult,
        filters=30,
        kernel_size=[2, 2],
        padding="same",
        strides=(2, 2),
        data_format="channels_last",
        activation=tf.nn.relu)
      poolLayer = tf.layers.max_pooling2d(inputs=convLayer, pool_size=[2, 2], strides=2)
      convResult = poolLayer

      #init = tf.global_variables_initializer()
      #sess.run(init)
    pool2_flat = tf.reshape(convResult, [-1, 120])
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense, rate=0.4, training=True)
    probabilities = tf.layers.dense(inputs=dropout, units=10)

    return probabilities 

  def trainModel(self, trainData, testData, trainLabels, testLabels):
    loss = 0
    sess = tf.Session()

    for i in range(0, 100):
      yhat = self.classifyImage(trainData[i], trainLabels[i])
      onehot = tf.one_hot(indices=tf.cast(trainLabels[i:i + 1], tf.int32), depth=10)
      loss += tf.losses.softmax_cross_entropy(onehot_labels=onehot, logits=yhat)
      print(i)
    
    trainOperation = tf.contrib.layers.optimize_loss(
        loss=loss,
        global_step=tf.contrib.framework.get_global_step(),
        learning_rate=0.1,
        optimizer="SGD") 

    init = tf.global_variables_initializer()
    sess.run(init)
    sess.run(trainOperation)

    testLoss = 0
    for i in range(0, 100):
      yhat = self.classifyImage(testData[i], testLabels[i])
      init = tf.global_variables_initializer()
      sess.run(init)
      print(testLabels[i])
      print(testLabels[i : i + 1])
      print(sess.run(yhat))
      onehot = tf.one_hot(indices=tf.cast(testLabels[i : i + 1], tf.int32), depth=10)
      testLoss += tf.losses.softmax_cross_entropy(onehot_labels=onehot, logits=yhat)
      print(i)

    sess.run(init)
    print(sess.run(testLoss))
