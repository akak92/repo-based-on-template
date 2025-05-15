import os
import sys
from flake8.main import application

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)

if __name__ == "__main__":
    app = application.Application()
    app.run([PROJECT_ROOT])
    sys.exit(app.result_count)
