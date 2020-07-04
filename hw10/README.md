# W251 - Summer 2020
## Homework 10 - Deep Reinforcement Learning
## Tom Goter

### Documentation of Cart Pole Environment
This week we are going through a tutorial and demonstration of reinforcement learning using the simple cart pole environment which is distributed from OpenAI Gym. In this environment there is a free-swinging pole attached to a cart. The cart can either move left or right and the overall objective is to keep the pole pointed up, normal to the cart. The environment itself is written in Python but converted to TensorFlow using the TFPyEnvironment. See image below for a diagram of the simple environment. ![Cart Pole Environment from OpenAI Gym](/hw10/images/cart.png)

### Actions
Within the environment one can take "action". In this case the action is left or right movement of the cart. The environment then returns the next observation of the environment (following the action) including the reward the agent received from taking the action. Within the cart pole environment, a left-movement action is indicated by the integer 0 and a right-movement is indicated by the integer 1.

### Agent
An agent is really the algorithm that is used to interact with the environment, take actions and hopefully succeed by maximizing the rewards. There are many different forms of agents, but in our case we use the DQN Agent. The DQN Agent uses a neural net under the hood and is basially trained to predict expected returns for taking either action given the current environment condition. Our underlying neural network had a fully connected layer with 100 nodes. As with any neural network, this DQN agent requires a gradient descent optimizer (Adam is used), a loss function (element_wise_squared_loss) and a training step counter. After the agent is instantiated with these bits of information, it can be initialized.

### Policies
The policy of an agent is essentially its action it will take once its trained. I am thinking about this as the actual final output of the underlying neural network. There are actually two policies used - one for evaluation and one for data collection. To generate an action from a policy, you just feed it the timesetp of an environment. In the HW it is also noted that you can have simple random action policies as well. 

### Metrics and Evalution
In order to evalute how well our policy (actions given an environment state) are working we need a metric. This is typically the averaged reward we observed after letting our agent/policy play out over several independent evaluations. During evaluation we typically use our policy for a fixed number of steps and record a set of trajectories in a replay buffer. This buffer is then used for traning of the agent. 

### Training
We actually trained our own agent in the HW. We ran 20,000 steps during our training. Our average return started out at about 11 and increased to about 200 by the end of the training. We recorded our returns as we trained and also generated a simple lineplot using pyplot. 
![Returns During Agent Training](/hw10/images/returns.png)
One cool thing is that we can also simply render the environment for each timestep (shows us a picture of the cart and pole position). With this we can generate (and did generate) a short movie of how our trained agent performs. ![Rendering of Interaction with Our Enviroment](/hw10/images/env_movie.png)
