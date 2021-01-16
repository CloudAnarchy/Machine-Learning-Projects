import torch
from Menu import Menu
from epsilon_greedy import epsilon_method
from soft_max import softmax
from BanditEnv import *

# For quick setup use this:
# bandit_env = BanditEnv(payout=[0.3, 0.6, 0.1],
#                        reward=[5, 2, 9],
#                        n_episode=10000)
# menu = Menu(bandit_env, algo_picked=2)
####################################################

# Otherwise use this:
menu = Menu()
menu.setup()
####################################################


bandit_env = menu.create_env()
if menu.algo_picked == 1:
    BanditEnv.solve(bandit_env, epsilon_method)
elif menu.algo_picked == 2:
    BanditEnv.solve(bandit_env, softmax)

visualize(bandit_env.n_action, bandit_env.action_avg_reward)
