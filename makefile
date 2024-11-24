d:
	@echo "Starting dev"
	ENV_FILE=.env.local uvicorn app.main:app --reload

f:
	pip freeze > requirements.txt

t:
	ENV_FILE=.env.test python script.py yoyo-up
	ENV_FILE=.env.test python -m pytest

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

# Yoyo
yn:
	@echo "Creating a new migration"
	@read -p "Enter migration name: " name; \
	yoyo new -m "$$name" --sql

yu:
	ENV_FILE=.env.local python script.py yoyo-up

yd:
	ENV_FILE=.env.local python script.py yoyo-down
