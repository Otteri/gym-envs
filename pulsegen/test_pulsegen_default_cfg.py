import gym
import pulsegen
import pytest

# Only basic checks in this file.

@pytest.fixture()
def env():
    yield gym.make("PeriodicalSignalWithAngle-v0")

class TestDefaultConfig:
    def test_collects_data(self, env):
        angle_data, signal_data = env.record_rotation(viz=False)
        assert angle_data.all() != None
        assert signal_data.all() != None

    def test_data_length_is_correct(self, env):
        angle_data, signal_data = env.record_rotation()
        assert len(angle_data) == 500
        assert len(signal_data) == 500

    def test_data_values_are_different(self, env):
        angle_data, signal_data = env.record_rotation(viz=False)
        assert angle_data[0] != angle_data[1]
        assert signal_data[0] != signal_data[1]
