import dotenv
import os

dotenv.load_dotenv(".env")
envs = {}


for var in ["SENTRY_URL"]:
    envs[var] = os.getenv(var)
