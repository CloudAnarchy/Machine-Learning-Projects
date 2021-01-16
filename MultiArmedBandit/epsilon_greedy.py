import torch
from BanditEnv import BanditEnv

"""
    torch.ones : Returns a tensor filled with the scalar value 1, with the shape defined by the variable argument size.
    torch.zeros : Same as the above with filled with 0's.
    torch.argmax : Returns the indices of the maximum value of all elements. Similar to max()
    torch.multinomial : Returns a tensor where each row contains num_samples indices sampled from the multinomial 
    probability distribution..
    https://pytorch.org/docs/stable/generated/torch.multinomial.html?highlight=multinomial#torch.multinomial
"""


# We do this "method" just because everytime we need to change the Q
# and not the number of actions or the epsilon since these stay the same
# for every action anyway.. So its cleaner to return the function and later on
# just change one param.
def gen_epsilon_greedy_policy(n_action: int, epsilon: float):
    def policy_function(q):
        probs = torch.ones(n_action) * epsilon / n_action
        best_action = torch.argmax(q).item()
        probs[best_action] += 1.0 - epsilon
        action = torch.multinomial(probs, 1).item()
        return action
    return policy_function


def epsilon_method(be: BanditEnv):
    epsilon = 0.2
    epsilon_greedy_policy = gen_epsilon_greedy_policy(be.n_action, epsilon)
    q = torch.zeros(be.n_action)
    for episode in range(be.n_episode):
        action = epsilon_greedy_policy(q)
        be.new_action_made(action, q)
