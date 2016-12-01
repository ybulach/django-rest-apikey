from django.core import validators

_error_message = 'Characters must match regex %s'

# Hexadecimal values (i.e. 123456789abcdef)
hexadecimal_regex = r'[a-fA-F0-9]+'
validate_hexadecimal = validators.RegexValidator('^%s$' % hexadecimal_regex, _error_message % hexadecimal_regex, 'invalid')
