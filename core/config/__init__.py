import os

env = os.getenv("PYTHON_ENV", "dev")
if env == "production":
    from .prod import *
elif env == "test":
    from .test import *
else:
    from .dev import *


config: AppConfig = AppConfig()
forecast_args: ForecastArgs = ForecastArgs()
