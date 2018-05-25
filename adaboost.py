import numpy as np  
from numpy import *  
from math import *  
def LoadData():  
    data=matrix([[1.,2.1],  
              [ 2. , 1.1],  
              [ 1.3, 1. ],  
              [ 1. , 1. ],  
              [ 2. , 1. ]])  
    label=np.mat([1.0,1.0,-1.0,-1.0,1.0]).T  
    return data,label  
def stumpClassify(dataSet,dim,thresholdValue):  
    m,n=np.shape(dataSet)  
    resultArray=zeros((m,1))  
    for i in range(m):  
        if dataSet[i,dim]>=  thresholdValue:  
            resultArray[i]=1  
        else:  
            resultArray[i]=-1  
    return resultArray  
def bestStump(dataSet,label,D):#D is weight vector,cloum.label is cloum vector  
    minErr=float(inf)  
    numStep=10  
    stump={}  
    m,n=np.shape(dataSet)  
    bestResult=mat(zeros((m,1)))  
    for i in range(n):  
        minValue=dataSet[:,i].min()  
        maxValue=dataSet[:,i].max()  
        minStep=float(maxValue-minValue)/numStep  
        for j in range(-1,numStep+1):  
            thresholdValue=minValue+float(j)*minStep  
            resultArray=stumpClassify(dataSet,i,thresholdValue)  
            error=mat(ones((m,1)))  
            error[resultArray==label]=0  
            weightError=D.T*error   #加权平均  
            if weightError<minErr:  
                minErr=weightError  
                stump['dim']=i  
                stump['thresholdValue']=thresholdValue  
                bestResult=resultArray.copy()  
    return stump,bestResult,minErr  
def buildBootsing(data,label,maxNumOfStump):  
    m,n=shape(data)  
    D=mat(ones((m,1)))/m  #初始权重为1/m  
    stumpList=[]  
    alphaList=[]  
    Hx=mat(zeros((m,1)))  
    for i in range(maxNumOfStump):  
        stump,result,error=bestStump(data,label,D)  
        alpha=log((1-error)/error,exp(1))/2  
        alphaList.append(alpha)  
        stump['alpha']=alpha  
        stumpList.append(stump)  
        temp=np.multiply(label,result)  
        print(temp)  
        temp=np.exp(-1*alpha*temp)  
        D=np.multiply(D,temp)/D.sum()  
        resultI=stumpClassify(data,stumpList[i]['dim'],\  
                                stumpList[i]['thresholdValue'])  
        Hx+=resultI*stumpList[i]['alpha']  
        globalError=mat(ones((m,1)))  
        globalError[sign(Hx)==label]=0  
        errorRate=sum(globalError)/m  
        if errorRate==0:  
            print('Sucess');break  
    return stumpList  