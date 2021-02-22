from django.utils.translation import gettext_lazy as _
from drfpasswordless.models import CallbackToken
from drfpasswordless.serializers import TokenField
from drfpasswordless.settings import api_settings
from drfpasswordless.utils import validate_token_age, verify_user_alias
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


def token_age_validator(value):
    valid_token = validate_token_age(value)
    if not valid_token:
        raise serializers.ValidationError("The token you entered isn't valid.")
    return value


class AbstractBaseCallbackTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    confirmation_code = TokenField(min_length=6, max_length=6,
                                   validators=[token_age_validator])

    def validate_alias(self, attrs):
        email = attrs.get('email', None)

        if email:
            return 'email', email

        return None


class CallbackTokenAuthSerializer(AbstractBaseCallbackTokenSerializer):
    def validate(self, attrs):
        try:
            alias_type, alias = self.validate_alias(attrs)
            callback_token = attrs.get('confirmation_code', None)
            user = User.objects.get(**{alias_type + '__iexact': alias})
            token = CallbackToken.objects.get(**{'user': user,
                                                 'key': callback_token,
                                                 'type': CallbackToken.
                                              TOKEN_TYPE_AUTH,
                                                 'is_active': True})

            if token.user == user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                if api_settings.PASSWORDLESS_USER_MARK_EMAIL_VERIFIED:
                    user = User.objects.get(pk=token.user.pk)
                    success = verify_user_alias(user, token)
                    if success is False:
                        msg = _('Error validating user alias.')
                        raise serializers.ValidationError(msg)
                attrs['user'] = user
                return attrs
            else:
                msg = _('Invalid Token')
                raise serializers.ValidationError(msg)
        except CallbackToken.DoesNotExist:
            msg = _('Invalid alias parameters provided.')
            raise serializers.ValidationError(msg)
        except User.DoesNotExist:
            msg = _('Invalid user alias parameters provided.')
            raise serializers.ValidationError(msg)
        except ValidationError:
            msg = _('Invalid alias parameters provided.')
            raise serializers.ValidationError(msg)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
