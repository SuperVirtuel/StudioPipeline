# Blender API Reference

API documentation for the Blender integration module.

## BlenderIntegration

Main class for Blender integration.

### Initialization

```python
from studio_pipeline.blender import BlenderIntegration

blender = BlenderIntegration()
blender.set_blender_path("/usr/bin/blender")
```

## SceneManager

Manage Blender scenes.

### Methods

```python
class SceneManager:
    def open(self, filepath: str) -> None:
        """Open a Blender file."""
        
    def save(self) -> None:
        """Save the current file."""
        
    def save_as(self, filepath: str) -> None:
        """Save as a new file."""
        
    def set_render_settings(self, settings: dict) -> None:
        """Configure render settings."""
```

## Renderer

Render Blender scenes.

### render_frame()

Render a single frame.

```python
def render_frame(
    blend_file: str,
    frame: int,
    output: str,
    engine: str = "CYCLES"
) -> bool:
    """
    Render a single frame.
    
    Args:
        blend_file: Path to .blend file
        frame: Frame number to render
        output: Output file path
        engine: Render engine (CYCLES, EEVEE, WORKBENCH)
        
    Returns:
        True if successful
    """
```

### render_animation()

Render an animation sequence.

```python
def render_animation(
    blend_file: str,
    output_dir: str,
    frame_start: int = None,
    frame_end: int = None,
    engine: str = "CYCLES"
) -> bool:
    """
    Render animation.
    
    Args:
        blend_file: Path to .blend file
        output_dir: Output directory
        frame_start: First frame (None = use scene)
        frame_end: Last frame (None = use scene)
        engine: Render engine
        
    Returns:
        True if successful
    """
```

## BatchRenderer

Batch rendering multiple files.

### Example Usage

```python
from studio_pipeline.blender import BatchRenderer

batch = BatchRenderer()

# Add render jobs
batch.add_job("/path/to/scene1.blend", frames=[1, 10, 20])
batch.add_job("/path/to/scene2.blend", frames=range(1, 101))

# Execute with parallel processing
batch.execute(parallel=True, max_workers=4)
```

## AssetExporter

Export assets from Blender.

### export()

Export to various formats.

```python
def export(
    blend_file: str,
    output: str,
    format: str,
    options: dict = None
) -> bool:
    """
    Export asset.
    
    Args:
        blend_file: Source .blend file
        output: Output file path
        format: Export format (FBX, OBJ, USD, etc.)
        options: Format-specific options
        
    Returns:
        True if successful
    """
```

### Supported Formats

```python
SUPPORTED_FORMATS = {
    "FBX": {
        "use_selection": bool,
        "global_scale": float,
        "apply_modifiers": bool,
        "use_mesh_modifiers": bool
    },
    "OBJ": {
        "use_selection": bool,
        "use_materials": bool,
        "use_triangles": bool
    },
    "USD": {
        "use_selection": bool,
        "export_animation": bool,
        "export_hair": bool
    },
    "GLTF": {
        "export_format": str,  # "GLB" or "GLTF_SEPARATE"
        "export_texcoords": bool,
        "export_normals": bool
    }
}
```

## AddonManager

Manage Blender add-ons.

### Methods

```python
class AddonManager:
    def install(self, addon_path: str) -> bool:
        """Install an add-on from file."""
        
    def enable(self, addon_name: str) -> bool:
        """Enable an installed add-on."""
        
    def disable(self, addon_name: str) -> bool:
        """Disable an add-on."""
        
    def list_addons(self) -> List[str]:
        """List all installed add-ons."""
```

## BlenderShotgridIntegration

Integrate Blender with Shotgrid.

### render_and_publish()

Render and publish to Shotgrid.

```python
def render_and_publish(
    blend_file: str,
    shotgrid_entity: dict,
    task_id: int,
    render_settings: dict = None
) -> dict:
    """
    Render and publish to Shotgrid.
    
    Args:
        blend_file: Path to .blend file
        shotgrid_entity: Shotgrid entity dict
        task_id: Task ID
        render_settings: Optional render settings
        
    Returns:
        Created Version entity
    """
```

### load_asset()

Load asset from Shotgrid.

```python
def load_asset(
    asset_id: int,
    version: str = "latest"
) -> str:
    """
    Load asset from Shotgrid.
    
    Args:
        asset_id: Asset ID
        version: Version number or "latest"
        
    Returns:
        Path to loaded file
    """
```

## TurntableRenderer

Create turntable renders.

### Example Usage

```python
from studio_pipeline.blender import TurntableRenderer

turntable = TurntableRenderer()
turntable.create_turntable(
    blend_file="/path/to/asset.blend",
    object_name="MyAsset",
    frames=360,
    output="/path/to/turntable/",
    camera_distance=5.0,
    camera_height=2.0
)
```

## Exceptions

### BlenderError

Base exception for Blender-related errors.

### RenderError

Raised when rendering fails.

### ExportError

Raised when export fails.

### AddonError

Raised when add-on operation fails.
