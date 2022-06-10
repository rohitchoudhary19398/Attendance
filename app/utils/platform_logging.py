"""
 /* Copyright (C) Magic Software Inc - All Rights Reserved
 * Proprietary and confidential.
 * Unauthorized copying of this file (full or in part), via any medium is strictly prohibited.
 * All code blocks in this file are subject to the terms and conditions defined
 * in the Master Services Agreement (MSA) and Statement of Work (SoW) between Magic Software Inc or its subsidiaries
 * and the "Client".
 */
"""

import logging
import logging.config as lcfg
from irecordpackages.config import Settings


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    return logger


def set_log_config(config: Settings):
    log_config = config.logConfig
    log_level = config.LOG_LEVEL
    loggers = log_config["loggers"].keys()
    lcfg.dictConfig(log_config)
    for logger_name in loggers:
        logger = get_logger(logger_name)
        logger.setLevel(log_level)


# logging object for tagging
logger = get_logger("irecord")
