# W251 - Summer 2020
## Homework 4 - Deep Learning 101
### Tom Goter

### Question 2: ConvnetJS MNIST Demo
#### Name all the layers in the network, describe what they do.
- The first part of our network is our input which generally isn't included in the layer count. It is specified as 24x24 which means the input images should all be of that dimension.
- The first layer is the convolution layer with a kernel size of (5,5) and a depth of 8 (i.e., number of channels). Since there is padding of 2 on all dimensions. The output of this layer will be of dimensions (24,24,8). Basically what we are doing is looking at localized blocks of 25 pixels and figuring out how to use this information to help classify our digits. We have 8 different filters which are all randomly initialized in order to learn different aspects.
- The second layer is a pooling layer that is 2x2 with stride 2. Basically this layer slides over the activations from the previous convolution layer and for every four pixels picks out the maximum activation in that 2x2 patch. In this way this layer is performing dimensionality reduction such that the output of this layer has dimension (12,12,8)
- Next we have another convolution layer of the same dimension but with an additional 8 channels as the first layer. So now we are looking for features of what was previously determined to be important through the first convolution and pooling layers. Again no data is lost due to the padding so the output dimensions of this layer is (12,12,16).
- Next we have another pooling layer. This time the pooling layer is larger. It is (3x3) with stride 3. So the output of our previous layer is reduced by a factor of 3 to (4,4,16)
- Finally we go to a softmax layer with 10 classes. In order to reduce to 10 classes, we basically flatten the remaining (4,4,16) or 256 neurons and then fully connect those to our 10 classification neurons. We use a softmax which basically uses an exponential of one class logit divided by the sum of exponentials of all class logits in order to normalize all logits to sum to 1.0. Thus the final value attributed to each class can be considered a probability of being in that class.
#### Experiment with the number and size of filters in each layer. Does it improve the accuracy?
- Obviously it depends on how you change them. I looked at increasing the filter depth in the first convolution layer and decreasing the kernel dimension of the second convolution layer. I achieved similar validation accuracy but had perhaps a little bit more of an overfitting problem when I started with some many channels.
#### Remove the pooling layers. Does it impact the accuracy?
- Yes. It appears to reduce overall validation accuracy on the order of 5% or so. It also reduces training accuracy by about the same. 
#### Add one more conv layer. Does it help with accuracy?
- I added one more convolution layer prior to the final pooling layer. It led to very similar performance as the original network.
#### Increase the batch size. What impact does it have?
- I increased batch size from 20 to 30. It seemed to reduce validation accuracy and increase overfitting.
#### What is the best accuracy you can achieve? Are you over 99%? 99.5%?
- Training accuracy was achieved on this level but validation accuracy was topping out around 97%.
eo
