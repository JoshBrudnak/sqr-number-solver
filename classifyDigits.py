import tensorflow as tf

class classifyDigits():
  x = tf.placeholder(tf.float32, [None, 10])
  weights = tf.Variable(tf.zeros([10, 10]))
  biases = tf.Variable(tf.zeros([10]))

  def parseTrainingData():
    trainFile = tf.train.string_input_producer("mnist_train.csv")
    testFile = tf.train.string_input_producer("mnist_train.csv")

    reader = tf.TextLineReader()
    label, image = reader.read(trainFile)
    label, image = reader.read(testFile)
 
    defaultLabels = tf.Variable(tf.zeros([784]))
    trainData, trainLabels = tf.decode_csv(image, record_defaults=defaultLabels)

  def convertImage(imageName):
    imageFile = tf.read_file(im_dir+im_name)
    image = tf.image.decode_png(im_content, channels=3)
    image = tf.cast(image, tf.float32) / 255.
    image = tf.image.resize_images(image, 28, 28)
  
    return image

  def classifyImage():
    y = tf.nn.softmax(tf.matmul(x, weights) + biases)

  def trainModel(trainData, testData):
    y = tf.nn.softmax(tf.matmul(x, weights) + biases)
