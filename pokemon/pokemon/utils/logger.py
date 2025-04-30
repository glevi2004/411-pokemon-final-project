import logging
import sys
from flask import current_app, has_request_context
from typing import Optional

def configure_logger(logger: Optional[logging.Logger] = None) -> logging.Logger:
    """Configure the application logger.
    
    Args:
        logger (Optional[logging.Logger]): The logger to configure. If None, creates a new one.
        
    Returns:
        logging.Logger: The configured logger
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    # Set log level
    logger.setLevel(logging.DEBUG)  # Set the desired logging level here

    # Create a console handler that logs to stderr
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.DEBUG)

    # Create a formatter with a timestamp
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add the formatter to the handler
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # If Flask request context exists, integrate with current_app.logger
    if has_request_context():
        app_logger = current_app.logger
        for app_handler in app_logger.handlers:
            logger.addHandler(app_handler)

    return logger