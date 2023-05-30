import numpy as np
import math
import random

in_dim = 785 # input dimension
out_dim = 10 # number of classes (0-9)
eta = 0.374 # Learning rate. You might try different rates (between 0.001 and 1) to maximize the accuracy

def Weight_update(feature, label, weight_i2o):
	##
	#Update the weights for a train feature.
		# Inputs:
			# feature: feature vector (ndarray) of a data point with 785 dimensions. Here, the feature represents a handwritten digit 
			         # of a 28x28 pixel grayscale image, which is flattened into a 785-dimensional vector (include bias)
			# label: Actual label of the train feature 
			# weight_i2o: current weights with shape (in_dim x out_dim) from input (feature vector) to output (digit number 0-9)
		# Return: updated weight
	##
	#"*** YOUR CODE HERE ***"
 
    actual_label = int(label)
    mweight = np.matrix(feature @ weight_i2o)
    predicted_labels = np.argmax((mweight), axis=None)
    
    if predicted_labels is actual_label: pass
     
    weight_i2o[:, actual_label] = (weight_i2o[:, actual_label] + feature)		
    weight_i2o[:, predicted_labels] = (weight_i2o[:, predicted_labels] - feature)

    return weight_i2o
    

def get_predictions(dataset, weight_i2o):
	#"""
	#Calculates the predicted label for each feature in dataset.
		# Inputs:
			# dataset: a set of feature vectors with shape  
			# weight_i2o: current weights with shape (in_dim x out_dim)
		# Return: list (or ndarray) of predicted labels from given dataset
	#"""
	#"*** YOUR CODE HERE ***"
 
    mprediction = np.matrix(dataset @ weight_i2o)
    
    # 1 means just one max value per axis is being given to pred
    pred = np.array(mprediction.argmax(axis=1, out=None))
    
    return pred
    
	

def train(train_set, labels, weight_i2o):
	#"""
	#Train the perceptron until convergence.
	# Inputs:
		# train_set: training set (ndarray) with shape (number of data points x in_dim)
		# labels: list (or ndarray) of actual labels from training set
		# weight_i2o:
	# Return: the weights for the entire training set
	#"""
 
    for i in range(0, train_set.shape[0]):        
        weight_i2o = Weight_update(train_set[i, :], labels[i], weight_i2o)        
    return weight_i2o