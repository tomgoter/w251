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

### Question 3 - See HTML Output in Git Repo

### HW 4 Part 2.1 - TFLite
#### efficientnet-L_quant.tflite
**parrot**
- 1420.8ms
- 1281.1ms
- 1386.6ms
- 1521.6ms
- 1467.7ms  
-------RESULTS--------
1. 89  macaw: 0.93359
2. 91  lorikeet: 0.00391
3. 336  fox squirrel, eastern fox squirrel, Sciurus niger: 0.00000
4. 335  porcupine, hedgehog: 0.00000
5. 334  hamster: 0.00000

**My Cute Soft-coated Wheaten Terrier**
- 1418.8ms
- 1531.6ms
- 1369.3ms
- 1565.0ms
- 1411.2ms  
-------RESULTS--------
1. 203  soft-coated wheaten terrier: 0.18359
2. 186  Norfolk terrier: 0.17188
3. 187  Norwich terrier: 0.14453
4. 185  Irish terrier: 0.12500
5. 192  Airedale, Airedale terrier: 0.09766

**My Delicious Pizza**
- 1774.6ms
- 1714.2ms
- 1523.7ms
- 1627.1ms
- 1453.4ms  
-------RESULTS--------
1. 964  pizza, pizza pie: 0.11719
2. 814  spatula: 0.11719
3. 557  fire screen, fireguard: 0.09375
4. 828  stove: 0.08594
5. 862  toilet seat: 0.06250

**Cute Semi-Domesticated Chipmunk**
- 1507.2ms
- 1427.0ms
- 1516.3ms
- 1728.3ms
- 1361.9ms  
-------RESULTS--------
1. 357  weasel: 0.28906
2. 359  polecat, fitch, foulmart, foumart, Mustela putorius: 0.08203
3. 360  black-footed ferret, ferret, Mustela nigripes: 0.05859
4. 299  mongoose: 0.03906
5. 678  nail: 0.03906

#### efficientnet-M_quant.tflite
**Parrot**
- 545.1ms
- 523.7ms
- 509.9ms
- 723.5ms
- 535.6ms  
-------RESULTS--------
1. 89  macaw: 0.93750
2. 90  sulphur-crested cockatoo, Kakatoe galerita, Cacatua galerita: 0.00391
3. 336  fox squirrel, eastern fox squirrel, Sciurus niger: 0.00000
4. 335  porcupine, hedgehog: 0.00000
5. 334  hamster: 0.00000

**My Cute Soft-coated Wheaten Terrier**
- 618.7ms
- 613.2ms
- 696.6ms
- 868.1ms
- 619.7ms  
-------RESULTS--------
1. 283  tiger cat: 0.11719
2. 204  West Highland white terrier: 0.03906
3. 278  red fox, Vulpes vulpes: 0.03906
4. 282  tabby, tabby cat: 0.03516
5. 192  Airedale, Airedale terrier: 0.03125

**My Delicious Pizza**
- 543.2ms
- 664.1ms
- 499.1ms
- 633.9ms
- 710.6ms  
-------RESULTS--------
1. 964  pizza, pizza pie: 0.33984
2. 814  spatula: 0.12891
3. 965  potpie: 0.08594
4. 963  meat loaf, meatloaf: 0.07422
5. 860  toaster: 0.01562

**Cute Semi-Domesticated Chipmunk**
- 859.9ms
- 567.2ms
- 634.4ms
- 607.2ms
- 611.9ms  
-------RESULTS--------
1. 784  screw: 0.17188
2. 114  snail: 0.17188
3. 678  nail: 0.10547
4. 563  fountain: 0.09766
5. 311  ant, emmet, pismire: 0.08984

#### efficientnet-S_quant.tflite
**Parrot**
- 326.2ms
- 324.0ms
- 321.2ms
- 459.8ms
- 322.2ms  
-------RESULTS--------
1. 89  macaw: 0.87891
2. 93  bee eater: 0.00781
3. 91  lorikeet: 0.00391
4. 337  marmot: 0.00000
5. 336  fox squirrel, eastern fox squirrel, Sciurus niger: 0.00000

**My Cute Soft-coated Wheaten Terrier**
- 328.0ms
- 324.5ms
- 387.3ms
- 486.6ms
- 320.9ms  
-------RESULTS--------
1. 286  Egyptian cat: 0.11328
2. 357  weasel: 0.06641
3. 283  tiger cat: 0.05859
4. 674  mouse, computer mouse: 0.05469
5. 645  matchstick: 0.04297

