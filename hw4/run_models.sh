#!/bin/bash

# I should have started with this :(



# Starting with TensorFlow 1.15 Efficient Net b4

for model in 'b4' 'b7'
do
for test_image in 'parrot' 'stormy' 'pizza' 'chunker'
do
# Flush buffers
sh flush_buffers.sh
python3 classifier.py -m https://tfhub.dev/google/efficientnet/${model}/classification/1 \
                      -i /home/tom/w251/w251/hw4/images/${test_image}.jpg
done
done

