import datetime as dt

from drfpasswordless.utils import validate_token_age
from rest_framework import serializers


def token_age_validator(value):
    valid_token = validate_token_age(value)
    if not valid_token:
        raise serializers.ValidationError("The token you entered isn't valid.")
    return value


def year_validator(value):
    if value > dt.datetime.now().year:
        raise serializers.ValidationError(
            'It is not a correcrt year.'
        )