**My Delicious Pizza**
- 336.6ms
- 680.5ms
- 389.5ms
- 333.5ms
- 347.4ms  
-------RESULTS--------
1. 753  racket, racquet: 0.17188
2. 715  pick, plectrum, plectron: 0.17188
3. 965  potpie: 0.10547
4. 964  pizza, pizza pie: 0.05469
5. 403  acoustic guitar: 0.03906

**Cute Semi-Domesticated Chipmunk**
- 441.1ms
- 471.4ms
- 404.5ms
- 371.7ms
- 405.2ms  
-------RESULTS--------
1. 300  meerkat, mierkat: 0.10938
2. 299  mongoose: 0.06250
3. 337  marmot: 0.06250
4. 107  wombat: 0.04688
5. 336  fox squirrel, eastern fox squirrel, Sciurus niger: 0.04688

#### inception_v4_299_quant.tflite
**Parrot**
- 1744.8ms
- 1765.6ms
- 1874.2ms
- 1882.4ms
- 1781.2ms  
-------RESULTS--------
1. 89  macaw: 0.99609
2. 332  hare: 0.00000
3. 331  wood rabbit, cottontail, cottontail rabbit: 0.00000
4. 335  porcupine, hedgehog: 0.00000
5. 334  hamster: 0.00000

**My Cute Soft-coated Wheaten Terrier**
- 2181.0ms
- 2479.1ms
- 2108.3ms
- 2168.1ms
- 1987.9ms  
-------RESULTS--------
1. 203  soft-coated wheaten terrier: 0.89062
2. 185 Irish terrier: 0.06641
3. 193  cairn, cairn terrier: 0.01562
4. 201  Tibetan terrier, chrysanthemum dog: 0.00781
5. 187  Norwich terrier: 0.00391

**My Delicious Pizza**
- 1613.4ms
- 1619.6ms
- 1592.7ms
- 1710.3ms
- 1571.3ms  
-------RESULTS--------
1. 964  pizza, pizza pie: 0.98438
2. 331  wood rabbit, cottontail, cottontail rabbit: 0.00000
3. 330  sea cucumber, holothurian: 0.00000
4. 334  hamster: 0.00000
5. 1000  toilet tissue, toilet paper, bathroom tissue: 0.00000

**Cute Semi-Domesticated Chipmunk**
- 1799.1ms
- 1758.8ms
- 1936.6ms
- 1762.5ms
- 1690.5ms  
-------RESULTS--------
1. 337  marmot: 0.98047
2. 332  hare: 0.00000
3. 1000  toilet tissue, toilet paper, bathroom tissue: 0.00000
4. 331  wood rabbit, cottontail, cottontail rabbit: 0.00000
5. 335  porcupine, hedgehog: 0.00000

#### mobilenet_v1_1.0_224_quant.tflite
**Parrot**
- 82.2ms
- 81.9ms
- 241.5ms
- 96.1ms
- 94.3ms  
-------RESULTS--------
1. 89  macaw: 0.99609
2. 332  hare: 0.00000
3. 331  wood rabbit, cottontail, cottontail rabbit: 0.00000
4. 335  porcupine, hedgehog: 0.00000
5. 334  hamster: 0.00000

**My Cute Soft-coated Wheaten Terrier**
- 82.0ms
- 81.5ms
- 88.4ms
- 89.1ms
- 104.0ms  
-------RESULTS--------
1. 185  Irish terrier: 0.49609
2. 203  soft-coated wheaten terrier: 0.25391
3. 187  Norwich terrier: 0.13281
4. 227  briard: 0.01953
5. 193  cairn, cairn terrier: 0.01953

**My Delicious Pizza**
- 83.3ms
- 81.7ms
- 82.9ms
- 90.2ms
- 81.0ms  
-------RESULTS--------
1. 964  pizza, pizza pie: 0.75000
2. 938  broccoli: 0.12109
3. 925  guacamole: 0.05078
4. 924  plate: 0.01172
5. 942  acorn squash: 0.00781

**Cute Semi-Domesticated Chipmunk**
- 81.8ms
- 81.6ms
- 84.4ms
- 83.6ms
- 84.5ms  
-------RESULTS--------
1. 105  wallaby, brush kangaroo: 0.35156
2. 337  marmot: 0.21484
3. 357  weasel: 0.05469
4. 299  mongoose: 0.04688
5. 336  fox squirrel, eastern fox squirrel, Sciurus niger: 0.04688

#### mobilenet_v2_1.0_224_quant.tflite
The model outputs trash.

