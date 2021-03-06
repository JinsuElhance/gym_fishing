import gym
from gym import spaces
from gym_fishing.envs.abstract_fishing_env import AbstractFishingEnv

class FishingEnv(AbstractFishingEnv):
    def __init__(self,
                 r = 0.3, 
                 K = 1, 
                 sigma = 0.01,
                 n_actions = 100,
                 init_state = 0.75,
                 Tmax = 100,
                 file = None):
        super().__init__(params = {"r": r, "K": K, "sigma": sigma},
                         init_state = init_state,
                         Tmax = Tmax,
                         file = file)
        # override to use discrete actions
        self.n_actions = n_actions
        self.action_space = spaces.Discrete(n_actions)

