from gym.envs.registration import register

register(
    id='zyw-v3',
    entry_point='zhengyang_env_3.envs:ZhengyangEnv3',
)