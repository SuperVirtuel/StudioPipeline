# Quick Start

Get up and running with the Studio Pipeline in minutes!

## Your First Pipeline

### 1. Import the Pipeline

```python
from studio_pipeline import Pipeline

# Initialize the pipeline
pipeline = Pipeline()
```

### 2. Connect to Shotgrid

```python
from studio_pipeline.shotgrid import ShotgridClient

# Connect to Shotgrid
sg = ShotgridClient(
    server="https://your-studio.shotgunstudio.com",
    script_name="your_script_name",
    api_key="your_api_key"
)

# Find assets
assets = sg.find("Asset", [["project", "is", {"type": "Project", "id": 1}]])
print(f"Found {len(assets)} assets")
```

### 3. Work with Blender

```python
from studio_pipeline.blender import BlenderIntegration

# Initialize Blender integration
blender = BlenderIntegration()

# Open a Blender file
blender.open_file("/path/to/scene.blend")

# Render
blender.render(output_path="/path/to/output.png")
```

## Common Workflows

### Asset Publishing

Publish an asset to Shotgrid:

```python
from studio_pipeline.core import AssetPublisher

publisher = AssetPublisher()
publisher.publish(
    asset_path="/path/to/asset.blend",
    asset_type="Model",
    version="v001",
    shotgrid_entity={"type": "Asset", "id": 123}
)
```

### Batch Rendering

Render multiple shots:

```python
from studio_pipeline.blender import BatchRenderer

renderer = BatchRenderer()
shots = sg.find("Shot", [["sg_status_list", "is", "rdy"]])

for shot in shots:
    renderer.render_shot(shot)
```

## Examples

Check out the `examples/` directory for more detailed examples:

- `examples/shotgrid_sync.py` - Sync assets with Shotgrid
- `examples/batch_export.py` - Batch export Blender files
- `examples/automated_render.py` - Automated render pipeline

## Next Steps

- Learn about the [Pipeline Architecture](../pipeline/overview.md)
- Explore [Shotgrid Integration](../pipeline/shotgrid.md)
- Discover [Blender Tools](../pipeline/blender.md)
