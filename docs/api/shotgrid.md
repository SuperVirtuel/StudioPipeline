# Shotgrid API Reference

API documentation for the Shotgrid integration module.

## ShotgridClient

The main client for interacting with Shotgrid.

### Initialization

```python
from studio_pipeline.shotgrid import ShotgridClient

# Script-based authentication
sg = ShotgridClient(
    server="https://studio.shotgunstudio.com",
    script_name="pipeline_script",
    api_key="api_key_here"
)

# From configuration
sg = ShotgridClient.from_config("/path/to/config.yml")
```

## Methods

### find()

Search for entities in Shotgrid.

```python
def find(
    entity_type: str,
    filters: List[List],
    fields: List[str] = None,
    order: List[dict] = None,
    limit: int = 0
) -> List[dict]:
    """
    Find entities matching the given criteria.
    
    Args:
        entity_type: Type of entity (e.g., "Asset", "Shot")
        filters: List of filter conditions
        fields: List of fields to return
        order: Sorting order
        limit: Maximum number of results
        
    Returns:
        List of entity dictionaries
    """
```

**Example:**

```python
assets = sg.find(
    "Asset",
    [["project", "is", {"type": "Project", "id": 123}]],
    ["code", "sg_asset_type"]
)
```

### create()

Create a new entity in Shotgrid.

```python
def create(
    entity_type: str,
    data: dict
) -> dict:
    """
    Create a new entity.
    
    Args:
        entity_type: Type of entity to create
        data: Entity data
        
    Returns:
        Created entity dictionary
    """
```

### update()

Update an existing entity.

```python
def update(
    entity_type: str,
    entity_id: int,
    data: dict
) -> dict:
    """
    Update an entity.
    
    Args:
        entity_type: Type of entity
        entity_id: Entity ID
        data: Fields to update
        
    Returns:
        Updated entity dictionary
    """
```

### delete()

Delete an entity from Shotgrid.

```python
def delete(
    entity_type: str,
    entity_id: int
) -> bool:
    """
    Delete an entity.
    
    Args:
        entity_type: Type of entity
        entity_id: Entity ID
        
    Returns:
        True if successful
    """
```

## FilePublisher

Upload and publish files to Shotgrid.

### Example Usage

```python
from studio_pipeline.shotgrid import FilePublisher

publisher = FilePublisher(sg)

# Upload a file
result = publisher.publish(
    filepath="/path/to/render.png",
    entity_type="Version",
    entity_id=123,
    field_name="sg_uploaded_movie"
)
```

## EventListener

Listen for and respond to Shotgrid events.

### Example Usage

```python
from studio_pipeline.shotgrid import EventListener

def on_version_create(event):
    print(f"New version created: {event['entity']['id']}")

listener = EventListener(sg)
listener.register("Version", "create", on_version_create)
listener.start()
```

## Entity Types

Common Shotgrid entity types:

- `Project` - Production projects
- `Asset` - Assets (characters, props, etc.)
- `Shot` - Shots in sequences
- `Sequence` - Shot sequences
- `Task` - Work tasks
- `Version` - File versions
- `PublishedFile` - Published files
- `Note` - Notes and feedback
- `Playlist` - Review playlists

## Filter Operators

Common filter operators:

- `is` - Exact match
- `is_not` - Not equal to
- `less_than` - Less than
- `greater_than` - Greater than
- `contains` - Contains substring
- `not_contains` - Does not contain
- `starts_with` - Starts with
- `ends_with` - Ends with
- `in` - In list
- `not_in` - Not in list
- `between` - Between two values

## Example Filters

```python
# Find active assets
[["sg_status_list", "is", "act"]]

# Find shots in sequence
[["sg_sequence", "is", {"type": "Sequence", "id": 456}]]

# Find tasks assigned to user
[["task_assignees", "is", {"type": "HumanUser", "id": 789}]]

# Complex filter with AND/OR
{
    "filter_operator": "any",
    "filters": [
        ["sg_status_list", "is", "rdy"],
        ["sg_status_list", "is", "ip"]
    ]
}
```

## Best Practices

1. **Use specific filters** to reduce data transfer
2. **Request only needed fields** for better performance
3. **Batch operations** when updating multiple entities
4. **Handle errors** gracefully with try/except
5. **Cache frequently accessed data** to reduce API calls
