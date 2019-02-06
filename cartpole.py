import gym
# env = gym.make('CartPole-v0')
# env = gym.make('MountainCar-v0')
# env = gym.make('MsPacman-v0') #req atari dependency
# env = gym.make('Hopper-v2')
# for i_episode in range(20):
#     observation = env.reset()
# # env.reset()
# 	for _ in range(1000):
# 	   	env.render()	
# 	   	env.step(env.action_space.sample()) # take a random action
	



# import gym
# env = gym.make('CartPole-v0')
for i_episode in range(2000):
    observation = env.reset()
    for t in range(1000):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break