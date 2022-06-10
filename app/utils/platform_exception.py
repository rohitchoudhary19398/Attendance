"""
 /* Copyright (C) Magic Software Inc - All Rights Reserved
 * Proprietary and confidential.
 * Unauthorized copying of this file (full or in part), via any medium is strictly prohibited.
 * All code blocks in this file are subject to the terms and conditions defined
 * in the Master Services Agreement (MSA) and Statement of Work (SoW) between Magic Software Inc or its subsidiaries and the "Client".
 */
"""


class PlatformException(Exception):
    """Custom Exception"""

    def __init__(self, original_exception, custom_message):
        super(PlatformException, self).__init__(
            f"{custom_message}:\n{original_exception}"
        )
        self.original_exception = original_exception
        self.custom_message = custom_message
