# Contributing

Thank you for your interest in contributing to the Studio Pipeline! This guide will help you get started.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Familiarity with Blender and/or Shotgrid (for relevant contributions)

### Setting Up Development Environment

1. **Fork and Clone**

```bash
git clone https://github.com/YOUR_USERNAME/StudioPipeline.git
cd StudioPipeline
```

2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

4. **Install in Development Mode**

```bash
pip install -e .
```

## Development Workflow

### Branching Strategy

- `main` - Stable release branch
- `develop` - Development branch
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches
- `hotfix/*` - Critical hotfix branches

### Creating a Feature Branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/my-new-feature
```

### Making Changes

1. **Write Code** - Implement your feature or fix
2. **Add Tests** - Ensure your code is tested
3. **Update Docs** - Update documentation if needed
4. **Run Tests** - Make sure all tests pass
5. **Lint Code** - Follow code style guidelines

### Code Style

We follow PEP 8 style guidelines:

```bash
# Format code with black
black src/

# Check with flake8
flake8 src/

# Sort imports with isort
isort src/
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_shotgrid.py

# Run with coverage
pytest --cov=studio_pipeline
```

### Commit Messages

Follow conventional commits format:

```
type(scope): subject

body

footer
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Build/tooling changes

Example:
```
feat(shotgrid): add batch update support

Implement batch update functionality to update multiple
entities in a single API call for better performance.

Closes #123
```

## Contributing Guidelines

### Code Quality

- Write clean, readable code
- Add docstrings to all functions and classes
- Use type hints where appropriate
- Follow existing code patterns

### Testing

- Write unit tests for new functionality
- Maintain or improve test coverage
- Test edge cases and error conditions
- Use meaningful test names

### Documentation

- Update relevant documentation
- Add code examples for new features
- Keep API reference up to date
- Write clear commit messages

## Pull Request Process

1. **Update Your Branch**

```bash
git fetch origin
git rebase origin/develop
```

2. **Push Your Changes**

```bash
git push origin feature/my-new-feature
```

3. **Create Pull Request**

- Go to GitHub and create a PR
- Fill in the PR template
- Link related issues
- Request reviews

4. **Address Feedback**

- Respond to review comments
- Make requested changes
- Push updates to your branch

5. **Merge**

- Once approved, maintainers will merge
- Delete your feature branch after merge

## Issue Reporting

### Bug Reports

Include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
- Error messages and logs

### Feature Requests

Include:
- Clear description of the feature
- Use cases and motivation
- Proposed implementation (optional)
- Examples (optional)

## Code Review Guidelines

### For Authors

- Keep PRs focused and small
- Provide clear descriptions
- Respond to feedback promptly
- Be open to suggestions

### For Reviewers

- Be constructive and respectful
- Focus on code quality and maintainability
- Test the changes if possible
- Approve when satisfied

## Community Guidelines

- Be respectful and professional
- Welcome newcomers
- Help others learn
- Give constructive feedback
- Follow the Code of Conduct

## Resources

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Writing Good Documentation](https://www.writethedocs.org/)

## Getting Help

- Open an issue for bugs or features
- Join our community discussions
- Contact maintainers for questions

Thank you for contributing to Studio Pipeline! 🎉
