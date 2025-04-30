import logging
import sys
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
    logger.setLevel(logging.INFO)
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger