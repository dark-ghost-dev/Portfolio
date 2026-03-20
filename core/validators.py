from django.core.exceptions import ValidationError

def validate_base_url(value):
    '''
    verifica si el input es una URL real
    '''
    value = value.strip()

    if value.startswith(('https://', 'mailto:', 'tel:')):
        return

    raise ValidationError(
        "La URL base debe iniciar con https://, mailto: o tel:"
    )