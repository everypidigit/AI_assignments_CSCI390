# import numpy as np
import math
#Input: the lists of prior probabilities, likelihood, and test data
#Output: list of corresponding posterior probabilities
#
def posteriorFunc(priorProb, likhd, data):
    posProb = []
    t = []
    n = 0
    normalizationConst = 0
    pwr = sum(data)
    dataLength = len(data)
    pwr_init = dataLength - pwr
    
    for x in priorProb:
        t.append(x * (pow(likhd[n], pwr)) * (pow(1-likhd[n], pwr_init)))
        n = n + 1
    
    normalizationConst = (1 / (sum(t)))
    
    for x in t:
        posProb.append(x * normalizationConst)
        
    return posProb

#Input the lists of prior probabilites, likhd/likelihood, training data, and one test datapoint
#Output: probability that the test datapoint happens
#Note: this function will call posteriorFunc to calculate the posterior probabilites

def predictionFunc (priorProb, likhd, data, fPoint):
    posteriorProbs = posteriorFunc(priorProb, likhd, data)
    predictProb = 0
    i = 0

    if fPoint == 1:
        for x in posteriorProbs:
            predictProb = predictProb + (x * likhd[i])
            i = i + 1   
    elif fPoint == 0:
        for x in posteriorProbs:
            predictProb = predictProb + (x * likhd[i])
            i = i + 1
        return 1-predictProb
     
    return predictProb