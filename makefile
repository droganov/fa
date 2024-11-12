d:
	@echo "Starting dev"
	ENV_FILE=.env.local uvicorn app.main:app --reload

f:
	pip freeze > requirements.txt


# Yoyo migrations
y-new:
	@echo "Creating a new migration"
	@read -p "Enter migration name: " name; \
	yoyo new -m "$$name" --sql

y-up:
	ENV_FILE=.env.local python script.py yoyo-up

y-down:
	ENV_FILE=.env.local python script.py yoyo-down
