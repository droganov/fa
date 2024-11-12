d:
	@echo "Starting dev"
	uvicorn app.main:app --reload

f:
	pip freeze > requirements.txt


# Yoyo migrations
y-new:
	@echo "Creating a new migration"
	@read -p "Enter migration name: " name; \
	yoyo new -m "$$name" --sql

y-up:
	python script.py apply_migrations

y-down:
	python script.py rollback_migrations
