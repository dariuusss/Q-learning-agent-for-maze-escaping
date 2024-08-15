import labyrinth as maze
import statistics as stats
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

labyrinth = maze.initialise_labyrinth()

start =  [(0,0), (0,7), (7,0), (7,7)]
finish = [(7,7), (7,0), (0,7), (0,0)]

total_episodes = 100
gamma = 0.9  # discount factor
alpha = 0.8  # learning rate
epsilon = 0.9
decay_rate = 0.26

#stats.analysis(labyrinth,start,finish,gamma,alpha,epsilon,total_episodes,decay_rate)
