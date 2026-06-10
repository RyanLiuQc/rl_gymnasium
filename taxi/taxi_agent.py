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
        self.env = env

        # a dictionay is a bit better for finding q_values because it does not required precise shape of matrices
        self.q_values = defaultdict(lambda: np.zeros(env.action_space.n)) # type: ignore
        
        self.lr = lr
        self.init_epsilon = init_epsilon
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon
        self.discount_factor = discount_factor
