# My AI Project

Hexagonal Python AI template using uv + FastAPI + pre-commit

## Quick Start

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
exec $SHELL

# Clone and setup project
git clone <your-repo>
cd my-ai-project

# Install dependencies and setup hooks
make setup
```

### Development

```bash
# Run the development server
make dev
# or
make run

# Format code
make format

# Run linting
make lint

# Run type checking
make type

# Run tests
make test

# Run all pre-commit hooks
make hooks
```

### Configuration

Copy `.env.example` to `.env` and configure your settings:

```bash
cp .env.example .env
```

Key environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `DATABASE_URL`: Database connection string (if using)
- `LOG_LEVEL`: Logging level (INFO, DEBUG, etc.)

## Architecture

This project follows hexagonal architecture principles:

- `app/api/`: HTTP transport layer (FastAPI routers)
- `app/config/`: Configuration and logging setup
- `app/core/`: Domain logic (business rules, entities)
- `app/services/`: Application services (LLM, embeddings, etc.)
- `app/infra/`: Infrastructure adapters (DB, external APIs)

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:2003/docs
- ReDoc: http://localhost:2003/redoc

## Development Tools

- **uv**: Fast Python package manager
- **FastAPI**: Modern web framework
- **Pre-commit**: Code quality hooks
- **Ruff**: Fast linting and formatting
- **MyPy**: Static type checking
- **Pytest**: Testing framework

## Make Commands

- `make setup`: Install dependencies and setup pre-commit hooks
- `make run`: Start development server
- `make format`: Format code with ruff and isort
- `make lint`: Run linting checks
- `make type`: Run type checking
- `make test`: Run tests
- `make hooks`: Run all pre-commit hooks
- `make clean`: Clean cache files
