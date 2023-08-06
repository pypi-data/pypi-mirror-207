"""
Anastasia Logging Standarization

This package holds a logging implementation wrapper for python scripts with standarized code notifications and additional features.

How to use
----------

To use, you can simply replace
```
import logging
```
with
```
import anastasia_logging as logging
```
and log away, no additional changes are required if your scripts already has logging implemented!

You can use additional containerized loggers by calling AnastasiaLogger class

```
from anastasia_logging import AnastasiaLogger
logger = AnastasiaLogger()
```

"""

from typing import Optional
from .logger import AnastasiaLogger

# Equivalent to RootLogger from logging but doesn't override it
anastasia_logger = AnastasiaLogger()

def override_logging(based_on: Optional[AnastasiaLogger] = None) -> None:
    """
    Modify base root logging with Anastasia logging format

    Attributes
    ----------

    based_on : Optional[AnastasiaLogger], default=None
        Reply properties from existing AnastasiaLogger, if not declared then it will use default AnastasiaLogger properties

    """
    import logging
    filename = anastasia_logger.log_path
    save_log = anastasia_logger.save_log
    format = anastasia_logger.formatter._fmt
    datefmt = anastasia_logger.formatter.datefmt
    level = anastasia_logger.level
    if isinstance(based_on, AnastasiaLogger):
        filename = based_on.log_path
        save_log = anastasia_logger.save_log
        format = based_on.formatter.format
        datefmt = based_on.formatter.datefmt
        level = based_on.level

    if not save_log:
        filename = None

    logging.basicConfig(filename=filename, format=format, datefmt=datefmt, level=level)
    logging.info("Root logging modified with AnastasiaLogger structure")

def info(msg: Optional[str] = None, code: Optional[int] = None, save_log: bool = False, *args, **kwargs) -> Optional[str]:
    """
    Inherited from logging.info function with additional properties

    Attributes
    ----------

    msg : Optional[str], default=None
        Name identification of logger instance

    code : Optional[int], default=None
        Code assignation to add, if msg is not declared then it will search for default info codes

    save_log : bool, default=False
        Force to save log file, predefined with log_path attribute

    *args, **kwargs inherited from logging.info function

    Returns
    -------

    return_value : Optional[str]
        Log path where file was saved, none if save_log = False

    Notes
    -----

    Base codes standards:

    -   0 = Unindentified
    - 1XX = Data related
    - 2XX = Mathematical related
    - 3XX = AI related
    - 4XX = Resources related
    - 5XX = Operative System (OS) related
    - 6XX = API related
    - 7XX = AWS related

    """

    return_value = anastasia_logger.info(msg=msg, code=code, save_log=save_log, *args, **kwargs)

    return return_value

def warning(msg: Optional[str] = None, code: Optional[int] = None, save_log: bool = False, *args, **kwargs) -> Optional[str]:
    """
    Inherited from logging.warning function with additional properties

    Attributes
    ----------

    msg : Optional[str], default=None
        Name identification of logger instance

    code : Optional[int], default=None
        Code assignation to add, if msg is not declared then it will search for default warning codes

    save_log : bool, default=False
        Force to save log file, predefined with log_path attribute

    *args, **kwargs inherited from logging.warning function

    Returns
    -------

    return_value : Optional[str]
        Log path where file was saved, none if save_log = False

    Notes
    -----

    Base codes standards:

    -   0 = Unindentified
    - 1XX = Data related
    - 2XX = Mathematical related
    - 3XX = AI related
    - 4XX = Resources related
    - 5XX = Operative System (OS) related
    - 6XX = API related
    - 7XX = AWS related

    """

    return_value = anastasia_logger.warning(msg=msg, code=code, save_log=save_log, *args, **kwargs)

    return return_value

def error(msg: Optional[str] = None, code: Optional[int] = None, raise_type: Optional[type] = None, save_log: bool = False, *args, **kwargs) -> Optional[str]:
    """
    Inherited from logging.error function with additional properties

    Attributes
    ----------

    msg : Optional[str], default=None
        Name identification of logger instance

    code : Optional[int], default=None
        Code assignation to add, if msg is not declared then it will search for default error codes

    raise_type : Optional[type], default=None
        Raise any type with message content as text description and terminating python script execution, if None then no python type will be raised

    save_log : bool, default=False
        Force to save log file, predefined with log_path attribute

    *args, **kwargs inherited from logging.error function

    Returns
    -------

    return_value : Optional[str]
        Log path where file was saved, none if save_log = False

    Notes
    -----

    Base codes standards:

    -   0 = Unindentified
    - 1XX = Data related
    - 2XX = Mathematical related
    - 3XX = AI related
    - 4XX = Resources related
    - 5XX = Operative System (OS) related
    - 6XX = API related
    - 7XX = AWS related

    """

    return_value = anastasia_logger.error(msg=msg, code=code, raise_type=raise_type, save_log=save_log, *args, **kwargs)
    
    return return_value

