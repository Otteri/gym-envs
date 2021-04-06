import gym
import pulsegen
import pytest

# This file basically repeates test_pulsegen_default_cfg.py,
# but test values are different to increase coverage.
# Also try to focus negative and more tricky cases here,

@pytest.fixture()
def env():
    yield gym.make("PeriodicalSignalWithAngle-v0", config_path="config.py")

class TestCustomConfig:
    def test_collects_data(self, env):
        angle_data, signal_data = env.record_rotation(viz=False)
        assert angle_data.all() != None
        assert signal_data.all() != None

    def test_data_length_is_correct(self, env):
        angle_data, signal_data = env.record_rotation()
        assert len(angle_data) == 1000
        assert len(signal_data) == 1000

    def test_data_values_are_different(self, env):
        angle_data, signal_data = env.record_rotation()
        assert angle_data[0] != angle_data[1]
        assert signal_data[0] != signal_data[1]
