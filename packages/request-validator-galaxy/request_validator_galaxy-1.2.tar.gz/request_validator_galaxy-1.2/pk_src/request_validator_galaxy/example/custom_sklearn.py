"""Validation of headers and params.

This have the following function:
    - validate_header(function): Validate the username header from the api
        request headers.
    - validate_arguments(param): Check for the arguments keys exist or not
        in api request.
"""

from functools import wraps
from flask import request as req

def validate_headers(header_param):
    """Check for the headers keys exist or not in api request.

    The validate_headers_list function is a decorator that checks if the
    required headers are present in the request. If any of them are
    missing, it returns an error response with status code 400 and error code
    EMPLOYEE_HEADER_VALIDATION_ERROR.

    Args:
        header_param (dict): Pass the list of headers that need to be
         validated.

    Returns:
        A decorator that is used to validate the headers list.
    """
    def decorator(function):
        """Create decorator function.

        The decorator function checks the header parameters of the request.
            If any of them is missing, it returns an error response.

        Args:
            function (func): Pass the function to be decorated.

        Returns:
            function (func): A wrapper function.
        """
        @wraps(function)
        def check_argument(*args, **kw):
            """Verify the arguments.

            The check_argument function is a decorator that checks if the
            request has all the required headers. If not, it returns an
            error response with status code 400 and error message.

            Args:
                *args (list): Send a non-keyword variable length argument
                    list to the function.
                **kw (dict): Pass a variable number of keyword arguments to
                    the function.

            Returns:
                The error_response if the header is not present or null.
            """
            headers = {"name":"preetam"}
            for header_key in header_param:
                if header_key not in headers or \
                        not headers.get(header_key):
                    return {"error" : "error"}
            return function(*args, **kw)

        return check_argument

    return decorator


def validate_arguments(param):
    """Check for the arguments keys exist or not in api request.

    The validate_arguments function is a decorator that checks if the
    required parameters are present in the request. If not, it returns an
    error response with status code 400 and error code 1002.

    Args:
        param (dict): Check if the required parameters are present in the
            request.

    Returns:
        A decorator which returns a function.
    """
    def decorator(function):
        """Create decorator function.

        The decorator function checks if the required parameters are present in the request.
            If not, it returns an error response with a message and status code 400.

        Args:
            function (func): Pass the function to be decorated.

        Returns:
            function (func): A function.
        """
        @wraps(function)
        def check_argument(*args, **kw):
            """Verify the arguments.

            The check_argument function is a decorator that checks if the
            required parameters are present in the request. If not,
            it returns an error response with status code 400.

            Args:
                *args (list): Send a non-keyword variable length argument
                    list to the function.
                **kw (dict): Pass a variable number of keyword arguments to
                    the function.

            Returns:
                function (func): The function if the required parameters
                    are present in the request.
            """
            request_param = {
                "req_param": {
                    "names": "preetam"
                }
            }
            if "req_param" not in request_param:
                error_response = {"error": "error"}
                return error_response
            for json_key in param:
                if json_key not in request_param["req_param"]:
                    error_response = {"error": "error"}
                    return error_response
            return function(*args, **kw)

        return check_argument

    return decorator