import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

trX = np.linspace(-1, 1, 101)
trY = 2 * trX + np.random.randn(*trX.shape) * 0.4 + 0.2 # create a y value which is approximately linear but with some random noise

plt.scatter(trX,trY)
plt.plot (trX, .2 + 2 * trX)
plt.show()

#...
X = tf.placeholder("float", name="X") # create symbolic variables
Y = tf.placeholder("float", name = "Y")

with tf.name_scope("Model"):

    def model(X, w, b):
        return tf.multiply(X, w) + b # We just define the line as X*w + b0  

    w = tf.Variable(-1.0, name="b0") # create a shared variable
    b = tf.Variable(-2.0, name="b1") # create a shared variable
    y_model = model(X, w, b)


with tf.name_scope("CostFunction"):
    cost = (tf.pow(Y-y_model, 2)) # use sqr error for cost function

train_op = tf.train.GradientDescentOptimizer(0.05).minimize(cost)


sess = tf.Session()
init = tf.global_variables_initializer()
tf.train.write_graph(sess.graph, '/tmp/linear','graph.pbtxt')
cost_op = tf.summary.scalar("loss", cost)
merged = tf.summary.merge_all()
sess.run(init)
writer = tf.summary.FileWriter('/tmp/linear', sess.graph)

for i in range(100):
    for (x, y) in zip(trX, trY): 
        sess.run(train_op, feed_dict={X: x, Y: y})    
        summary_str = sess.run(cost_op, feed_dict={X: x, Y: y})
        writer.add_summary(summary_str, i)       
    b0temp=b.eval(session=sess)
    b1temp=w.eval(session=sess)
    plt.plot (trX, b0temp + b1temp * trX )


print((sess.run(w))) # Should be around 2 
print((sess.run(b))) #Should be around 0.2


plt.scatter(trX,trY)
plt.plot (trX, sess.run(b) + trX * sess.run(w))
plt.show()
