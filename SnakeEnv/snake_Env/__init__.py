from gym.envs.registration import register

register(
    id='snakeEnv-v0',
    entry_point='snake_Env.envs:SnakeEnv',
)
