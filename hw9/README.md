# W251 - Summer 2020
## Homework 9
## Tom Goter

This homework was quite the learning experience. I started off by provisioning two P100 nodes in WDC07 datacenter, as V100s were not available. However, it took about five hours to transfer the data, and they trained slow. So following this I switched over to provisioning from the London data center, which was closer to the raw data (~2 hours for downloading), and V100 GPUs were available. These GPUs however were only training at a rate of about 30 seconds per step. Based on throughput of other individuals, this was estimated to be ~15x slower than expected. My network was monitored using nmon and found that it was pretty steady at 12.5K KB/s which also appeared to be slower than others were seeing. Given that this wasn't changing, I considered it may be a function of the data center. So after training for 14 hours and only getting through 1700 steps (and spending 200 credit dollars), I decided to spin up another pair in the Dallas12 data center. I basically hit the same issue in that my GPUs were maxed out at 100% and my network traffic was maxing out less then **12,500 KB/s**. So I killed by Dallas servers and let the London servers keep plugging away. Something still didn't seem right. That's when I realized I had not increased the maximum port speed from 100 Mbps to 1000Mbps. I made this change, and it finally resulted in a 17x increase in step throughput.



1. **How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)**
- As noted above, I learned some lessons along the way, so it took me longer than most. However, with the final setup it took just under 24 hours to train the follow 50K steps at a rate of about 1.7 seconds per step.

2. **Do you think your model is fully trained? How can you tell?**
- No, the validation loss is still falling so additional benefits could be had with further training.
3. **Were you overfitting?**
Not really. Training loss and evaluation loss were both decreasing throughout training and the BLEU score was still slowly increasing after 50K steps.
![My Losses](/hw9/images/loss.png)
4. **Were your GPUs fully utilized?**
- Yes, they were running at 100%. I monitored them using nvidia-smi.  
5. **Did you monitor network traffic (hint: apt install nmon )? Was network the bottleneck?**
- Yes, see the summary discussion. I did not upgrade the port speed from the default of 100Mbps to 1000Mbps. The net effect of this was not a 10x slowdown, but a 17x slowdown (30 seconds per step vs 1.7 seconds per step). So clearly the network is the bottleneck.  
6. **Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?**
- The learning rate uses the transformer policy which is mathematically described [on NVIDIA's website](https://nvidia.github.io/OpenSeq2Seq/html/_modules/optimizers/lr_policies.html). The policy takes an input learning rate, dimensionality, and number of warm-up steps. These parameters are all part of the config file. If you look at the mathematical equation, you will see the learning rate linearly ramps until the end of the warm-up rate. At that point it decays as the inverse square-root of the number of steps.
![My Learning Rate](/hw9/images/learning_rate.png)

7. **How big was your training set (mb)? How many training lines did it contain?**
- The English training set is 593MB, and contains more than 4.5 million sentences. Obviously since this is a translation problem there are the same number of German sentences meaning we are really training on over 1 GB of data.
8. **What are the files that a TF checkpoint is comprised of?**
- *index file* - This file has a list of all of the checkpoints that were created. Typically when restoring a checkpoint, it will try to load the latest checkpoint from the index file. 
- *meta file* - This file contains the graph structure of your TensorFlow model. Basically this is the connections of all the nodes and edges that represent your various operations and transformations. 
- *Data file* - this file actually has the weights for all of your nodes in it. 
9. **How big is your resulting model checkpoint (mb)?**
- The data file is about 813 MB, and the meta file is about 16 MB. The index file is obviously tiny. So in total there is about 830MB of data for the checkpoint.
10. **Remember the definition of a "step". How long did an average step take?**
- 1.8 seconds per step for the final model with the upgraded port speed. 30 seconds per step with the 100 Mbps max port speed.
11. **How does that correlate with the observed network utilization between nodes?**
- As noted in the discussion above, the network was the bottleneck. Increasing the network utilization or network speed will reduce the time per step to a point, until the GPU itself becomes limiting.
