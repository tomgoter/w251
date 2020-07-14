# W251 - Summer 2020
## Homework 11 - Deep Reinforcement Learning with ATARI Lunar Lander
## Tom Goter

### Overview
This week we were asked to modify a Python script which applies a Q-learning methodology to implement deep reinforcement learning in order to master the ATARI Lunar Lander game. The goal of the Lunar Lander game is to safely land your Lunar Lander in a goal zone. You do this by taking a series of actions. The actions consist of firing your thrusters either down, to the left or to the right. Thus, these actions propel you up, right, or left, respectively. We apply a Q-learning methodology to automatically play and hopefully win this game. In Q-learning we basically approach the game is a greedy manner. We evaluate our state and always take the action that maximizes our reward. Unfortunately we do not know the reward for a given state and action a priori. Thus, we must learn. The learning in this process uses a relatively simply two-layer neural network. We are trying to learn for a given state how to maximize our reward. A series of sensitivities studies were performed for this homework in order to determine an effective means to maximize our score in as few episodes (game play-throughs) as possible.

### Videos
Links to video from final model: 

You should save three videos showing your first, last, and an intermediary run of the training. Also save a couple videos from the testing process that runs at the end of the training.


### Questions
1. **What parameters did you change?**. 
- I performed a series of perturbation studies to slowly converge on a model that would result in achieving the goal of an average reward of 200. The results of my studies are discussed below and shown in the figures.
- The baseline model trained slowly. It is represented by the black dots. One can see that after 400 episodes, the average reward had plateaued at about 30. That is not to say that the model may not have continued improving, but the slow accumulation of skill indicated that performance could be improved.
- The next model looked at doubling the hidden units in both the first and second layer. This is represented by the blue series. This model plateaued around an average reward of zero between 300 and 400 training episodes. Based on the observation of how the baseline model trained, this plateau may have correlate to the first plateau seen in the baseline training between episodes 200-300. This plateau seems to occur when the lander decides it is advantageous to slow down. This observation seems to make the lander tend to hover for a while instead of learning it really needs to land to get big points.
- The second sensitivity (gray series) is the same as the previous but with double the batch size and a lower exploration factor (epsilon). The increased batch size should get the model to learn longer-range dependencies. The change to the epsilon value was to start getting the model to start making moves it knows to have high value sooner (as opposed to randomly exploring moves). I speculated that this might lead to quicker training. In the end this model achieved the highest average reward, but still only got to about 120 after 500 episodes.
- The third sensitivity included another doubling of the hidden units in both layers (i.e., 64 and 32 in layers 1 and 2, respectively). The epsilon decay factor was retained at 0.98. This model training quickly, achieving an average score of 200 after only 350 iterations. The problem was that during testing the average score was only about 196. What happened is that in some episodes during training, the lunar lander encountered situations it did not know how to handle. Thus, it appears the exploitation factor was too high, and more exploration was needed.
- The final sensitivity was simply to increase the epsilon decay factor from 0.98 to 0.99 (red series). This one small change had a large effect. First, on training, the model initially trained more quickly than the previous model; however, around episode 250 the training slowed down as additional exploration was taking place. This slower ramp toward an average training score of 200 allowed the model to better learn differnt environments and how to react. And the proof is in the fact that the average of the test iterations was 243 (vice the 196 of the previous model). We show in the second figure (showing score per iteration, not average score) below that the main cause for increase is the elimination of the landing failures that we saw with the previous model. Again this is attributed to a better coverage of the overall environment space caused by increased exploration and additional training steps (thus more environments).

![Model Comparison](/hw11/img/avg_score.png)
![Test Comparison](/hw11/img/test_scores.png)


2. **What values did you try?** 
- See above. All sensitivies and their effects discussed there.
3. **Did you try any other changes that made things better or worse?**
- See above. All sensitivies and their effects discussed there.
4. **Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?**
- See the second figure above. The final model nearly achieved this goal, but had two episodes with scores less than 200.
5. **Based on what you observed, what conclusions can you draw about the different parameters and their values?**
- Some discussion above. In general the increased hidden units are important to allow us to better capture all the different possible state/environment combinations. The increased batch size let's us learn from additional state/environment pairs at once, so it should decrease training time. The epsilon decay factor does control how quickly we transition from exploring to exploiting, but the tradeoff may come with generalization.
6. **What is the purpose of the epsilon value?**
- This factor controls the propensity of your model to try a random action as opposed to take the action that currently as the highest Q-value associated with it. So in the beginning epsilon is started at 1.0. Which means 100% random action to allow the model to learn. The rate at which you decrease epsilon as you train is controlled by the epsilon decay factor, and as discussed above this controls how quickly your model learns versus how completely your model learns. This is typically referred to as exploitation (pick action associated with highest q-value) vs exploration (try random stuff to better learn the actual q-values associated with different state/env combinations).
7. **Describe "Q-Learning".**
- In Q-learning we try to learn for every environment state, the cumulative value (in our case episode reward) associated with a given action. We do this by essentially learning how each action contributes to the final score through a period of learning. We approximate the Q-function with our two-layer neural net in our homework. This neural net takes as input state and action and predicts the cumulative score. As we train we refine this prediction such that we are continually (hopefully) taking actions that are more likely to result in a higher overall end reward. There are subtleties in q-learning such as the discount factor that gives you more reward for near term benefits vs benefits projected many actions away (think of it as time-value of money - 10 dollars now is better than 10 dollars 10 years from now - hopefully).
