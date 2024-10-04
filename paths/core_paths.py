# Copyright (C) 2023 Robert Wiese - All Rights Reserved.
# Copyright (C) 2023 Robert Wiese - All Rights Reserved.
"""Get core helpful paths for repository."""

import logging
import os
from pathlib import PurePath
import sys

LOG = logging.getLogger(os.path.basename(__file__))


def core_paths():
    """Get main useful repo paths.

    Returns:
        list: [Repository Root Path, Palette Path]
    """
    # Repository path
    # start_path = PurePath(os.path.realpath(__file__))

    pure_repo_path = PurePath(
        get_parent_directory(PurePath(os.path.realpath(__file__)).as_posix(), 2)
    )
    # pure_repo_path = PurePath(repo_path)
    # dcc_path = f"{pure_repo_path.parents[0]}".replace("\\", "/")
    dcc_path = PurePath(get_parent_directory(pure_repo_path, 1), "DCC")
    # ue_path = f"{pure_repo_path.parents[1]}/UE".replace("\\", "/")
    ue_path = PurePath(get_parent_directory(pure_repo_path, 2), "UE")
    # cg_project_path = f"{dcc_path}/CG".replace("\\", "/")
    cg_project_path = PurePath(get_parent_directory(pure_repo_path, 1), "CG")

    # src_path = f"{repo_path}/src"
    # python_tools_path = f"{src_path}/tools"
    # core_path = f"{python_tools_path}/val_core"
    core_path = PurePath(pure_repo_path, "val_core")
    shared_icons_path = f"{core_path}/icons"
    # logs_directory = f"{src_path}/logs"
    logs_directory = PurePath(core_path, "logs")
    # configs_directory = f"{core_path}/config"
    configs_directory = PurePath(core_path, "config")
    project_configs_path = f"{dcc_path}/ProjectConfig/ProjectConfig.json"

    # repo_resources = f"{repo_path}/resources"
    # project_maya_banner = f"{repo_resources}/Banners/project_maya_banner.png"

    # Palette filepath
    palette_path = f"{core_path}/data/qpalette_maya2016.json"

    # Style sheet
    style_path = f"{core_path}/ui/Style/RoF_style_v002.css"

    # Enable access to boilerlib (Qt.py, mayapalette)
    if pure_repo_path not in sys.path:
        sys.path.append(pure_repo_path)

    paths_dict = {
        "root": pure_repo_path.as_posix(),
        "dcc": dcc_path,
        "ue": ue_path,
        "cg_path": cg_project_path,
        # "src": src_path,
        # "python_tools_path": python_tools_path,
        "core": core_path,
        "shared_icons": shared_icons_path,
        "logs": logs_directory,
        "configs": configs_directory,
        "projectConfigs": project_configs_path,
        "palette": palette_path,
        "stylesheet": style_path,
        # "database_paths": database_paths,
        # "repo_resources": repo_resources,
        # "project_maya_banner": project_maya_banner,
    }

    return paths_dict


def get_parent_directory(
    starting_path: str, level: int = 0, return_full_path: bool = True
) -> str:
    """Get parent directory at specific level above starting path.

    Args:
        starting_path (str): File or folder path start.
        level (int, optional): How many levels up to get parent. Defaults to 0.

    Returns:
        str: Path to directory above starting path.
    """
    current_path = PurePath(starting_path)
    if return_full_path:
        return str(current_path.parents[level]).replace("\\", "/")

    return str(current_path.parents[level]).rsplit("\\", maxsplit=1)[-1]


def get_module_paths(starting_path: str):
    current_path = PurePath(starting_path)

    LOG.info("parent: %s", current_path.parents[0])
    if not str(current_path.parents[0]).endswith("src"):
        LOG.warning(
            "File/Folder's parent folder isn't a module. Parent folder of provided "
            "path should be 'src'."
        )
        return None

    return 1


if __name__ == "__main__":
    paths = core_paths()
    for key_name, item_path in core_paths().items():
        sys.stdout.write(f"{key_name}: {item_path}\n")
