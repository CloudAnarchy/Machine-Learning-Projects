import torch
from random import randint
import matplotlib.pyplot as plt
from typing import List


class BanditEnv:
    MAX_REWARD = 100

    def __init__(self, payout: List, reward: List, n_episode: int):
        self.payout = payout
        self.n_episode = n_episode
        self.reward = reward

        # Setup the actual env
        self.n_action: int = len(self.payout)
        self.action_count = [0 for _ in range(self.n_action)]
        self.action_total_reward = [0 for _ in range(self.n_action)]
        self.action_avg_reward = [list() for _ in range(self.n_action)]

        # def __init__(self, n_arms: int):
    #     self.payout: List = torch.rand(n_arms).tolist()
    #     # I could maybe use "torch.randperm(n)" here but not sure which suits better the case.
    #     self.arm_rewards: List = [randint(0, BanditEnv.MAX_REWARD) for _ in range(n_arms)]

    """
         torch.Tensor: Is a multi-dimensional matrix containing elements of a single data type. Its similar to 
         a NumPy array with the difference that it can utilize GPU as well instead of CPU.

         torch.rand(): Returns a tensor filled with random numbers from a uniform distribution on the interval [0, 1)
         torch.Tensor.item(): Returns the value of this tensor as a standard Python number. Needs one element to work.
         https://pytorch.org/docs/stable/tensors.html?highlight=item#torch.Tensor.item 
         https://pytorch.org/docs/stable/generated/torch.rand.html?highlight=rand#torch.rand

         So in this case "torch.rand(1).item()" just returns a random num between [ 0 , 1 )  
         And the step method executes an action and returns the reward if it pays out.
    """
    def step(self, action) -> float:
        if torch.rand(1).item() < self.payout[action]:
            return self.reward[action]
        return 0

    def new_action_made(self, action, q):
        reward = self.step(action)
        self.action_count[action] += 1
        self.action_total_reward[action] += reward
        q[action] = self.action_total_reward[action] / self.action_count[action]

        # Append the new avg reward. Updating the statistics in other word.
        for i in range(self.n_action):
            if self.action_count[i]:
                self.action_avg_reward[i].append(
                    self.action_total_reward[i] / self.action_count[i]
                )
            else:
                self.action_avg_reward[i].append(0)

    @staticmethod
    def solve(be, algo):
        algo(be)


def visualize(n_action: int, action_avg_reward: List):
    for action in range(n_action):
        plt.plot(action_avg_reward[action])
    plt.legend([f"Arm {action}" for action in range(n_action)])
    plt.title("Average reward over time")
    plt.xscale("log")
    plt.xlabel("Episode")
    plt.ylabel("Average reward")
    plt.show()
