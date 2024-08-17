import statistics as stats

start =  [(0,0), (0,7), (7,0), (7,7)]
finish = [(7,7), (7,0), (0,7), (0,0)]

total_episodes = 100
gamma = 0.8  # discount factor
alpha = 0.7  # learning rate
epsilon = 0.9
decay_rate = 0.1

stats.analysis(start,finish,gamma,alpha,epsilon,total_episodes,decay_rate)
