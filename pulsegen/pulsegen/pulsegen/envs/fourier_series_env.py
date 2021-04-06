import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from gym import Env

class FourierSeries(Env):
    def __init__(self, config_path=None) -> None:
        """
        Signal properties are set here. Uses values from the default
        config file, if no separate config path is provided.
        """
        if config_path:
            import sys
            print("[INFO] Loading config:", config_path)
            sys.path.append(config_path)
            import config
        else:
            from . import default_config as config

        self.data_length = config.signal_length
        self.step_size = config.step_size
        self.harmonics = config.harmonics
        self.noise = config.noise

    def _get_sample(self, angle):
        """
        Gives a single point value. Increment angle and call
        this function reteatedly to record full signal.

        Args:
            angle (float): Angle in radians [0 2PI]

        Returns:
            sample value
        """
        value = 0.0
        for harmonic_n in self.harmonics:
            magnitue = self.harmonics[harmonic_n]
            value += magnitue * np.cos(harmonic_n * angle)
        return value

    def _record_rotation(self, viz=False) -> (np.array, np.array):
        """
        This is the core function for this module. Increments angle from
        zero to 2PI using the step size and collects samples during operation.

        Args:
            Viz (bool): Should the generated signal be visualized?

        Returns:
            (angle, signal): Generated data arrays
        """
        signal_data = np.empty(self.data_length, 'float64')
        angle_data = np.empty(self.data_length, 'float64')
        current_sample_num = 0

        # Does approximately one full rotation
        # Due to noise and discrete step size, may not be precisely one rotation
        angle = np.random.uniform(0, 2*np.pi) # Start from random angle
        while(current_sample_num < self.data_length):
            angle_data[current_sample_num] = angle
            signal_data[current_sample_num] = self._get_sample(angle)

            noise = np.random.uniform(-self.noise, self.noise) # simulate noise (%)
            angle += self.step_size + noise
            current_sample_num += 1

            # Make angle to stay within limits [0, PI2]
            angle = 0 if angle > 2*np.pi else angle

        # Visualize sample if user wants to see it
        if viz: 
            self._plot_recorded_data(signal_data, angle_data)

        return angle_data, signal_data 

    def _plot_recorded_data(self, y1, y2):
        """
        A helper function for visualizing data
        y1 (np.array): signal
        y2 (np.array): angle
        """
        fig, (ax1, ax2) = plt.subplots(2, 1)
        ax1.title.set_text('Signal values')
        ax2.title.set_text('Angle [rad]')
        fig.tight_layout()

        x = np.arange(y1.shape[0])
        ax1.plot(x, y1, color='r', linewidth=2.0)
        ax2.plot(x, y2, color='b', linewidth=2.0)
        plt.show(block=True)

# ---------------------------------------------------------------------
# User interfaces:

class PeriodicalSignal(FourierSeries):
    def record_rotation(self, viz=False) -> np.array:
        _, signal = self._record_rotation(viz)
        return signal

class PeriodicalSignalWithAngle(FourierSeries):
    def record_rotation(self, viz=False) -> (np.array, np.array):
        angle, signal = self._record_rotation(viz)
        return signal, angle

class PeriodicalSignalWithTime(FourierSeries):
    def __init__(self, hz=1.0, config_path=None) -> None:
        """
        Uses parent constructor, but takes in an additional parameter.
        The additional hz parameter is used for deriving time from angle
        values.

        Args:
            hz (float): rotation frequency.
        """
        FourierSeries.__init__(self, config_path)
        self.hz = hz

    def record_rotation(self, viz=False) -> (np.array, np.array):
        angle, signal = self._record_rotation(viz)
        time_data = (1.0 / self.hz) * angle
        return signal, time_data
