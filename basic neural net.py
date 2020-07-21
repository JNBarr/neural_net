# basic neural net, james b author
input_set = np.array([[0,1,0],
                      [0,0,1]
                      [1,0,0],
                      [1,1,0],
                      [1,1,1],
                      [0,1,1],
                      [0,1,0]])
#dependent variables
labels = np.array([[1,
                    0,
                    0,
                    1,
                    1
                    0,
                    1]])
labels = labels.reshape(7,1)
# to convert these labels to a "vector"
# now define hyperparameters
np.random.seed(42)
weights = np.random.rand(3,1)
bias = np.random.rand(1)
lr = 0.05 # this is the learning rate
# activation function (derivative, sigmoid funct)
def sigmoid(x):
    return 1/(1+np.exp(-x))
# funct to calc deriviate of sig funct
def sigmoid_derivative(x):
    return sigmoid(x)((1-sigmoid(x))

# train ANN model (25,000 times)
for epoch in range(25000):
    inputs = input_setXW = np.dot(inputs, weights)+ bias
    z = sigmoid(XW)
    error = z - labels
    print(error.sum())
    dcost = error
    dpred = sigmoid_derivative(z)
    z_del = dcost * depred
    inputs = input_set.T
    weights = weights - lr*np.dot(inputs, z_del)
    
    for num in z_del:
        bias = bias - lr*num

        ## not sure if this in in the for, but oh well
        single_pt = np.array([1,0,0])
        result = sigmoid(np.dot(single_pt, weights) + bias)
        print(result)
        #output apprently something like 0.01010301 etc (not exact)
        single_pt = np.array([0,1,0])
        result = sigmoid(np.dot(single_pt, weights) + bias)
        print(result)
        #output shoudl eb something like 0.9940207 etc 

# if the data were non linearly seperated, the ANN
# would not be able to classify that type of data
    