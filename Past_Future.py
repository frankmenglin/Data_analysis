import numpy as np
import matplotlib.pyplot as plt
import csv
import math

def past_future_corr(S,n,m):
    #S is the array of daily price of underlying (stock, commodity, etc.)
    #n means calculate the performance of past n days
    #m means calculate the performance of next m days
    Past=[]
    for i in range(n,len(S)-m):
        Past.append((S[i]/S[i-n]-1)*100)
    Future=[]
    for i in range(n,len(S)-m):
        Future.append((S[i+m]/S[i]-1)*100)

    C=np.corrcoef(Past,Future)
    #plt.scatter(Past, Future)
    #plt.show()
    return C[0,1]


stockprice=[]
#with open("SP500.csv") as csvfile:
#    reader=csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
#    for row in reader:
#        stockprice.append(row[3])

stockprice.append(1.0)
Time=[1]
Ra=[0]
for i in range(2000000):
    current=stockprice[-1]
    R=np.random.normal(0,1,1)
    Ra.append(R[0])
    Time.append(Time[-1]+1)
C=np.corrcoef(Ra[0:-1],Ra[1:])
print(C)
#plt.scatter(Time,Ra)
#plt.show()
#print(past_future_corr(stockprice,1,1))
#A=np.zeros((20,20))
#absmaxcorr=0
#index_past=1
#index_future=1
#for i in range(1,20):
#    for j in range(1,20):
#        A[i-1][j-1]=past_future_corr(stockprice,i,j)
#        if abs(A[i-1][j-1])>absmaxcorr:
#            absmaxcorr=A[i-1][j-1]
#            index_past=i
#            index_future=j
#print(absmaxcorr)
#print(index_past)
#print(index_future)