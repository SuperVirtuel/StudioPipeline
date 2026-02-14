# Blender Integration

The Blender integration module provides tools and automation for working with Blender in a production pipeline.

## Overview

Blender is a powerful open-source 3D creation suite. Our pipeline integrates with Blender to:

- Automate rendering and export tasks
- Standardize scene setup and organization
- Integrate with Shotgrid for asset tracking
- Provide custom tools for artists

## Setup

### Blender Python API

The pipeline uses Blender's Python API (bpy):

```python
from studio_pipeline.blender import BlenderIntegration

blender = BlenderIntegration()
blender.set_blender_path("/usr/bin/blender")
```

### Headless Mode

For automation, use Blender in headless mode:

```python
blender.run_script(
    script="/path/to/script.py",
    blend_file="/path/to/scene.blend",
    headless=True
)
```

## Scene Management

### Opening and Saving

```python
from studio_pipeline.blender import SceneManager

scene = SceneManager()

# Open a file
scene.open("/path/to/scene.blend")

# Save
scene.save()

# Save as a new file
scene.save_as("/path/to/new_scene.blend")
```

### Scene Setup

```python
# Set render settings
scene.set_render_settings({
    "resolution_x": 1920,
    "resolution_y": 1080,
    "fps": 24,
    "frame_start": 1,
    "frame_end": 250
})

# Set output format
scene.set_output_format("PNG", quality=90)
```

## Rendering

### Single Frame Render

```python
from studio_pipeline.blender import Renderer

renderer = Renderer()
renderer.render_frame(
    blend_file="/path/to/scene.blend",
    frame=1,
    output="/path/to/output/frame_001.png"
)
```

### Animation Render

```python
# Render entire animation
renderer.render_animation(
    blend_file="/path/to/scene.blend",
    output_dir="/path/to/output/",
    frame_start=1,
    frame_end=250
)
```

### Batch Rendering

```python
from studio_pipeline.blender import BatchRenderer

batch = BatchRenderer()

# Add multiple render jobs
batch.add_job("/path/to/scene1.blend", frames=[1, 10, 20])
batch.add_job("/path/to/scene2.blend", frames=[1, 15, 30])

# Execute all jobs
batch.execute(parallel=True, max_workers=4)
```

## Asset Export

### Exporting Models

```python
from studio_pipeline.blender import AssetExporter

exporter = AssetExporter()

# Export as FBX
exporter.export(
    blend_file="/path/to/asset.blend",
    output="/path/to/asset.fbx",
    format="FBX",
    options={
        "use_selection": False,
        "global_scale": 1.0,
        "apply_modifiers": True
    }
)

# Export as USD
exporter.export(
    blend_file="/path/to/asset.blend",
    output="/path/to/asset.usd",
    format="USD"
)
```

### Supported Formats

- FBX
- OBJ
- Alembic (ABC)
- USD
- glTF/GLB
- Collada (DAE)

## Custom Blender Add-ons

### Installing Add-ons

```python
from studio_pipeline.blender import AddonManager

addon_mgr = AddonManager()

# Install custom add-on
addon_mgr.install("/path/to/addon.zip")

# Enable add-on
addon_mgr.enable("addon_name")
```

### Creating Pipeline Add-ons

Create custom tools for artists:

```python
# addon_example.py
import bpy

class PIPELINE_OT_PublishAsset(bpy.types.Operator):
    bl_idname = "pipeline.publish_asset"
    bl_label = "Publish Asset"
    
    def execute(self, context):
        # Your publish logic here
        from studio_pipeline.core import AssetPublisher
        publisher = AssetPublisher()
        publisher.publish(bpy.data.filepath)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(PIPELINE_OT_PublishAsset)

def unregister():
    bpy.utils.unregister_class(PIPELINE_OT_PublishAsset)
```

## Integration with Shotgrid

### Publishing to Shotgrid

```python
from studio_pipeline.blender import BlenderShotgridIntegration

integration = BlenderShotgridIntegration()

# Render and publish to Shotgrid
integration.render_and_publish(
    blend_file="/path/to/scene.blend",
    shotgrid_entity={"type": "Shot", "id": 123},
    task_id=456
)
```

### Loading from Shotgrid

```python
# Load asset from Shotgrid
integration.load_asset(
    asset_id=789,
    version="latest"
)
```

## Automation Scripts

### Example: Automated Turntable Render

```python
from studio_pipeline.blender import TurntableRenderer

turntable = TurntableRenderer()
turntable.create_turntable(
    blend_file="/path/to/asset.blend",
    object_name="MyAsset",
    frames=360,
    output="/path/to/turntable/"
)
```

## Best Practices

- **Use Relative Paths**: Keep .blend files portable
- **Clean Scene**: Remove unused data before rendering
- **Version Files**: Always maintain version history
- **Test Renders**: Do test renders before batch jobs
- **Optimize Scenes**: Keep poly counts and textures reasonable

## Troubleshooting

### Common Issues

**Blender not found**:
```python
# Set explicit path
blender.set_blender_path("/Applications/Blender.app/Contents/MacOS/Blender")
```

**Memory issues**:
```python
# Render with memory management
renderer.render_animation(
    blend_file="/path/to/scene.blend",
    output_dir="/path/to/output/",
    tile_size=256,  # Smaller tiles use less memory
    use_persistent_data=False
)
```

## API Reference

For detailed API documentation, see [Blender API Reference](../api/blender.md).
