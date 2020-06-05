# W251 - Summer 2020
## Homework 6: BERT - Classifying Toxicity
### Tom Goter

### BERT with P100
Notebook file and HTML of output available in this repository.

Reading in dataset of 1.5 million (1M training and 0.5M validation) and tokenizing into masked word parts took 33 minutes and 17 seconds. This averaged out to be 751 sequences tokenized per second. The training itself proceeded at a pace of about 1.43 batches per second. Each batch was 32 sequences, so one epoch is 31250 iterations or steps. This whole process took about 6 hours. At a rate of ~4.07 dollars per hour, this analysis cost approximately $24  (just for training) on the P100.

### BERT with V100
Notebook file and HTML of output available in this repository.

Reading in dataset of 1.5 million (1M training and 0.5M validation) and tokenizing into masked word parts took 25 minutes and 7 seconds. This averaged out to be 1055 sequences tokenized per second. The training itself proceeded at a pace of about 4.75 batches per second. Each batch was 32 sequences, so one epoch is 31250 iterations or steps. This whole process took about 2 hours. At a rate of ~6.29 dollars per hour, this analysis cost approximately $12.50 (just for training) on the V100. The tokenization speed scaled with the price (both about 40-50%) higher. However, during training the V100 crushed the P100 to the tune of a 3x increase. Thus, if you have a very large training set, the V100 will be worth the additional per hour cost both in turnaround time and pure dollar value. If you need to do a lot of preprocessing, etceter, it is less of a bargain. So perhaps you can process on the p100, save your objects and then port to v100 when you are ready for training an inference.
