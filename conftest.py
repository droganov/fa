import os
import sys

os.environ["ENV_FILE"] = ".env.test"

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
