"""
A module for deploying project sources.
"""

# built-in
from pathlib import Path
from typing import Any, Dict

# internal
from userfs.config import ProjectSpecification


def deploy(
    root: Path, project: ProjectSpecification, options: Dict[str, Any]
) -> None:
    """Deploy an individual project."""

    print(root)
    print(project)
    print(options)
