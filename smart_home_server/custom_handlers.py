from rest_framework.views import exception_handler
from rest_framework.response import Response
import logging

logger = logging.getLogger('server_log')

def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first,
    # to get the standard error response.
    logger.error(f'Error: {exc}, Context: {context}')

    response = exception_handler(exc, context)

    if response is not None:
        # You can modify the response here if needed
        response.data['status_code'] = response.status_code
    else:
        # Here you can add handling for exceptions not already covered
        response = Response({'error': f'Unexpected error occurred - {exc}'}, status=500)



    return response