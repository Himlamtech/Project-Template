#!/bin/bash
# Run strict pre-commit checks (mypy, bandit, etc.)
# Use this before important commits or CI/CD

echo "🔍 Running strict code quality checks..."
uv run pre-commit run --config .pre-commit-config-strict.yaml --all-files

echo ""
echo "💡 To fix issues manually:"
echo "  - Type errors: Add type hints, fix mypy issues"
echo "  - Security: Review bandit warnings"
echo "  - Files: Fix YAML/TOML/JSON syntax"
