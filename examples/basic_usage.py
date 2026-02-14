"""
Example: Basic Pipeline Usage

This example demonstrates basic usage of the Studio Pipeline.
"""

from studio_pipeline import Pipeline


def main():
    """Main example function."""
    # Initialize the pipeline
    print("Initializing Studio Pipeline...")
    pipeline = Pipeline()
    
    # Get project information
    project = pipeline.get_project()
    print(f"Current Project: {project['name']}")
    
    # Note: This is a basic example. Full functionality requires:
    # - Shotgrid configuration
    # - Blender installation
    # - Proper project setup
    
    print("\nPipeline initialized successfully!")
    print("\nNext steps:")
    print("1. Configure Shotgrid connection")
    print("2. Set up Blender integration")
    print("3. Configure project paths")
    print("\nSee documentation for detailed setup: https://supervirtuel.github.io/StudioPipeline/")


if __name__ == "__main__":
    main()
