# gym-envs
Custom environments for OpenAI gym. In order to use these environment, you must first install them.
After installation, test files might be a good starting point for understanding how to use these environements.
The critical information about environment interface is also explained below, but only very briefly.
## Installation
Environments can be installed with following command: `$ pip install -e <env-name>/`  
It is recommended to use virtual environment when installing these custom gym environments.

## Environments
### pulsegen
Pulsegen can be used to generate sequential data.
Data generation logic is based on Fourier series, which allows to configure and generate various repeatitive patterns with ease.
Signal shape can be adjusted modifying configuration file parameters. Default configuration file is provided with the environemnt,
but user can also create a new configuration file to same directory as from where the environment is imported. Data can be collected
with following function call: `recordRotations(rotations=1, viz=False)`. It is possible to repeat the pattern when recording. Recorded
data can be also visualized with matplotlib.
## Testing
Tests are written using [pytest](https://docs.pytest.org/en/stable/index.html) framework.
After installing the framework, tests cane be run with:  
`$ pytest -q <test_filename.py>`