**Parrot**
-------RESULTS--------
481  cash machine, cash dispenser, automated teller machine, automatic teller machine, automated teller, automatic teller, ATM: 25.21760
174  Ibizan hound, Ibizan Podenco: 25.21760
166  black-and-tan coonhound: 25.21760
316  mantis, mantid: 25.21760
757  rain barrel: 25.21760
693  packet: 25.21760
204  West Highland white terrier: 25.21760
860  toaster: 25.21760
467  bullet train, bullet: 25.21760
878  turnstile: 25.21760

#### Question 2: Which model do you think is best and why?
I would go with Inception Net based on my limited testing. It gives correct responses with high confidence. The time for inferrence is comparable to that of efficientnet-L.

### HW 4 Part 2.2 - TensorFlow 1.15
#### mobilenet_v1_100_224

**Parrot**
- 45.7ms
- 27.3ms
- 26.2ms
- 24.0ms

*Label: Confidence*
macaw: 0.99980

**My Cute Soft-coated Wheaten Terrier**
- 198.6ms
- 29.8ms
- 22.8ms
- 25.7ms

*Label: Confidence*
Irish terrier: 0.42554

**My Delicious Pizza**
- 26.2ms
- 25.1ms
- 25.5ms
- 25.5ms

*Label: Confidence*
pizza: 0.71701

**Cute Semi-Domesticated Chipmunk**
- 197.9ms
- 25.2ms
- 24.6ms
- 26.8ms

*Label: Confidence*
marmot: 0.39983

#### mobilenet_v2_130_224

**Parrot**
- 40.3ms
- 35.7ms
- 35.8ms
- 34.7ms

*Label: Confidence*
macaw: 0.85107

**My Cute Soft-coated Wheaten Terrier**

- 38.6ms
- 35.8ms
- 35.5ms
- 35.5ms

*Label: Confidence*
Norwich terrier: 0.16122

**My Delicious Pizza**

- 39.8ms
- 35.8ms
- 35.6ms
- 34.9ms

Label: Confidence
pizza: 0.87503

**Cute Semi-Domesticated Chipmunk**
- 40.7ms
- 38.0ms
- 35.6ms
- 35.5ms

*Label: Confidence*
marmot: 0.60034

#### efficientnet b0
Needed to modify the classification script to add one to the class id as the efficient net does not have a background class as class 0 
**Parrot**
- 43.6ms
- 50.0ms
- 42.5ms
- 39.7ms

*Label: Confidence*
macaw: 0.94196

**My Cute Soft-coated Wheaten Terrier**

- 56.5ms
- 41.4ms
- 40.6ms
- 38.3ms

*Label: Confidence*
soft-coated wheaten terrier: 0.52879


**My Delicious Pizza**

- 40.1ms
- 38.2ms
- 36.7ms
- 40.9ms

*Label: Confidence*
pizza: 0.64217


**Cute Semi-Domesticated Chipmunk**
- 46.7ms
- 41.4ms
- 43.9ms
- 41.7ms

*Label: Confidence*
marmot: 0.38074

#### efficientnet b4
Needed to modify the classification script to add one to the class id as the efficient net does not have a background class as class 0 

**Parrot**
- 300.0ms
- 177.6ms
- 173.5ms
- 182.4ms

*Label: Confidence*
macaw: 0.75135


**My Cute Soft-coated Wheaten Terrier**

- 315.9ms
- 178.1ms
- 169.8ms
- 169.7ms

*Label: Confidence*
soft-coated wheaten terrier: 0.62035

**My Delicious Pizza**

- 350.5ms
- 178.7ms
- 171.8ms
- 179.2ms

*Label: Confidence*
pizza: 0.69223

**Cute Semi-Domesticated Chipmunk**
- 333.5ms
- 175.3ms
- 171.6ms
- 168.7ms

*Label: Confidence*
marmot: 0.71713

#### efficientnet b7
Needed to modify the classification script to add one to the class id as the efficient net does not have a background class as class 0 
**Parrot**
- 999.4ms
- 842.2ms
- 845.1ms
- 871.1ms

*Label: Confidence*
macaw: 0.84907

**My Cute Soft-coated Wheaten Terrier**

- 987.1ms
- 814.1ms
- 836.4ms
- 822.7ms

*Label: Confidence*
soft-coated wheaten terrier: 0.75012

**My Delicious Pizza**

- 1064.0ms
- 810.7ms
- 808.8ms
- 797.9ms

*Label: Confidence*
pizza: 0.78267

**Cute Semi-Domesticated Chipmunk**
- 969.5ms
- 816.4ms
- 818.8ms
- 824.8ms

*Label: Confidence*
marmot: 0.84802

