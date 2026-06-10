import gymnasium as gym

if __name__ == "__main__":
    env = gym.make("Taxi-v4", render_mode="human")
    env.reset()

    episode_over = False
    total_reward = 0
    while not episode_over:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)

        # print(reward)
        total_reward += reward # pyright: ignore[reportOperatorIssue]
        episode_over = terminated or truncated

        

