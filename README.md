# FastAPI SQLAlchemy App

This is a FastAPI application using SQLAlchemy as ORM and PostgreSQL as the database backend.

## Setup

1. Make sure you have Python 3.12+ and Poetry installed.
2. Clone this repository and navigate to the project directory.
3. Install dependencies:
   ```
   poetry install
   ```
4. Set up your PostgreSQL database and update the connection string in `app/database.py`.

## Running the application

### Using Poetry

To run the FastAPI server:

```
make run
```

This will start the server at `http://localhost:8000`.

### Using Docker

To run the application using Docker:

```
make docker-run
```

This will build the Docker images (if needed) and start both the FastAPI application and the PostgreSQL database containers.

To stop the Docker containers:

```
make docker-stop
```

## Running tests

To run the tests:

```
make test
```

This will run both integration and functional tests.

## API Endpoints

- `POST /items/`: Create a new item
- `GET /items/`: List all items
- `GET /items/{item_id}`: Get a specific item by ID

## Development

- To format the code: `make format`
- To run linting: `make lint`

## Notes

- When running the application locally (not using Docker), make sure to set up your PostgreSQL database and update the connection string in `app/database.py` before running the application.
- You may need to create database migrations using Alembic for production use.