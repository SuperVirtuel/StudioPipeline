# Installation

This guide will help you install and set up the Studio Pipeline.

## Prerequisites

Before installing the Studio Pipeline, ensure you have:

- **Python 3.8+** installed
- **Blender 3.0+** (for Blender integration)
- Access to a **Shotgrid** instance (for Shotgrid integration)
- **Git** for version control

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/SuperVirtuel/StudioPipeline.git
cd StudioPipeline
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment:

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Package

For development:

```bash
pip install -e .
```

For production:

```bash
pip install .
```

## Configuration

### Shotgrid Configuration

Create a configuration file at `config/shotgrid.yml`:

```yaml
server: https://your-studio.shotgunstudio.com
script_name: your_script_name
api_key: your_api_key
```

!!! warning "Security"
    Never commit your API keys to version control. Use environment variables or secure key management systems.

### Blender Configuration

Set the Blender executable path:

```bash
export BLENDER_PATH=/path/to/blender
```

Or in Windows:

```cmd
set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender\blender.exe
```

## Verify Installation

Run the following to verify the installation:

```bash
python -c "import studio_pipeline; print(studio_pipeline.__version__)"
```

## Next Steps

- [Quick Start Guide](quickstart.md) - Get started with your first pipeline
- [Pipeline Overview](../pipeline/overview.md) - Learn about the architecture
