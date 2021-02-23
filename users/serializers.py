from drfpasswordless.models import CallbackToken
from drfpasswordless.serializers import TokenField
from drfpasswordless.settings import api_settings
from drfpasswordless.utils import verify_user_alias
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from .validators import token_age_validator


class AbstractBaseCallbackTokenSerializer(serializers.Serializer):
    """
    Abstract class inspired by DRF's own token serializer.
    Returns a user if valid, None or a message if not.
    """

    email = serializers.EmailField(
        required=False)  # Needs to be required=false to require both.
    confirmation_code = TokenField(min_length=6, max_length=6,
                                   validators=[token_age_validator])

    def validate_alias(self, attrs):
        email = attrs.get('email')

        if email:
            return 'email', email

        return None


class CallbackTokenAuthSerializer(AbstractBaseCallbackTokenSerializer):

    def validate(self, attrs):
        # Check Aliases
        try:
            alias_type, alias = self.validate_alias(attrs)
            callback_token = attrs.get('confirmation_code')
            user = User.objects.get(**{alias_type + '__iexact': alias})
            token = CallbackToken.objects.get(**{'user': user,
                                                 'key': callback_token,
                                                 'type': CallbackToken.
                                              TOKEN_TYPE_AUTH,
                                                 'is_active': True})

            if token.user == user:
                # Check the token type for our uni-auth method.
                # authenticates and checks the expiry of the callback token.
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                if api_settings.PASSWORDLESS_USER_MARK_EMAIL_VERIFIED:
                    # Mark this alias as verified
                    user = User.objects.get(pk=token.user.pk)
                    success = verify_user_alias(user, token)

                    if not success:
                        msg = 'Error validating user alias.'
                        raise serializers.ValidationError(msg)

                attrs['user'] = user
                return attrs

            else:
                msg = 'Invalid Token'
                raise serializers.ValidationError(msg)
        except CallbackToken.DoesNotExist:
            msg = 'Invalid alias parameters provided.'
            raise serializers.ValidationError(msg)
        except User.DoesNotExist:
            msg = 'Invalid user alias parameters provided.'
            raise serializers.ValidationError(msg)
        except ValidationError:
            msg = 'Invalid alias parameters provided.'
            raise serializers.ValidationError(msg)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
