import inspect
import logging
import time
from typing import Any, Callable, TypeVar, cast

# With python 3.10 param spec can be used instead - as described here:
# https://stackoverflow.com/questions/66408662/type-annotations-for-decorators
F = TypeVar("F", bound=Callable[..., Any])


def log_execution_time(log_level: int = logging.INFO, logger_name: str = __name__) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        """This decorator logs the execution time of sync and async methods

        Args:
            func (F): The function that is decorated
            log_level (int, optional): The log level used for the log message. Defaults to logging.INFO.
            logger_name (str, optional): A logger used for the log message. Defaults to __name__.

        Returns:
            F: The return value of the original function
        """
        if inspect.iscoroutinefunction(func):

            async def wrapper_async(*args: Any, **kw: Any) -> Any:
                start_time = _get_current_time()
                result = await func(*args, **kw)  # types: ignore
                end_time = _get_current_time()
                _calculate_and_log_execution_time(start_time, end_time, logger_name, log_level, func.__name__)
                return result

            return cast(F, wrapper_async)

        else:

            def wrapper_sync(*args: Any, **kw: Any) -> Any:
                start_time = _get_current_time()
                result = func(*args, **kw)
                end_time = _get_current_time()
                _calculate_and_log_execution_time(start_time, end_time, logger_name, log_level, func.__name__)
                return result

            return cast(F, wrapper_sync)

    return decorator


def _get_current_time() -> int:
    return round(int(time.time() * 1000))


def _calculate_and_log_execution_time(
    start_time: int, end_time: int, logger_name: str, log_level: int, func_name: str
) -> None:
    execution_time = end_time - start_time

    extra_args = {"function_name": func_name, "execution_time": execution_time}

    time_logger = logging.getLogger(logger_name)
    time_logger.log(log_level, "%s took %s ms.", func_name, execution_time, extra=extra_args)
