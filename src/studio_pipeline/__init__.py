"""
Studio Pipeline - A comprehensive pipeline for studio workflows using Shotgrid Toolkit and Blender.

This package provides tools and automation for:
- Shotgrid integration
- Blender automation
- Asset management
- Version control
- Rendering pipelines
"""

__version__ = "0.1.0"
__author__ = "Studio Pipeline Team"

from .core.pipeline import Pipeline

__all__ = ["Pipeline", "__version__"]