#### Question 3: Did the efficientNet models return the correct classification. If not why, and how would you fix this?
I fixed the classify python script such that the correct class was returned. The source of the problem is that the EfficientNet models assume 1000 classes without a background class. The other models have a background class - i.e., class 0. All models use the same lookup table of classes. Thus, the EfficientNet models need to account for the background class by adding one to the index of the most probable class. After this is done, the script does in fact return the expected classes.

#### Question 4: How big are the models (MB)?
- *MobileNet v1*: 15 MB
- *MobileNet v2*: 19 MB
- *EfficientNet b0*: 19 MB
- *EfficientNet b4*: 69 MB
- *EfficientNet b7*: 234 MB

#### Question 5: How did the performance compare to TFLite?
- Looking at the models, they appear to run more quickly in TF 1.15 than in TFLite.

### HW 4 Part 2.3 - TensorFlow 2.1
#### mobilenet_v1_100_224

**Parrot**
- 738.3ms
- 236.3ms
- 232.3ms
- 206.8ms

*Label: Confidence*
macaw: 0.99980

**My Cute Soft-coated Wheaten Terrier**
- 835.6ms
- 157.7ms
- 177.5ms
- 199.8ms

*Label: Confidence*
Irish terrier: 0.42554

**My Delicious Pizza**
- 773.9ms
- 293.3ms
- 298.1ms
- 265.6ms

*Label: Confidence*
pizza: 0.71701

**Cute Semi-Domesticated Chipmunk**
- 896.2ms
- 284.2ms
- 298.6ms
- 265.9ms

*Label: Confidence*
marmot: 0.39983

#### mobilenet_v2_130_224

**Parrot**

- 829.2ms
- 279.6ms
- 283.8ms
- 276.7ms

*Label: Confidence*
macaw: 0.85107

**My Cute Soft-coated Wheaten Terrier**

- 884.3ms
- 278.9ms
- 256.4ms
- 285.1ms

*Label: Confidence*
Norwich terrier: 0.16122

**My Delicious Pizza**

- 892.9ms
- 298.6ms
- 304.0ms
- 249.6ms

*Label: Confidence
pizza: 0.87503


**Cute Semi-Domesticated Chipmunk**
- 952.6ms
- 301.7ms
- 281.3ms
- 295.1ms

*Label: Confidence*
marmot: 0.60034

#### efficientnet b0
Needed to modify the classification script to add one to the class id as the efficient net does not have a background class as class 0 
**Parrot**
- 977.9ms
- 297.4ms
- 212.3ms
- 301.8ms

*Label: Confidence*
macaw: 0.94196

**My Cute Soft-coated Wheaten Terrier**

- 797.7ms
- 278.2ms
- 255.8ms
- 307.8ms

*Label: Confidence*
soft-coated wheaten terrier: 0.52879

**My Delicious Pizza**

- 827.8ms
- 218.2ms
- 313.7ms
- 238.5ms

*Label: Confidence*
pizza: 0.64217

**Cute Semi-Domesticated Chipmunk**
- 801.1ms
- 315.2ms
- 233.3ms
- 277.3ms

*Label: Confidence*
marmot: 0.38074


#### efficientnet b4
Needed to modify the classification script to add one to the class id as the efficient net does not have a background class as class 0 
**Parrot**
- 858.1ms
- 268.5ms
- 293.7ms
- 287.8ms

*Label: Confidence*
macaw: 0.76850


**My Cute Soft-coated Wheaten Terrier**

- 770.8ms
- 262.9ms
- 232.2ms
- 225.0ms

*Label: Confidence*
soft-coated wheaten terrier: 0.75463


**My Delicious Pizza**

- 817.3ms
- 249.4ms
- 218.3ms
- 377.9ms

*Label: Confidence*
pizza: 0.58870


**Cute Semi-Domesticated Chipmunk**
- 941.0ms
- 236.5ms
- 215.1ms
- 220.1ms

*Label: Confidence*
marmot: 0.73212



#### efficientnet b7
Needed to modify the classification script to add one to the class id as the efficient net does not have a background class as class 0 
**Parrot**
- 1592.0ms
- 407.8ms
- 356.8ms
- 410.2ms

*Label: Confidence*
macaw: 0.93852


**My Cute Soft-coated Wheaten Terrier**

- 1830.3ms
- 400.3ms
- 373.8ms
- 417.2ms

*Label: Confidence*
soft-coated wheaten terrier: 0.79033


**My Delicious Pizza**

- 1653.8ms
- 470.9ms
- 468.6ms
- 459.5ms

*Label: Confidence*
pizza: 0.83019


**Cute Semi-Domesticated Chipmunk**
- 1825.1ms
- 412.4ms
- 458.6ms
- 480.5ms

