# Shotgrid Integration

The Shotgrid integration module provides seamless connectivity with Shotgrid (formerly Shotgun) for production tracking and asset management.

## Overview

Shotgrid is a production tracking platform used by studios worldwide. Our pipeline integrates with Shotgrid to:

- Track assets, shots, and tasks
- Manage versions and reviews
- Publish files and media
- Synchronize production data

## Setup

### Authentication

The pipeline supports multiple authentication methods:

#### Script-based Authentication

```python
from studio_pipeline.shotgrid import ShotgridClient

sg = ShotgridClient(
    server="https://your-studio.shotgunstudio.com",
    script_name="pipeline_script",
    api_key="your_api_key"
)
```

#### User-based Authentication

```python
sg = ShotgridClient.from_user_credentials(
    server="https://your-studio.shotgunstudio.com",
    username="artist@studio.com",
    password="secure_password"
)
```

### Configuration File

Store credentials securely in a config file:

```yaml
# config/shotgrid.yml
server: https://your-studio.shotgunstudio.com
script_name: pipeline_script
api_key: ${SHOTGRID_API_KEY}  # Use environment variable
```

## Common Operations

### Finding Entities

```python
# Find all assets in a project
assets = sg.find(
    "Asset",
    [["project", "is", {"type": "Project", "id": 123}]],
    ["code", "sg_asset_type", "sg_status_list"]
)

# Find shots ready for animation
shots = sg.find(
    "Shot",
    [
        ["project", "is", {"type": "Project", "id": 123}],
        ["sg_status_list", "is", "rdy"]
    ],
    ["code", "sg_sequence", "sg_cut_in", "sg_cut_out"]
)
```

### Creating Entities

```python
# Create a new version
version = sg.create("Version", {
    "project": {"type": "Project", "id": 123},
    "code": "asset_model_v001",
    "entity": {"type": "Asset", "id": 456},
    "sg_task": {"type": "Task", "id": 789},
    "description": "Initial model version"
})
```

### Updating Entities

```python
# Update task status
sg.update("Task", 789, {
    "sg_status_list": "ip"  # In Progress
})
```

### Publishing Files

```python
from studio_pipeline.shotgrid import FilePublisher

publisher = FilePublisher(sg)

# Upload a file
publisher.publish(
    filepath="/path/to/asset.blend",
    entity_type="Version",
    entity_id=version["id"],
    field_name="sg_uploaded_movie"
)
```

## Advanced Features

### Event Handling

Listen for Shotgrid events:

```python
from studio_pipeline.shotgrid import EventListener

def on_task_update(event):
    print(f"Task {event['entity']['id']} was updated")

listener = EventListener(sg)
listener.register("Task", "update", on_task_update)
listener.start()
```

### Batch Operations

Perform bulk operations efficiently:

```python
# Batch update multiple tasks
updates = [
    {"type": "Task", "id": 100, "sg_status_list": "fin"},
    {"type": "Task", "id": 101, "sg_status_list": "fin"},
    {"type": "Task", "id": 102, "sg_status_list": "fin"},
]
sg.batch_update(updates)
```

### Custom Fields

Access custom fields defined in your Shotgrid schema:

```python
# Query custom fields
assets = sg.find(
    "Asset",
    [["project", "is", {"type": "Project", "id": 123}]],
    ["code", "sg_custom_field_1", "sg_custom_field_2"]
)
```

## Shotgrid Toolkit Integration

The pipeline is compatible with Shotgrid Toolkit (tk):

```python
import sgtk

# Initialize toolkit
tk = sgtk.sgtk_from_path("/path/to/project")

# Get templates
template = tk.templates["asset_work_area"]
path = template.apply_fields({"Asset": "character", "Step": "model"})
```

## Best Practices

- **Use Filters**: Always filter queries to reduce data transfer
- **Cache Results**: Cache frequently accessed data
- **Batch Operations**: Use batch methods for multiple updates
- **Error Handling**: Always handle API errors gracefully
- **Rate Limiting**: Be mindful of API rate limits

## API Reference

For detailed API documentation, see [Shotgrid API Reference](../api/shotgrid.md).
