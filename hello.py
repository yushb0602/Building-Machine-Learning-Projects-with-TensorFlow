import tensorflow as tf
a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_a")
c = tf.multiply(a,b, name="mul_c")
d = tf.add(a,b, name="add_d")
e = tf.add(c,d, name="add_e")

sess = tf.Session()
sess.run(e)
output = sess.run(e)

writer = tf.summary.FileWriter('/tmp/tensorflow_logs', graph=sess.graph)

print(sess.run(e))
