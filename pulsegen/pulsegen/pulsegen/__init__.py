from gym.envs.registration import register

register(
    id='PeriodicalSignal-v0',
    entry_point='pulsegen.envs:PeriodicalSignal',
)

register(
    id='PeriodicalSignalWithAngle-v0',
    entry_point='pulsegen.envs:PeriodicalSignalWithAngle',
)

register(
    id='PeriodicalSignalWithTime-v0',
    entry_point='pulsegen.envs:PeriodicalSignalWithTime',
)
