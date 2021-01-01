# gym-envs
Custom environments for OpenAI gym. In order to use these environment, you must first install them.  
After installation, test files might be a good starting point for obtaining understanding how to use these environements.  
The critical interface information about environments is also explained below, but only very briefly.
## Installation
When in repository root folder, environments can be installed with following command: `$ pip install -e <env-name>/<env-name>/`  
Environment is fully defined in the latter directory, but tests and such require additional nesting in order to not clutter root of this repository.  
It is recommended to use virtual environment when installing these custom gym environments.

## Environments
### Pulsegen
Pulsegen can be used to generate sequential data.
Data generation logic is based on Fourier series, which allows to configure and generate various repeatitive patterns with ease.
Signal shape can be adjusted modifying configuration file parameters. Interface is given as
```
# Create environment:
env = gym.make("FourierSeries-v0", config_path="config.py")

# Collect data:
data = recordRotations(rotations=1, viz=False)
```
Argument `config_path` is optional. If it is not given, then default configurations are used.
Also `Viz` is optional. Recorded data can be visualized, but this requires `matplotlib`.

Data is three dimensional vector: [batch-num, signal, length]
`recordRotations` collects a batch of data, which matches with specified repetitions. Two signals are currecntly recorded.
First one is the data and second one is linearly increassing number. Length is the number of samples.

## Testing
Tests are written using [pytest](https://docs.pytest.org/en/stable/index.html) framework.
After installing the framework, all tests cases can be run with: `$ pytest`. Single module can be run with:
`$ pytest -q <test_filename.py>`
