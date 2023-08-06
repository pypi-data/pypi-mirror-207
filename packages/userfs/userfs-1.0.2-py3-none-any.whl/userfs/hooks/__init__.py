"""
A module implementing interfaces to interact with external scripts and modules.
"""

# built-in
from contextlib import contextmanager, suppress
from importlib import import_module
from logging import getLogger
from pathlib import Path
import sys
from typing import Callable, Dict, Iterator, List, Optional, Set, cast

# third-party
from vcorelib.names import to_snake

# internal
from userfs.config import Config, Interact, ProjectInteraction

HookLoader = Callable[[str, ProjectInteraction, Config], Optional[Interact]]
LOG = getLogger(__name__)


@contextmanager
def paths_added(paths: List[Path]) -> Iterator[None]:
    """Add search paths to sys.path as a context manager."""

    added = set()
    orig_set = set(sys.path)

    # Add provided paths.
    for path in [str(x) for x in paths]:
        if path not in orig_set and path not in added:
            sys.path.append(path)
            added.add(path)

    try:
        yield
    finally:
        # Remove paths that we actually added. Don't restore the previous state
        # of sys.path in case anything else modified it.
        restore_path = []
        for path in sys.path:
            if path not in added:
                restore_path.append(path)
        sys.path = restore_path


def get_hooks(
    prefixes: Set[str],
    project: str,
    interaction: ProjectInteraction,
    config: Config,
) -> Dict[str, Optional[Interact]]:
    """Attempt to load a certain kind of project hook."""

    result: Dict[str, Optional[Interact]] = {}

    with paths_added(config.hook_paths):
        for prefix in prefixes:
            result[prefix] = None
            with suppress(ModuleNotFoundError):
                mod_name = f"{to_snake(project)}_hooks"
                LOG.info("Looking for '%s' module.", mod_name)
                mod = import_module(mod_name)

                hook_name = f"{prefix}_{interaction.value}"
                LOG.info("Looking for '%s' hook.", hook_name)
                result[prefix] = cast(Interact, getattr(mod, hook_name, None))

    return result
