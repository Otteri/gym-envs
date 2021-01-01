import gym
import pulsegen
import pytest

# This file basically repeates test_pulsegen_default_cfg.py,
# but test values are different to increase coverage.
# Also try to focus negative and more tricky cases here,

@pytest.fixture()
def env():
    yield gym.make("FourierSeries-v0", config_path="config.py")

class TestCustomConfig:
    def test_collects_data(self, env):
        data = env.recordRotations(rotations=1, viz=False)
        assert data.all() != None
        assert data.ndim == 3

    def test_does_multiple_rotations(self, env):
        data1 = env.recordRotations(rotations=1, viz=False)
        data2 = env.recordRotations(rotations=2, viz=False)
        assert len(data2) > len(data1)

    def test_data_length_is_correct(self, env):
        data = env.recordRotations(rotations=1)
        assert data.shape[2] == 1000

    def test_batch_size_is_correct(self, env):
        with pytest.raises(ValueError):
            data = env.recordRotations(rotations=-1)

    def test_data_values_change(self, env):
        data = env.recordRotations(rotations=1)
        assert data[0, 0, 0] != data[0, 0, 1]
