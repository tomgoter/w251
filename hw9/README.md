# W251 - Summer 2020
## Homework 9
## Tom Goter

This homework was quite the learning experience. I started off by provisioning two P100 nodes in WDC07 datacenter, as V100s were not available. However, it took about five hours to transfer the data, and they trained slow. So following this I switched over to provisioning from the London data center, which was closer to the raw data (~2 hours for downloading), and V100 GPUs were available. Unfortunately when I first spun my cluster up I did not upgrade the maximum port speed. I trained a model for about 24 hours, but only got through about 2600 steps (~30 seconds per step). I knew something wasn't quite right, so after poking at it I realized that the port speed could be increased to 1000Mbps. After doing this and restarting the nodes, I started training closer to 1.7 seconds per step or about 17x faster. I spent a good chunk of my monthly credit learning this lesson, but it will stick with me for a while.

1. How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
- I went through a series of evolutions on training. I used a pair of V100s in London04; however, these were only training at a rate of about 30 seconds per step. Based on throughput of other individuals, this was estimated to be ~15x slower than expected. My network was monitored using nmon and found that it was pretty steady at 12.5K KB/s which also appeared to be slower than others were seeing. Given that this wasn't changing, I considered it may be a function of the data center. So after training for 14 hours and only getting through 1700 steps (and spending 200 credit dollars), I decided to spin up another pair in the Dallas12 data center. I basically hit the same issue in that my GPUs were maxed out at 100% and my network traffic was maxing out less then 13000 KB/s. So I killed by Dallas servers and let the London servers keep plugging away.




2. Do you think your model is fully trained? How can you tell?
3. Were you overfitting?
4. Were your GPUs fully utilized?
**5. Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?**
Yes, see the summary discussion. I did not upgrade the port speed from the default of 100Mbps to 1000Mbps. The net effect of this was not a 10x slowdown, but a 17x slowdown (30 seconds per step vs 1.7 seconds per step). So clearly the network is the bottleneck.
6. Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?
7. How big was your training set (mb)? How many training lines did it contain?
The English training set is 593MB, and contains more than 4.5 million sentences. Obviously since this is a translation problem there are the same number of German sentences meaning we are really training on over 1 GB of data.
8. What are the files that a TF checkpoint is comprised of?
- *index file* - This file has a list of all of the checkpoints that were created. Typically when restoring a checkpoint, it will try to load the latest checkpoint from the index file. 
- *meta file* - This file contains the graph structure of your TensorFlow model. Basically this is the connections of all the nodes and edges that represent your various operations and transformations. 
- *Data file* - this file actually has the weights for all of your nodes in it. 
9. How big is your resulting model checkpoint (mb)?
The data file is about 813 MB, and the meta file is about 16 MB. The index file is obviously tiny. So in total there is aobut 830MB of data for the checkpoint.
10. Remember the definition of a "step". How long did an average step take?
1.8 seconds per step for the final model with the upgraded port speed. 30 seconds per step with the 100 Mbps max port speed.
11. How does that correlate with the observed network utilization between nodes?
As noted in the discussion above, the network was the bottleneck. Increasing the network utilization or network speed will reduce the time per step to a point, until the GPU itself becomes limiting.
