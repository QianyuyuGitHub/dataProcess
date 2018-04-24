import tensorflow as tf

def geneData():
    dataList = []
    for a in numpy.arange(0.0, 1.0, 0.05):
        x = 2 * numpy.pi * a
        y = numpy.sin(x)
        dataList.append([x, y])
    return dataList
    x = -2 * numpy.pi

def train(dataList):
    # X and Y data
    x_train = dataList[:, 0]
    y_train = dataList[:, 1]

    W = tf.Variable(tf.random_normal([1]), name='weight')
    b = tf.Variable(tf.random_normal([1]), name='bias')

    # Our hypothesis XW+b
    for i in range(len(x_train)):
        x_train[i] = x_train[i]**i
    hypothesis = x_train * W + b

    # cost/loss function
    cost = tf.reduce_mean(tf.square(hypothesis - y_train))

    # Minimize
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
    train = optimizer.minimize(cost)

    # Launch the graph in a session.
    sess = tf.Session()
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    # Fit the line
    for step in range(2001):
       sess.run(train)
       if step % 20 == 0:
           print(step, sess.run(cost), sess.run(W), sess.run(b))

def main():
    dataList = geneData()
    train(dataList)
    # print(calculate_polynomial([1, 2, 3], [5, 7]))


if __name__ == '__main__':
    main()