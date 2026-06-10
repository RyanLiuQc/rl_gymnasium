import gymnasium as gym

class TaxiAgent:
    def __init__(
            self, 
            env: gym.Env,
            lr: float,
            init_epsilon: float,
            epsilon_decay: float,
            final_epsilon: float,
            discount_factor: float # how much we care about future reward compared to current
    ) -> None:
        '''
        Q-learning agent
        '''
        self.env = env,
        

env = gym.make("Taxi-v4", render_mode="human")
observation, info = env.reset()
observation, reward, terminated, truncated, info = env.step(4)
env.render()

print(observation,info)