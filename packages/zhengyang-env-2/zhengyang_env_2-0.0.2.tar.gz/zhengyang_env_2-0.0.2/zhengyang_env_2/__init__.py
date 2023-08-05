from gym.envs.registration import register

register(
    id='zyw-v2',
    entry_point='zhengyang_env_2.envs:ZhengyangEnv2',
)