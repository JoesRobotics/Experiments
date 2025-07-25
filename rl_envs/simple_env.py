import gym
import numpy as np

class SimpleEnv(gym.Env):
    """A minimal environment for demonstration purposes."""

    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super().__init__()
        self.action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(1,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(1,), dtype=np.float32)
        self.state = np.zeros(1, dtype=np.float32)

    def step(self, action):
        self.state += action
        reward = -np.linalg.norm(self.state)
        done = bool(np.abs(self.state[0]) > 10.0)
        return self.state.copy(), reward, done, {}

    def reset(self):
        self.state.fill(0.0)
        return self.state.copy()

    def render(self, mode="human"):
        print(f"State: {self.state[0]:.2f}")

if __name__ == "__main__":
    env = SimpleEnv()
    obs = env.reset()
    for _ in range(5):
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        print("obs", obs, "reward", reward)
        if done:
            break
