def smtp_filter_email_function(message):
    """
    A filter function for the smtp email...
    if return False the backend won't send this message via smtp.
    """
    return True
