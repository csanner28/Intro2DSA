import numpy

#function to iterate through the loss calc and minimize it
def minLossCalc(w, b, x, y):
    #initialization
    X = numpy.array([[i,1] for i in x], dtype=int)
    Y = numpy.array([[i] for i in y], dtype=int)
    WB = numpy.array([[w], [b]], dtype=int)
    N = len(x)
    return type(X.value)

    loss = 1
    newLoss = 0
    count = 0

    #main loop
    #while(loss > newLoss):
    for i in range(10):
        loss = (numpy.sum((Y-numpy.dot(X,WB))**2))
        lossW = (numpy.sum(numpy.dot((2*(Y-numpy.dot(X,WB))).T, X.T[0])))
        lossB = (numpy.sum(2*(Y-numpy.dot(X,WB))))/N
        WB -= numpy.array([[(lossW/100000)], [(lossB/100000)]], dtype=int)
        newLoss = (numpy.sum((Y-numpy.dot(X,WB))**2))
        print(loss, newLoss)
        count += 1
    return [count, loss, newLoss, WB]