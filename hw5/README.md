# W251 - Summer 2020
## Homework 5 - TF2 and TF1
### Tom Goter

## Introduction to Tensorflow v2
In this portion of the homework, we were asked to go through two Jupyter Notebooks in a Docker Container on our Jetson device. The first lab was a straightforward introduction to using a Sequential Model in Keras to perform classification on the MNIST data. The provided example in the notebook used a fully connected layer with 128 hidden units.  We were asked to determine whether we could improve the model accuracy. To this end I constructed two challenger models. The first model was simply a two-layer version of the first model with increased regularization to prevent overfitting. This model was able to slightly improve accuracy to the tune of 0.2% (i.e., 97.8% vs 97.6%). The second challenger model was a two-layer convolutional neural network with heavy regularization in the form of dropout after the pooling layers and prior to the classification layer.This model showed a significant increase in performance - achieving a test set accuracy of 98.9%.

The second notebook in the first part of the homework dealt with transfer learning. We were asked to load in a pretraing Mobilent feature extraction model (i.e., the mobile net model pretrained on imaged net with everything but the classification layer). This allows us to put any sort of additional layer(s) on top of all of the convolution layers which have been pre-trained to recognize certain components of images. In our case we replace the 1000 node classification layer that would have been used during ImageNet training with a five node classification layer as we are using the pretrained model to enhance and speed up our ability to classify images of flowers. In order to avoid out-of-memory errors on the Jetson, we use a batch size of 16 instead of 32. We investigate using frozen layers and unfrozen layers in our transfered feature extraction model. In general, we see that either way we see immediate and substantial increases in accuracy during our training which shows us the benefit of the transfer learning.

Notebook files and HTML versions of the completed notebooks are available in this repository as:  
1. beginner.ipynb - Notebook for MNIST classification  
2. beginner.HTML - HTML version of completed MNIST classification notebook with challenger models  
3. transfer_learning_with_hub.ipynb - Notebook for transfer learning with mobilenet  
4. transfer_learning_with_hub.html - HTML version of completed mobilenet transfer learning notebook  

## Comparison to Tensorflow v1
