from django.utils.translation import gettext_lazy as _
from rest_framework.fields import CharField
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer, TokenVerifySerializer)

from .constants import (TokenFieldNames as _tfn, AUTH_REQUEST_TYPE_FIELD_NAME, AUTH_REQUEST_USER_FIELD_NAME)
from .users import TokenUser
from msb_cipher import Cipher


class MsbJwtTokenObtainSerializer(TokenObtainPairSerializer):
	"""Customizes JWT default Serializer to add more information about user"""
	username_field = AUTH_REQUEST_USER_FIELD_NAME
	default_error_messages = {
		'no_active_account': _('User Authentication Failed.')
	}

	def __init__(self, *args, **kwargs):
		super(MsbJwtTokenObtainSerializer, self).__init__(*args, **kwargs)
		self.fields[AUTH_REQUEST_TYPE_FIELD_NAME] = CharField(required=True)
		self.fields[AUTH_REQUEST_USER_FIELD_NAME] = CharField(required=True)

	@classmethod
	def format_token_data(cls, token_data, user: TokenUser):
		return token_data

	@classmethod
	def get_token(cls, user: TokenUser = None):
		try:
			token_data = super().get_token(user)
			token_data[_tfn.ID] = user.token.get(_tfn.USER_ID)
			token_data[_tfn.IP] = user.token.get(_tfn.IP)
			token_data[_tfn.IS_VALID] = user.token.get(_tfn.IS_VALID)
			token_data[_tfn.SESSION] = user.token.get(_tfn.SESSION).to_json()
			token_data[_tfn.OWNER] = Cipher.encrypt(f"{user.token.get(_tfn.OWNER)}@{user.token.get(_tfn.IP)}")
			token_data[_tfn.ACCESS_TYPE] = Cipher.encrypt(user.token.get(_tfn.ACCESS_TYPE))

			return cls.format_token_data(token_data, user)
		except Exception as e:
			return None


class MsbJwtTokenVerifySerializer(TokenVerifySerializer):
	pass
