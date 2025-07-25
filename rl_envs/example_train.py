"""Example script that runs random policy on the SimpleEnv."""
from simple_env import SimpleEnv
import numpy as np


def run_episode(env: SimpleEnv, steps: int = 20):
    obs = env.reset()
    total_reward = 0.0
    for _ in range(steps):
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break
    return total_reward


if __name__ == "__main__":
    env = SimpleEnv()
    reward = run_episode(env)
    print(f"Episode reward: {reward}")
