import tensorflow as tf
import random 
import os

class Model():
  layerDepth = 30
  convolutionLayers = 2
  filterDimentions = [2, 2, 1, 1]
  filters = tf.Variable(tf.truncated_normal(filterDimentions, stddev=0.03)) 
  bias = tf.Variable(tf.truncated_normal([30], stddev=0.03)) 
  init = tf.global_variables_initializer()

  x = tf.placeholder('float', [1, 28, 28, 1])
  y = tf.placeholder('float')
  
  #silences tensorflow info logging
  os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
  sess = tf.Session()

  def initModel(self, depth, layers): 
    saver = tf.train.import_meta_graph("./trained_model/digitClassificationModel.meta")
    saver.restore(self.sess, tf.train.latest_checkpoint('./'))
    graph = tf.get_default_graph()
    self.filters = graph.get_tensor_by_name("filters:0")
    self.bias = graph.get_tensor_by_name("biases")

    self.sess.run(self.init)
    self.layerDepth = depth
    self.convolutionLayers = layers
  
  def classifyImage(self, data):
    image = tf.Variable(data, name="image")

    firstConvLayer = tf.nn.conv2d(
      image,
      self.filters,
      strides=[1, 2, 2, 1],
      padding="SAME"
    )
    firstConvRelu = tf.nn.relu(firstConvLayer)
    convResult = tf.layers.max_pooling2d(inputs=firstConvRelu, pool_size=[2, 2], strides=2)
    convLayer = tf.nn.conv2d(
      convResult,
      self.filters,
      strides=[1, 2, 2, 1],
      padding="SAME"
    )

    reluStep = tf.nn.relu(convLayer)
    poolLayer = tf.layers.max_pooling2d(inputs=reluStep, pool_size=[2, 2], strides=2)
    convResult = poolLayer

    # image flattening layer
    pool2_flat = tf.reshape(convResult, [-1, 4])

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
    total_loss = 0

    for i in range(0, 8):
      print(i)
      batchLabels, batchData = self.getBatchNum(i + 1, 100, trainData, trainLabels)
      yhat = self.classifyImage(batchData)
      session = tf.Session()
      init = tf.global_variables_initializer()
      session.run(init)
      yhatList = session.run(yhat).tolist()

      onehot = tf.one_hot(indices=tf.cast(batchLabels, tf.int32), depth=10)
      loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot, logits=yhat)

      trainOperation = tf.contrib.layers.optimize_loss(
        loss=loss,
        global_step=tf.contrib.framework.get_global_step(),
        learning_rate=0.1,
        optimizer="SGD") 

      session2 = tf.Session()
      session2.run(self.init)
      _, c = session2.run([trainOperation, loss], feed_dict={self.x: batchData, self.y: yhatList})
      total_loss += c

    saver = tf.train.Saver({"filters:0": self.filters})
    saver.save(self.sess, "./trained_model/digitClassificationModel")

    testLoss = 0
    for i in range(0, 1):
      batchLabels, batchData = self.getBatchNum(i + 1, 100, testData, testLabels)
      yhat = self.classifyImage(batchData)
      onehot = tf.one_hot(indices=tf.cast(testLabels[i : i + 1], tf.int32), depth=10)
      testLoss = tf.losses.softmax_cross_entropy(onehot_labels=onehot, logits=yhat)
