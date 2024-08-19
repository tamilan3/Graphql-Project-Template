from termcolor import colored
from decouple import config
from .base import *


# Load the project variable from the .env file
project = config('PROJECT', default='production')

# Determine which settings to import based on the project variable
if project == 'local':
    print(colored("Running development...", 'green'))
    from .develop import *
elif project == 'develop':
    print(colored("Running development...", 'green'))
    from .develop import *
else:
    print(colored("Running production...", 'green'))
    from .local import *