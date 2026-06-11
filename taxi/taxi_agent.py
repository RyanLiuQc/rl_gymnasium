import gymnasium as gym

# note on observation:
# observation = ((taxi_row * 5 + taxi_col) * 5 + passenger_location) * 4 + destination
'''
intuition:
5x5 grid -> total 25 position for taxi. 
since there is 5 passenger_location possible, shift taxi position by x5 so that 
(taxi_row * 5 + taxi_col) // 5 == position value
(taxi_row * 5 + taxi_col)%5 == passenger_location

DECODING: Using modular arithmetics, role back 
taxiPosition_and_passengerLocaation = obs // 4
-> destination = obs % 4
similarly, taxiPosition = taxiPosition_and_passengerLocaation // 5
-> passenger_location = taxiPosition_and_passengerLocaation % 5
...
-> taxi_row = taxiPosition // 5
-> taxi_col = taxiPosition % 5
'''

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

        # track progress. for graphing
        self.training_error = []

    def get_action(self, obs: tuple[]):
        '''
        DECODING of observation: Using modular arithmetics, role back 
        taxiPosition_and_passengerLocaation = obs // 4
        -> destination = obs % 4
        similarly, taxiPosition = taxiPosition_and_passengerLocaation // 5
        -> passenger_location = taxiPosition_and_passengerLocaation % 5
        -> taxi_row = taxiPosition // 5
        -> taxi_col = taxiPosition % 5
        '''
        # TODO: complete signature and write the function.
        pass 
