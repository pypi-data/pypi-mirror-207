import sentry_sdk
from . import env_loader

sentry_sdk.init(
    dsn=env_loader.envs.get("SENTRY_URL"),

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
