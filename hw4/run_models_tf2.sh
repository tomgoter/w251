#!/bin/bash

# I should have started with this :(



# Starting with TensorFlow 1.15 Efficient Net b4

#for model in 'imagenet/mobilenet_v1_100_224/classification/4'\
#             'imagenet/mobilenet_v2_130_224/classification/4'\
for model in 'efficientnet/b0/classification/1'\
	     'efficientnet/b4/classification/1'\
             'efficientnet/b7/classification/1'
do
url="https://tfhub.dev/google/${model}"
echo "Looking for model at: ${url}"
for test_image in 'parrot' 'stormy' 'pizza' 'chunker'
do
# Flush buffers
sh ../tf1\.15/flush_buffers.sh
python3 classifier.py -m ${url} \
                      -i /home/tom/w251/w251/hw4/images/${test_image}.jpg
done
done

