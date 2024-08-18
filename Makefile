.PHONY: docker-build docker-run docker-stop docker-test format lint clean

run:
	poetry run uvicorn app.main:app --reload

format:
	poetry run black .
	poetry run isort .

lint:
	poetry run mypy .

docker-build:
	docker-compose build --no-cache

docker-run:
	docker-compose up -d --build 

docker-stop:
	docker-compose down

docker-test:
	docker-compose run --rm --build \
		-e DATABASE_URL=postgresql://testuser:testpassword@test-db:5432/testdb \
		web pytest -v /app/tests

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
