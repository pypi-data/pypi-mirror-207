"""
Common argument-parsing utilities for package commands.
"""
# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from pathlib import Path as _Path
from typing import Iterable, Set

# internal
from userfs.config import Config, ProjectInteraction, load_config
from userfs.project import execute_interactions


def add_common(parser: _ArgumentParser) -> None:
    """Add common command options."""

    parser.add_argument(
        "-c",
        "--config",
        type=_Path,
        help="an optional path to the configuration directory",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="interact with all configured projects",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        default=".*",
        help=(
            "a pattern to use to select project "
            "specifications filtered by name"
        ),
    )


def get_projects(args: _Namespace, config: Config) -> Set[str]:
    """Get a set of projects based on command-line arguments."""

    if args.all:
        names = set(config.projects.keys())
    else:
        names = set(args.projects)

    # Apply filter.

    return names


def run_command(
    interactions: Iterable[ProjectInteraction], args: _Namespace
) -> int:
    """Run a project interaction command."""

    config = load_config(root=args.config)
    return execute_interactions(
        interactions, get_projects(args, config), config
    )
