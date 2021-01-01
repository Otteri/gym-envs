import numpy as np
import gym
import pulsegen
import pytest

@pytest.fixture()
def env():
    yield gym.make("FourierSeries-v0")

class TestDefaultConfig:
    def test_collects_data(self, env):
        data = env.recordRotations(rotations=1, viz=False)
        assert data.all() != None

    def test_does_multiple_rotations(self, env):
        data1 = env.recordRotations(rotations=1, viz=False)
        data2 = env.recordRotations(rotations=2, viz=False)
        assert len(data2) > len(data1)
