def pos_error_formatter(response):
    error_code = response['error']
    error_message = response['error_message']

    form_errors = response.get('form_errors')

    formatted_message = f""" Error Code: {error_code}
    Error Message: {error_message}
    """

    if form_errors:
        formatted_message = "".join((formatted_message, f"Form Errors: {form_errors}", "\n"))

    return formatted_message


res_with_form_errors = {
    'result': 'ERROR',
    'error': 700,
    'error_message': 'Error in form',
    'form_errors': {
        'payment_id': ['This field is required.'],
        'trx_id': ['This field is required.'],
        'tid': ['This field is required.'],
        'amount': ['This field is required.']
    }
}

res_without_form_errors = {
    'result': 'ERROR',
    'error': 700,
    'error_message': 'Error in form'
}

print(pos_error_formatter(res_with_form_errors))
print(pos_error_formatter(res_without_form_errors))
print(pos_error_formatter(res_without_form_errors))
