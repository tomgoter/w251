# W251 - Summer 2020
## Homework 6: BERT - Classifying Toxicity
### Tom Goter

### Notes
V100 Notebook and HTML file have the complete results including for question 8. The P100 notebook froze after validation inference and before the AUC score was calculated. For the sake of saving my credits, I did not rerun. The training used the same seed as the V100 so the results are the same. The most and least toxic comments on the V100 were determined both after running one epoch and again after running for two epochs (instead of 1). The most and least toxic comments on the P100 file were determined after the development. 

### BERT with P100
Notebook file and HTML of output available in this repository.

Reading in dataset of 1.5 million (1M training and 0.5M validation) and tokenizing into masked word parts took 33 minutes and 17 seconds. This averaged out to be 751 sequences tokenized per second. The training itself proceeded at a pace of about 1.43 batches per second. Each batch was 32 sequences, so one epoch is 31250 iterations or steps. This whole process took about 6 hours. At a rate of ~4.07 dollars per hour, this analysis cost approximately $24  (just for training) on the P100.

### BERT with V100
Notebook file and HTML of output available in this repository.

Reading in dataset of 1.5 million (1M training and 0.5M validation) and tokenizing into masked word parts took 25 minutes and 7 seconds. This averaged out to be 1055 sequences tokenized per second. The training itself proceeded at a pace of about 4.75 batches per second. Each batch was 32 sequences, so one epoch is 31250 iterations or steps. This whole process took just under 2 hours. Inference on 500K comments, was performed at a rate of ~17 iterations per second (544 examples per second) for a total inference time of ~15 minutes. I achieved an overall AUC score of 0.9699; whereas, I topped out at 0.934 in HW4.

Between training and inference, I used just over two hours of resources on the V100.  At a rate of ~6.29 dollars per hour, this analysis cost approximately $12.50 on the V100. The tokenization speed scaled with the price (both about 40-50%) higher. However, during training (and inference) the V100 crushed the P100 to the tune of a 3x increase. Thus, if you have a very large training set, the V100 will be worth the additional per hour cost both in turnaround time and pure dollar value. If you need to do a lot of preprocessing, etceter, it is less of a bargain. So perhaps you can process on the p100, save your objects and then port to v100 when you are ready for training or inference.

### Question 8 - 
For question 8 I trained for two epochs on the V100. Overall our validation score hardly changed with the additional pass over the data. The final validation score was 0.96968 (vice 0.9699 after one epoch). The training loss did go down signaling that there is potentially some overfitting going on with the current set of hyperparameters. See the V100 Notebook or HTML for the results.
