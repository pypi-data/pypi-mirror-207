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

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

# Equivalent to RootLogger from logging but doesn't override it
anastasia_logger = AnastasiaLogger()

def basicConfig(filename: str=None, filemode: str = None, format: str=None, datefmt: str=None, level: int=None, handlers=None, **kwargs) -> None:
    """
    Do basic configuration for Anastasia logging system, similar to logging base root function.

    Attributes
    ----------

    filename : Optional[str]
        Specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler.

    filemode : Optional[str]
        Specifies the mode to open the file, if filename is specified (if filemode is unspecified, it defaults to 'a').

    format : Optional[str]
        Use the specified format string for the handler.

    datefmt : Optional[str]
        Use the specified date/time format.

    level : Optional[str]
        Set the root logger level to the specified level.

    handlers : Iterable[Handlers]
        If specified, this should be an iterable of already created handlers, which will be added to the root handler.
        Any handler in the list which does not have a formatter assigned will be assigned the formatter created in this function.

    """
    from logging import Formatter, FileHandler, StreamHandler

    if isinstance(filemode, type(None)):
        filemode = 'a'
    if isinstance(format, type(None)):
        format = anastasia_logger.formatter._fmt
    if isinstance(datefmt, type(None)):
        datefmt = anastasia_logger.formatter.datefmt
    if isinstance(level, type(None)):
        level = anastasia_logger.level
    if isinstance(handlers, type(None)):
        handlers = []

    while anastasia_logger.hasHandlers():
        anastasia_logger.removeHandler(anastasia_logger.handlers[0])
    
    fmt = Formatter(format, datefmt)
    anastasia_logger.setLevel(level)

    if not handlers:
        if filename:
            h = FileHandler(filename, filemode)
        else:
            h = StreamHandler()
        handlers = [h]

    for h in handlers:
        if h.formatter is None:
            h.setFormatter(fmt)
        anastasia_logger.addHandler(h)
    

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

