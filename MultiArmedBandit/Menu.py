from colorama import Fore, Style, Back
from BanditEnv import BanditEnv


class Menu:

    def __init__(self, bandit_env: BanditEnv = None, algo_picked: int = -1):
        self.author: dict = {"name": "Nikos Pappas", "am": "2114046"}
        self.data_picked: int = -1
        self.data: dict = {"payout": list, "reward": list, "n_episode": int}
        self.algo_picked: int = algo_picked
        self.bandit_env = bandit_env

        # self.create_env()

    def setup(self) -> None:
        self.greeting_msg()
        self.pick_data()
        self.pick_algo()

    def create_env(self) -> BanditEnv:
        if self.bandit_env is None:
            return BanditEnv(self.data["payout"], self.data["reward"], self.data["n_episode"])
        else:
            return self.bandit_env

    def pick_algo(self):
        print(f"{Fore.RED}NOTE:{Fore.RESET} If you picked the example data give it a while to run "
              f"its set to episodes {Fore.RED}100000{Fore.RESET}")
        print(f"{Fore.CYAN}1.{Fore.RESET} Execute with {Fore.GREEN}epsilon-greedy{Fore.RESET}.")
        print(f"{Fore.CYAN}2.{Fore.RESET} Execute with {Fore.GREEN}soft-max{Fore.RESET}.")
        self.algo_picked = int(input())

    def pick_data(self):
        tmp = ''
        while 1:
            self.data_picked = int(input(f"\n{tmp}\n{Fore.CYAN}1.{Fore.RESET} Load example data.\n"
                                         f"\t{Fore.MAGENTA}probabilities = [0.2 , 0.32, 0.25]{Fore.RESET}\n"
                                         f"\t{Fore.YELLOW}reward = [8, 5, 7]{Fore.RESET}\n"
                                         f"\t{Fore.BLUE}n-episodes = 100.000{Fore.RESET}\n"
                                         f"{Fore.CYAN}2.{Fore.RESET} Add your own data.\n\n"))
            tmp = f"{Fore.RED}Pick either 1 or 2.{Fore.RESET}"
            if self.data_picked == 1 or self.data_picked == 2:
                break

        if self.data_picked == 1:
            self.data = {"payout": [0.2, 0.32, 0.25], "reward": [8, 5, 7], "n_episode": 100000}
        elif self.data_picked == 2:
            n_machines: int = int(input(f"{Fore.CYAN}Add number of machines: {Fore.RESET}\n"))
            n_arms: int = int(input(f"{Fore.CYAN}Add number of arms: {Fore.RESET}\n"))
            n_episodes: int = int(input(f"{Fore.CYAN}Number of episodes: {Fore.RESET}\n"))

            payout_prob = [0. for _ in range(n_arms * n_machines)]
            reward = [0 for _ in range(n_arms * n_machines)]

            arm = 0
            for i in range(n_machines * n_arms):
                print(f"{Back.MAGENTA}Machine{Back.RESET}[{Fore.GREEN}{i // n_arms}{Fore.RESET}]")

                payout_prob[i] = float(
                    input(f"{Fore.BLUE}Payout probability{Fore.RESET} for arm[{Fore.GREEN}{arm}{Fore.RESET}]: "))
                while payout_prob[i] <= 0 or payout_prob[i] >= 1:
                    if payout_prob[i] <= 0 or payout_prob[i] >= 1:
                        print(f"{Fore.RED}Please enter a number between (0 - 1){Fore.RESET}")
                    payout_prob[i] = float(
                        input(f"{Fore.BLUE}Payout probability{Fore.RESET} for arm[{Fore.GREEN}{arm}{Fore.RESET}]: "))
                reward[i] = int(input(f"{Fore.BLUE}Reward{Fore.RESET} for arm[{Fore.GREEN}{arm}{Fore.RESET}]: "))
                if arm % n_arms == 0 and arm != 0:
                    arm = 0
                else:
                    arm += 1

            self.data["payout"] = payout_prob
            self.data["reward"] = reward
            self.data["n_episodes"] = n_episodes

    def greeting_msg(self):
        print(f"{Back.MAGENTA}Multi-armed Bandit problem{Back.RESET} \n"
              f"{Fore.YELLOW}Author{Fore.RESET}: {Fore.GREEN}{self.author['name']}{Fore.RESET} \n"
              f"{Fore.YELLOW}AM{Fore.RESET}: {Fore.GREEN}{self.author['am']}{Fore.RESET}")
