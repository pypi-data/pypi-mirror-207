# -*- coding: utf-8 -*-
import datetime
import os
import traceback

# A class that provides logging functionality


class Logger:

    # A dictionary to map logging levels to integers
    level_list = {
        'none': 99,
        'error': 40,
        'warning': 30,
        'warn': 30,
        'info': 20,
        'debug': 10,
        'verbose': 5,
        'verb': 5,
    }

    # A dictionary to map integers to logging level strings
    level_str_list = {
        5: 'VERB',
        10: 'DEBUG',
        20: 'INFO',
        30: 'WARN',
        40: 'ERROR'
    }

    # Logger information and configuration
    log_info = {
        'prev_remove': False,
        'out_console': True,
        'out_file': True,
        'log_level': 'debug',
        'dir_name': './log',
        'log_file': 'Logger.log',
        'log_path': '',
    }

    log_level = level_list['info']

    # Initialize the logger with the specified log level, file name, and log removal option
    def init(log_level='verbose', dir_name='./log', file_name='Logger.log', prev_log_remove=False, out_console=True, out_file=True):
        """
        Initialize the logger with the specified log level, directory name, file name, and log removal option.

        :param log_level: The log level to set (debug, info, warning, or error). Default is 'debug'.
        :param dir_name: The directory name to use for log files. Default is './log'.
        :param file_name: The file name to use for logging. Default is None, which will create a file named "Logger.log".
        :param prev_log_remove: Whether to remove the existing log file on initialization. Default is False.
        :param out_console: Whether to output log messages to the console. Default is True.
        :param out_file: Whether to output log messages to a file. Default is True.
        """
        Logger.set_log_level(log_level)
        Logger.log_info['prev_remove'] = prev_log_remove
        Logger.log_info['log_level'] = log_level
        Logger.log_info['out_console'] = out_console
        Logger.log_info['out_file'] = out_file
        if dir_name:
            Logger.log_info['log_dir'] = dir_name
        else:
            Logger.log_info['log_dir'] = ''
        Logger.log_info['log_file'] = file_name
        Logger.log_info['log_path'] = Logger.log_info['log_dir'] + \
            "/" + Logger.log_info['log_file']
        if Logger.log_info['prev_remove']:
            Logger.log_remove()

    # Set the logging level
    @staticmethod
    def set_log_level(log_level: str):
        """
        :param log_level: the log level to set (debug, info, warning, or error)
        """
        Logger.log_level = Logger.level_list[log_level]

    # Get the current date and time
    @staticmethod
    def get_datetime() -> str:
        """
        :return: the current date and time in a formatted string
        """
        now = datetime.datetime.now()
        return now.strftime("[%Y/%m/%d %H:%M:%S]")

    # Remove the log file if the option is enabled
    @staticmethod
    def log_remove():
        """
        Remove the log file if the log_remove option is enabled
        """
        if Logger.log_info['prev_remove']:
            if os.path.exists(Logger.log_info['log_path']):
                os.remove(Logger.log_info['log_path'])

    # Print a log message
    def log_print(tag, message, level, exc_info=None):
        """
        Print a log message

        :param tag: The tag to add to the log message
        :param message: The message to log
        :param level: The log level of the message (1-4, with 1 being the most verbose and 4 being the least verbose)
        :param exc_info: Optional traceback information
        """
        if level >= Logger.log_level:
            log_p = f'{Logger.get_datetime()}[{Logger.level_str_list[level]}][{tag}]{message}'
            log_f = f'{Logger.get_datetime()}[{Logger.level_str_list[level]}][{tag}]{message}\n'
            if exc_info:
                traceback_str = "".join(traceback.format_exception(*exc_info))
                log_p += "\n" + traceback_str
                log_f += traceback_str
            if Logger.log_info['out_console']:
                print(log_p)
            if Logger.log_info['out_file']:
                new_dir_path = Logger.log_info['log_dir'] + "/"
                if not os.path.exists(new_dir_path):
                    os.makedirs(new_dir_path)
                if Logger.log_info['out_file']:
                    with open(new_dir_path + Logger.log_info['log_file'], mode="a") as file:
                        file.write(log_f)

    # Log a verbose message
    @staticmethod
    def verbose(tag: str, message: str = "") -> None:
        """
        Logs a debug message.

        :param tag: The tag to use for the log message.
        :param message: The message to log.
        """
        Logger.log_print(tag, message, 5)

    # Log a verbose message
    @staticmethod
    def verb(tag: str, message: str = "") -> None:
        """
        Logs a debug message.

        :param tag: The tag to use for the log message.
        :param message: The message to log.
        """
        Logger.log_print(tag, message, 5)

    # Log a debug message
    @staticmethod
    def debug(tag: str, message: str = "") -> None:
        """
        Logs a debug message.

        :param tag: The tag to use for the log message.
        :param message: The message to log.
        """
        Logger.log_print(tag, message, 10)

    # Log an info message
    @staticmethod
    def info(tag: str, message: str = "") -> None:
        """
        Logs an info message.

        :param tag: The tag to use for the log message.
        :param message: The message to log.
        """
        Logger.log_print(tag, message, 20)

    # Log a warning message
    @staticmethod
    def warning(tag: str, message: str = "") -> None:
        """
        Logs a warning message.

        :param tag: The tag to use for the log message.
        :param message: The message to log.
        """
        Logger.log_print(tag, message, 30)

    # Log a warning message (alias for warning)
    @staticmethod
    def warn(tag: str, message: str = "") -> None:
        """
        Logs a warning message (alias for warning).

        :param tag: The tag to use for the log message.
        :param message: The message to log.
        """
        Logger.log_print(tag, message, 30)

    # Log an error message
    def error(tag: str, message: str = "", exc_info: tuple[None, None, None] = None) -> None:
        """
        Logs an error message.

        :param tag: The tag to use for the log message.
        :param message: The message to log.
        :param exc_info: The exception information to log.
        """
        Logger.log_print(tag, message, 40, exc_info)
