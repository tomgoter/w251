# W251 - Summer 2020
## Homework 9
## Tom Goter

For this homework, I provisioned two P100 devices using the docker image from Week 2 which already included the 2TB SAN disk and Docker. Both of these P100 machines were provisioned from the WDC07 cluster. Unfortunately, V100s were unavailable at the time of doing the homework :(. I already had an NVIDIA account, but I did go through the process of getting a new NVIDIA API key, and logged in with it on one of my P100 devices. I then pulled a new tensor pulled new tensorflow image, cloned v2, and built an image for the openseq2seq model with:
`docker build -t openseq2seg -f Dockerfile .` 
The docker image was then also created on my secondary device. The next step was to create two docker containers, one on each device using the following command:
`docker run --runtime=nvidia -d --name openseq2seq --net=host -e SSH_PORT=4444 -v /data:/data -p 6006:6006 opense2seg:v1`




1. How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
- I went through a series of evolutions on training. I used a pair of V100s in London04; however, these were only training at a rate of about 30 seconds per step. Based on throughput of other individuals, this was estimated to be ~15x slower than expected. My network was monitored using nmon and found that it was pretty steady at 12.5K KB/s which also appeared to be slower than others were seeing. Given that this wasn't changing, I considered it may be a function of the data center. So after training for 14 hours and only getting through 1700 steps (and spending 200 credit dollars), I decided to spin up another pair in the Dallas12 data center. I basically hit the same issue in that my GPUs were maxed out at 100% and my network traffic was maxing out less then 13000 KB/s. So I killed by Dallas servers and let the London servers keep plugging away.

**Update** I realized I am an idiot. I was starting from the Week 2 Image we created, but that had a 100 Mbps rate limit on the port (if you convert 100Mbits to KB you get 12,500 KB). So that means I wasted a few hundred dollars. But on the bright side you are able to upgrade your session while it's running. I did a quick reboot and started over one last time and voila we are finally training at 1.8seconds per step. 



2. Do you think your model is fully trained? How can you tell?
3. Were you overfitting?
4. Were your GPUs fully utilized?
**5. Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?**
Yes, see the summary discussion. I did not upgrade the port speed from the default of 100Mbps to 1000Mbps. The net effect of this was not a 10x slowdown, but a 15x slowdown (30 seconds per step vs 1.8 seconds per step). So clearly the network is the bottleneck.
6. Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?
7. How big was your training set (mb)? How many training lines did it contain?
8. What are the files that a TF checkpoint is comprised of?
9. How big is your resulting model checkpoint (mb)?
10. Remember the definition of a "step". How long did an average step take?
1.8 seconds per step for the final model with the upgraded port speed. 30 seconds per step with the 100 Mbps max port speed.
11. How does that correlate with the observed network utilization between nodes?
As noted in the discussion above, the network was the bottleneck. Increasing 
