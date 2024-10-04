"""Set up logging levels and basic configurations."""

from datetime import datetime
import logging
import logging.config
import os
import time

from ..paths import core_paths
from ..util import file_util_tools


CONFIG_DIR = f"{core_paths.core_paths()['configs'].as_posix()}"
LOG_DIR = f"{core_paths.core_paths()['logs'].as_posix()}"


def setup_logging(current_env="dev"):
    """Load logging configuration"""
    log_configs = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}

    config_path = "/".join([CONFIG_DIR, log_configs[current_env]])

    # Make sure logs folder exists
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    timestamp = datetime.now().strftime("%Y%m%d")

    logging.debug("Config path being loaded: %s", config_path)

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
    )
    logging.info("Current environment: %s", current_env)


def cleanup_logs():
    for log_file in file_util_tools.get_files_or_folders(LOG_DIR, True, True):
        if is_file_older_than(log_file):
            os.remove(log_file)


def is_file_older_than(file_path, days_old: int = 7):
    # Get the current time in seconds
    current_time = time.time()

    # Get the modification time of the file
    file_mod_time = os.path.getmtime(file_path)

    # Convert days to seconds
    seven_days_in_seconds = days_old * 24 * 60 * 60

    # Compare the current time with the file's modification time
    return (current_time - file_mod_time) > seven_days_in_seconds


if __name__ == "__main__":
    setup_logging()
