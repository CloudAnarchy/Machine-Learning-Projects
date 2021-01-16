import torch
from BanditEnv import BanditEnv

"""
    torch.exp : Returns a new tensor with the exponential of the elements of the input tensor input.
    y = e^x
    torch.sum : Idio me to sum()
    https://pytorch.org/docs/stable/generated/torch.exp.html?highlight=exp#torch.exp
"""


def gen_softmax_exploration_policy(t):
    def policy_function(q):
        probs = torch.exp(q / t)
        probs = probs / torch.sum(probs)
        action = torch.multinomial(probs, 1).item()
        return action
    return policy_function


def softmax(be: BanditEnv):
    t = 0.1
    softmax_exploration_policy = gen_softmax_exploration_policy(t)
    q = torch.zeros(be.n_action)

    for episode in range(be.n_episode):
        action = softmax_exploration_policy(q)
        be.new_action_made(action, q)
