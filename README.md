# FastAPI with Strawberry GraphQL

A simple FastAPI project that demonstrates the integration of Strawberry GraphQL.

## Setup

1. Install uv if you haven't already:
```bash
pip install uv
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"  # Install with development dependencies including Ruff and mypy
```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

The application will be available at:
- Main API: http://localhost:8000
- GraphQL Playground: http://localhost:8000/graphql
- API Documentation: http://localhost:8000/docs

## Development

### Linting with Ruff

Run the linter:
```bash
ruff check .
```

To automatically fix issues that can be fixed:
```bash
ruff check --fix .
```

### Type Checking with mypy

Run type checking:
```bash
mypy .
```

For more detailed output:
```bash
mypy --pretty .
```

## GraphQL Queries

You can try these example queries in the GraphQL Playground:

```graphql
# Query all books
query {
  books {
    id
    title
    author
    year
  }
}

# Query a specific book by ID
query {
  book(id: 1) {
    id
    title
    author
    year
  }
}
```
