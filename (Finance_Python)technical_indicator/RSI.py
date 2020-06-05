import numpy as np
import matplotlib.pyplot as plt
import csv

def RSI(A):
    up=[]
    down=[]
    for i in range(len(A)-1):
        if A[i+1]>A[i]:
            up.append(A[i+1]-A[i])
        else:
            down.append(A[i]-A[i+1])
    if up==[]:
        return 0
    elif down==[]:
        return 100
    else:
        Average_Up=sum(up)/len(up)
        Average_Down=sum(down)/len(down)
        return 100-(100/(1+Average_Up/Average_Down))

def RSI_performance_corr(S,n,m):
    #S is the array of daily price of underlying (stock, commodity, etc.)
    #n is the number of days used to compute RSI index (recommend: 14)
    #m means calculate the performance of next m days (recommend: 1)
    RSIarray=[]
    for i in range(n-1,len(S)-m):
        RSIarray.append(RSI(S[i-n+1:i+1]))
    Performance=[]
    for i in range(n-1,len(S)-m):
        Performance.append((S[i+m]/S[i]-1)*100)
    C=np.corrcoef(RSIarray,Performance)
    plt.scatter(RSIarray, Performance)
    plt.show()
    return C[0,1]


stockprice=[]
with open("SP500.csv") as csvfile:
    reader=csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        stockprice.append(row[3])

print(RSI_performance_corr(stockprice,14,7))