*Label: Confidence*
fox squirrel: 0.10910

#### Question 6: Compare TF2 performance with TF1.15.
Inference with TF2 was significantly slower than that with TF1.15. Apparently this is expected as found in this [very helpful Stack Overflow post](https://stackoverflow.com/questions/58441514/why-is-tensorflow-2-much-slower-than-tensorflow-1) excerpt below:  
- "as confirmed by a TensorFlow developer, Q. Scott Zhu, TF2 focused development on Eager execution & tight integration w/ Keras, which involved sweeping changes in TF source - including at graph-level. Benefits: greatly expanded processing, distribution, debug, and deployment capabilities. The cost of some of these, however, is speed."

### Jetson Inference

#### GoogleNet
**Parrot**
- image is recognized as 'macaw' (class #88) with 99.951172% confidence
Total         CPU  11.44932ms  CUDA  11.25696ms
**My Cute Soft-coated Wheaten Terrier**
image is recognized as 'hyena, hyaena' (class #276) with 19.055176% confidence
Total         CPU  12.73538ms  CUDA  12.53302ms
**My Delicious Pizza**
image is recognized as 'pizza, pizza pie' (class #963) with 99.169922% confidence
Total         CPU  41.88729ms  CUDA  41.71021ms
**Cute Semi-Domesticated Chipmunk**
image is recognized as 'marmot' (class #336) with 65.380859% confidence
Total         CPU  11.81363ms  CUDA  11.61536ms

#### AlexNet
**Parrot**
image is recognized as 'macaw' (class #88) with 99.951172% confidence
Total         CPU  11.92051ms  CUDA  11.73824ms
**My Cute Soft-coated Wheaten Terrier**
image is recognized as 'Irish terrier' (class #184) with 43.530273% confidence
Total         CPU  12.24803ms  CUDA  12.25197ms
**My Delicious Pizza**
image is recognized as 'pizza, pizza pie' (class #963) with 70.361328% confidence
Total         CPU  11.83098ms  CUDA  11.80643ms
**Cute Semi-Domesticated Chipmunk**
image is recognized as 'dung beetle' (class #305) with 18.212891% confidence
Total         CPU  12.70169ms  CUDA  12.51158ms

#### Inception V4
**Parrot**
image is recognized as 'macaw' (class #88) with 94.433594% confidence
Total         CPU 213.92099ms  CUDA 213.71884ms
**My Cute Soft-coated Wheaten Terrier**
image is recognized as 'standard schnauzer' (class #198) with 87.207031% confidence
Total         CPU 185.27765ms  CUDA 184.97978ms
**My Delicious Pizza**
image is recognized as 'pizza, pizza pie' (class #963) with 33.837891% confidence
Total         CPU 183.88162ms  CUDA 183.85498ms
**Cute Semi-Domesticated Chipmunk**
image is recognized as 'marmot' (class #336) with 50.195312% confidence
Total         CPU 174.25325ms  CUDA 174.23187ms

#### ResNet 152
**Parrot**
image is recognized as 'macaw' (class #88) with 99.804688% confidence
Total         CPU 184.86336ms  CUDA 184.81546ms
**My Cute Soft-coated Wheaten Terrier**
image is recognized as 'soft-coated wheaten terrier' (class #202) with 55.712891% confidence
Total         CPU 170.57799ms  CUDA 170.19058ms
**My Delicious Pizza**
image is recognized as 'pizza, pizza pie' (class #963) with 91.308594% confidence
Total         CPU 143.68022ms  CUDA 143.40199ms
**Cute Semi-Domesticated Chipmunk**
image is recognized as 'marmot' (class #336) with 91.845703% confidence
Total         CPU 147.65044ms  CUDA 147.43996ms

#### Question 7: What models did you use?
I used GoogleNet, AlexNet, InceptionNet and ResNet-152.

#### Question 8: What was the average inference time for model and image combination? What were the return classes and their score?
See output above. The GoogleNet and AlexNet inference times were much less compared to InceptionNet and ResNet. However ResNet is the only network that correctly identified my soft-coated wheaten terrier, and had the strongest (most confident predictions)

#### Question 9: What is quantization? What is its effect on performance and accuracy?
Quantization is a method of reducing model size by reducing the precision of the weights you are storing. Thus, you may be trading off performance but you have a more portable model.

#### Question 10: In your opinion, which framework was best? Why?
For inference at the edge, it appears the TensorRT backed Jetson Inference framework is the best. The inference time is the least, and accuracy remains high when paired with a powerful netowrk such as ResNet-152. Although TFLite with MobileNet performed quite well, as well.
