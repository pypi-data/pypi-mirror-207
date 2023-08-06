from qwertyenv.collect_coins_pz import CollectCoinsEnv
from qwertyenv.pz_to_gymnasium_wrappers import PZ2GymnasiumWrapper
from qwertyenv.ensure_valid_action_pz import EnsureValidAction
# import gym
import qwertyenv
import numpy as np

import torch

import tianshou
from tianshou.data import Collector
from tianshou.env import DummyVectorEnv


action = None

# env =  gym.make('qwertyenv/CollectCoins-v0', pieces=['rock', 'rock'])

pz_env = CollectCoinsEnv(pieces=['rock', 'rock'], with_mask=True)

def another_action_taken(action_taken):
    global action
    action = action_taken

# Wrapping the original environment as to make sure a valid action will be taken.
pz_env = EnsureValidAction(
  pz_env,
  pz_env.check_action_valid,
  pz_env.provide_alternative_valid_action,
  another_action_taken
)

def act_player_1(obs):
    return (0, 0)

gym_env = PZ2GymnasiumWrapper(pz_env, act_others={'player_1': act_player_1})

policy = tianshou.policy.RandomPolicy()

def play(num_episodes: int = 1):

  seed = 1
    
  # ======== environment setup =========
  train_envs = DummyVectorEnv([lambda: gym_env])
  test_envs = DummyVectorEnv([lambda: gym_env])
  # seed
  np.random.seed(seed)
  torch.manual_seed(seed)
  train_envs.seed(seed)
  test_envs.seed(seed)
    
  rewards = []

  policy.eval()
  # pdb.set_trace()
  test_collector = Collector(policy, test_envs, exploration_noise=False)



  result = test_collector.collect(n_step=100000, render=False) # n_episode=num_episodes,
    
  print(result)
  rewards.extend(result['rews'])    

  print(np.mean(rewards))


if __name__ == "__main__":
   play(1)
