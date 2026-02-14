# Core API Reference

The core module provides the foundational functionality for the Studio Pipeline.

## Pipeline Class

The main Pipeline class that orchestrates all pipeline operations.

### Example Usage

```python
from studio_pipeline import Pipeline

# Initialize the pipeline
pipeline = Pipeline(config_path="/path/to/config.yml")

# Get project info
project = pipeline.get_project()
print(f"Project: {project.name}")

# Set up paths
pipeline.setup_paths()
```

## Configuration

### Configuration Management

The Config class handles loading and managing pipeline settings.

```python
from studio_pipeline.core import Config

config = Config.load("/path/to/config.yml")
print(config.get("shotgrid.server"))
```

## Path Resolution

### Path Templates

```python
from studio_pipeline.core import PathResolver

resolver = PathResolver()
path = resolver.resolve("asset_work", {
    "project": "MyProject",
    "asset": "character_hero",
    "step": "model",
    "version": "v001"
})
# Returns: /mnt/projects/MyProject/assets/character_hero/model/v001
```

## Version Control

### Version Management

```python
from studio_pipeline.core import VersionManager

vm = VersionManager()

# Get latest version
latest = vm.get_latest_version("/path/to/asset")
print(f"Latest version: {latest}")

# Create new version
new_version = vm.create_version(
    filepath="/path/to/asset.blend",
    comment="Updated materials"
)
```

## Logging

### Logging System

```python
from studio_pipeline.core import get_logger

logger = get_logger(__name__)

logger.info("Pipeline started")
logger.warning("Deprecated function used")
logger.error("Failed to publish asset")
```

## Classes and Functions

### Pipeline

**Methods:**

- `__init__(config_path: str = None)` - Initialize the pipeline
- `get_project() -> Project` - Get current project
- `setup_paths()` - Set up project directory structure
- `get_config() -> Config` - Get configuration object

### Config

**Methods:**

- `load(path: str) -> Config` - Load configuration from file
- `get(key: str, default=None) -> Any` - Get configuration value
- `set(key: str, value: Any)` - Set configuration value
- `save(path: str = None)` - Save configuration to file

### PathResolver

**Methods:**

- `resolve(template: str, fields: dict) -> str` - Resolve path template
- `get_template(name: str) -> str` - Get path template by name
- `add_template(name: str, template: str)` - Add custom template

### VersionManager

**Methods:**

- `get_latest_version(path: str) -> str` - Get latest version number
- `create_version(filepath: str, comment: str = None) -> str` - Create new version
- `list_versions(path: str) -> List[str]` - List all versions
- `restore_version(filepath: str, version: str)` - Restore specific version

## Exceptions

### PipelineError

Base exception for all pipeline errors.

```python
from studio_pipeline.core.exceptions import PipelineError

try:
    pipeline.setup_paths()
except PipelineError as e:
    print(f"Pipeline error: {e}")
```

### ConfigurationError

Raised when configuration is invalid or missing.

### PathResolutionError

Raised when path cannot be resolved.

### VersionError

Raised when version operation fails.
