from sklearn import linear_model
import matplotlib.pyplot as plt
import math


reg = linear_model.LinearRegression()
reg.fit([[0,1,2], [1,3,6], [9,6,12]], [0, 1, 2])
print(reg.coef_) #simple linear regression y=a1x1+a2x2+a3x3
#x = [0.01*i for i in range(1000)]
#y = [math.sin(0.01*i) for i in range(1000)]

#plt.plot(x,y)
#plt.show()