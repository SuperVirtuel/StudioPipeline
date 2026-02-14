# Studio Pipeline

A comprehensive Python-based pipeline for studio workflows integrating **Shotgrid (Flow) Toolkit** and **Blender**.

[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://supervirtuel.github.io/StudioPipeline/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🎯 Overview

This project provides a unified pipeline system for production studios, combining the power of Shotgrid for asset tracking and task management with Blender for 3D creation and animation.

### Key Features

- **🔗 Shotgrid Integration**: Seamless connectivity with Shotgrid for production tracking
- **🎨 Blender Automation**: Automated rendering, export, and asset management
- **📦 Asset Management**: Version control and asset publishing
- **🔄 Automated Workflows**: Python-based pipeline automation
- **📚 Comprehensive Documentation**: Full documentation with MkDocs

## 📋 Requirements

- Python 3.8 or higher
- Blender 3.0+ (for Blender integration)
- Access to a Shotgrid instance (for Shotgrid features)

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/SuperVirtuel/StudioPipeline.git
cd StudioPipeline

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

### Basic Usage

```python
from studio_pipeline import Pipeline

# Initialize the pipeline
pipeline = Pipeline()

# Get project information
project = pipeline.get_project()
print(f"Working on: {project['name']}")
```

## 📖 Documentation

Full documentation is available at: [https://supervirtuel.github.io/StudioPipeline/](https://supervirtuel.github.io/StudioPipeline/)

### Building Documentation Locally

```bash
# Install documentation dependencies
pip install -r requirements.txt

# Serve documentation locally
mkdocs serve

# Build static documentation
mkdocs build
```

The documentation will be available at `http://localhost:8000`

## 📁 Project Structure

```
StudioPipeline/
├── src/
│   └── studio_pipeline/      # Main package
│       ├── core/             # Core pipeline functionality
│       ├── shotgrid/         # Shotgrid integration
│       └── blender/          # Blender integration
├── docs/                      # MkDocs documentation
│   ├── getting-started/      # Installation and quickstart guides
│   ├── pipeline/             # Pipeline documentation
│   ├── api/                  # API reference
│   └── development/          # Development guides
├── tests/                     # Test suite
├── examples/                  # Usage examples
├── .github/
│   └── workflows/            # GitHub Actions workflows
├── mkdocs.yml                # MkDocs configuration
├── pyproject.toml            # Python project configuration
└── requirements.txt          # Python dependencies
```

## 🔧 Development

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/

# Lint code
flake8 src/
```

### Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development/contributing.md) for details.

## 📝 Documentation Pages

The documentation includes:

- **Getting Started**: Installation and quick start guides
- **Pipeline Overview**: Architecture and workflow documentation
- **Shotgrid Integration**: Detailed Shotgrid integration guide
- **Blender Integration**: Blender automation and tools
- **API Reference**: Complete API documentation
- **Development**: Contributing and testing guides

## 🔗 Links

- **Documentation**: [https://supervirtuel.github.io/StudioPipeline/](https://supervirtuel.github.io/StudioPipeline/)
- **Repository**: [https://github.com/SuperVirtuel/StudioPipeline](https://github.com/SuperVirtuel/StudioPipeline)
- **Issues**: [https://github.com/SuperVirtuel/StudioPipeline/issues](https://github.com/SuperVirtuel/StudioPipeline/issues)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- Powered by [Shotgrid](https://www.shotgridsoftware.com/) and [Blender](https://www.blender.org/)

---

**Note**: This is an early-stage project. APIs and workflows may change as the project evolves.
