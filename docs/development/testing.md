# Testing

This guide covers testing practices for the Studio Pipeline.

## Test Structure

Tests are organized in the `tests/` directory:

```
tests/
├── unit/               # Unit tests
│   ├── test_core.py
│   ├── test_shotgrid.py
│   └── test_blender.py
├── integration/        # Integration tests
│   ├── test_pipeline.py
│   └── test_workflow.py
├── fixtures/          # Test fixtures and data
└── conftest.py        # Pytest configuration
```

## Running Tests

### All Tests

```bash
pytest
```

### Specific Test File

```bash
pytest tests/unit/test_core.py
```

### Specific Test

```bash
pytest tests/unit/test_core.py::test_pipeline_init
```

### With Coverage

```bash
pytest --cov=studio_pipeline --cov-report=html
```

### Verbose Output

```bash
pytest -v
```

## Writing Tests

### Unit Tests

Test individual functions and classes:

```python
# tests/unit/test_core.py
import pytest
from studio_pipeline.core import PathResolver

def test_path_resolver_basic():
    """Test basic path resolution."""
    resolver = PathResolver()
    path = resolver.resolve("asset_work", {
        "project": "TestProject",
        "asset": "test_asset"
    })
    assert "TestProject" in path
    assert "test_asset" in path

def test_path_resolver_missing_field():
    """Test path resolution with missing field."""
    resolver = PathResolver()
    with pytest.raises(ValueError):
        resolver.resolve("asset_work", {})
```

### Integration Tests

Test multiple components together:

```python
# tests/integration/test_workflow.py
import pytest
from studio_pipeline import Pipeline
from studio_pipeline.shotgrid import ShotgridClient

@pytest.mark.integration
def test_asset_publish_workflow(mock_shotgrid):
    """Test complete asset publishing workflow."""
    pipeline = Pipeline()
    sg = mock_shotgrid
    
    # Create asset
    asset = sg.create("Asset", {"code": "test_asset"})
    
    # Publish asset
    result = pipeline.publish_asset(
        filepath="/tmp/test.blend",
        entity=asset
    )
    
    assert result["type"] == "PublishedFile"
    assert "test_asset" in result["code"]
```

### Test Fixtures

Use fixtures for common test data:

```python
# tests/conftest.py
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_shotgrid():
    """Mock Shotgrid client."""
    sg = Mock()
    sg.find.return_value = [{"type": "Asset", "id": 1, "code": "test"}]
    sg.create.return_value = {"type": "Asset", "id": 1, "code": "test"}
    return sg

@pytest.fixture
def temp_blend_file(tmp_path):
    """Create temporary Blender file."""
    blend_file = tmp_path / "test.blend"
    blend_file.write_text("mock blend data")
    return str(blend_file)
```

## Test Categories

### Unit Tests

- Fast execution
- No external dependencies
- Mock external services
- Test single units of code

```python
@pytest.mark.unit
def test_version_increment():
    """Test version number increment."""
    from studio_pipeline.core import increment_version
    assert increment_version("v001") == "v002"
    assert increment_version("v099") == "v100"
```

### Integration Tests

- Test component interactions
- May use test databases
- Slower than unit tests
- More comprehensive

```python
@pytest.mark.integration
def test_shotgrid_integration(mock_shotgrid):
    """Test Shotgrid integration."""
    # Test code here
    pass
```

### End-to-End Tests

- Test complete workflows
- Use real or staging environments
- Slowest tests
- Most realistic

```python
@pytest.mark.e2e
def test_full_pipeline():
    """Test complete pipeline workflow."""
    # Test code here
    pass
```

## Mocking

### Mock External Services

```python
from unittest.mock import Mock, patch

def test_shotgrid_find():
    """Test Shotgrid find with mock."""
    with patch('shotgun_api3.Shotgun') as mock_sg:
        mock_sg.return_value.find.return_value = [
            {"type": "Asset", "id": 1}
        ]
        
        from studio_pipeline.shotgrid import ShotgridClient
        sg = ShotgridClient("url", "script", "key")
        results = sg.find("Asset", [])
        
        assert len(results) == 1
        assert results[0]["id"] == 1
```

### Mock File System

```python
def test_file_operation(tmp_path):
    """Test file operations with temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content")
    
    # Test your file operations
    result = process_file(str(test_file))
    
    assert result is not None
```

## Test Best Practices

### 1. Test Naming

Use descriptive names:

```python
# Good
def test_path_resolver_with_invalid_template():
    pass

# Bad
def test1():
    pass
```

### 2. Arrange-Act-Assert Pattern

```python
def test_version_creation():
    # Arrange
    vm = VersionManager()
    filepath = "/path/to/file.blend"
    
    # Act
    version = vm.create_version(filepath)
    
    # Assert
    assert version.startswith("v")
    assert version.endswith("001")
```

### 3. One Concept Per Test

```python
# Good - single concept
def test_path_resolver_asset():
    """Test asset path resolution."""
    # Test asset paths only

def test_path_resolver_shot():
    """Test shot path resolution."""
    # Test shot paths only

# Bad - multiple concepts
def test_path_resolver():
    """Test all path resolution."""
    # Tests too many things
```

### 4. Use Parametrize for Multiple Cases

```python
@pytest.mark.parametrize("input,expected", [
    ("v001", "v002"),
    ("v099", "v100"),
    ("v999", "v1000"),
])
def test_version_increment(input, expected):
    """Test version increment with multiple inputs."""
    assert increment_version(input) == expected
```

### 5. Test Edge Cases

```python
def test_version_increment_edge_cases():
    """Test version increment edge cases."""
    assert increment_version("v999") == "v1000"
    assert increment_version("v000") == "v001"
    
    with pytest.raises(ValueError):
        increment_version("invalid")
    
    with pytest.raises(ValueError):
        increment_version("")
```

## Continuous Integration

Tests run automatically on CI:

```yaml
# .github/workflows/tests.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: pytest --cov=studio_pipeline
```

## Coverage Goals

- Aim for >80% code coverage
- 100% coverage for critical paths
- Test both success and failure cases
- Test edge cases and boundary conditions

## Test Performance

### Fast Tests

```bash
# Run only fast tests
pytest -m "not slow"
```

### Mark Slow Tests

```python
@pytest.mark.slow
def test_heavy_operation():
    """Test that takes a long time."""
    # Slow test code
    pass
```

## Debugging Tests

### Run with Debugging

```bash
pytest --pdb  # Drop into debugger on failure
```

### Print Output

```bash
pytest -s  # Show print statements
```

### Increase Verbosity

```bash
pytest -vv  # Very verbose output
```

## Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)
- [Mock Objects](https://docs.python.org/3/library/unittest.mock.html)
