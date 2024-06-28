# from typing import Optional

# from marshmallow.exceptions import ValidationError
# from werkzeug.exceptions import HTTPException

# from controller.blueprint import api
# from model.common_response import CommonResponse


# class ErrorResponseFormatter:
#     @staticmethod
#     def format_error_response(
#         field_errors: Optional[str] = None, global_errors: Optional[str] = None
#     ):  # noqa: E501
#         errors = {"fields": field_errors, "global": global_errors}
#         response = CommonResponse(status="ERROR", result=None, errors=errors)
#         print(response)
#         return response.__dict__


# @api.errorhandler(HTTPException)   
# def handle_root_exception(error):  
#     custom_response = ErrorResponseFormatter.format_error_response(
#         global_errors=[error.description]   # type: ignore
#     )   # noqa: E501
#     return custom_response, error.code  


# @api.errorhandler(ValidationError)  
# def handle_validation_error(error):  
#     errors = error.normalized_messages()  
#     merged_errors = [
#         f"{field}: {', '.join(messages) if isinstance(messages, list) else messages}"  
#         for field, messages in errors.items()  
#     ]    # noqa: E501
#     custom_response = ErrorResponseFormatter.format_error_response(
#         field_errors=merged_errors   # type: ignore
#     )  # noqa: E501 
#     # next line is added due to a bug in library https://github.com/noirbizarre/flask-restplus/issues/530
#     error.data = custom_response
#     return custom_response, 403  

# @api.errorhandler(ValueError)  
# def handle_custom_exception(error):  
#     custom_response = ErrorResponseFormatter.format_error_response(
#         global_errors=[str(error)]   # type: ignore
#     )   # noqa: E501
#     return custom_response, 400

