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
- I changed many parameters including hidden units per layer, batch size, epochs, epsilon. Each 


What values did you try?
Did you try any other changes that made things better or worse?
Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?
Based on what you observed, what conclusions can you draw about the different parameters and their values?
What is the purpose of the epsilon value?
Describe "Q-Learning".
