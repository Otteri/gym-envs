###################
# Data generation #
###################
signal_length = 500       # Signal length (starts from zero)
step_size = 6.2832 / 500  # Sample step. (2PI / L, for one cycle).
repetitions = 15          # How many times pattern is repeated during single period
noise = 0.00              # Makes the signal jagged. 0.01 = 1% error.
datafile = "traindata"    # Where generated data is saved

harmonics = {             # Signal shape.
    1 : 5.0,
}

###################
#    Plotting     #
###################
color = 'b'
dpi = 100
