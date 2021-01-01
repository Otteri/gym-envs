import gym
import pulsegen
import pytest

# Only basic checks in this file.

@pytest.fixture()
def env():
    yield gym.make("FourierSeries-v0")

class TestDefaultConfig:
    def test_collects_data(self, env):
        data = env.recordRotations(rotations=1)
        assert data.all() != None
        assert data.ndim == 3

    def test_does_multiple_rotations(self, env):
        data1 = env.recordRotations(rotations=1)
        data2 = env.recordRotations(rotations=2)
        assert len(data2) > len(data1)

    def test_data_length_is_correct(self, env):
        data = env.recordRotations(rotations=1)
        assert data.shape[2] == 500

    def test_batch_size_is_correct(self, env):
        data = env.recordRotations(rotations=5)
        assert data.shape[0] == 5

    def test_data_values_change(self, env):
        data = env.recordRotations(rotations=1)
        assert data[0, 0, 0] != data[0, 0, 1]
