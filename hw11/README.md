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
- I performed a series of perturbation studies to slowly converge on a model that would result in achieving the goal of an average reward of 200. The results of my studies are discussed below and shown in the figure below the discussion.
- The baseline model trained slowly. It is represented by the black dots. One can see that after 400 episodes, the average reward had plateaued at about 30. That is not to say that the model may not have continued improving, but the slow accumulation of skill indicated that performance could be improved.
- The next model looked at doubling the hidden units in both the first and second layer. This is represented by the blue series. This model plateaued around an average reward of zero between 300 and 400 training episodes. Based on the observation of how the baseline model trained, this plateau may have correlate to the first plateau seen in the baseline training between episodes 200-300. This plateau seems to occur when the lander decides it is advantageous to slow down. This observation seems to make the lander tend to hover for a while instead of learning it really needs to land to get big points.
- The third sensitivity is the same as the previous but with double the batch size and a lower exploration factor (epsilon). The increased batch size should get the model to learn longer-range dependencies. The change to the epsilon value was to start getting the model to start making moves it knows to have high value sooner (as opposed to randomly exploring moves). I speculated that this might lead to quicker training. In the eng this model achieved the highest average reward, but still only got to about 120 after 500 episodes.
- 


What values did you try?
Did you try any other changes that made things better or worse?
Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?
Based on what you observed, what conclusions can you draw about the different parameters and their values?
What is the purpose of the epsilon value?
Describe "Q-Learning".
