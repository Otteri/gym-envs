###################
# Data generation #
###################
signal_length = 1000      # Signal length (starts from zero)
step_size = 6.2832 / 1000 # Sample step. (2PI / L, for one cycle).
repetitions = 10          # How many times pattern is repeated during single period
datafile = "traindata"    # Where generated data is saved

harmonics = {             # Signal shape.
    1 : 5.5,
    2 : 1.3,
    6 : 4.0
}

noise = 0.04              # Makes the signal jagged. 0.01 = 1% error.

###################
#    Plotting     #
###################
color = 'b'
dpi = 100
