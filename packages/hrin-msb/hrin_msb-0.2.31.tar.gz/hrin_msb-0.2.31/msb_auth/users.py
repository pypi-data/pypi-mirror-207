from .token import AuthToken
from django.utils.functional import cached_property


class TokenUser(AuthToken):

	@cached_property
	def username(self):
		return self.session.get('username', None)

	@property
	def is_authenticated(self):
		return self.session.get('is_authenticated', False) and self.is_valid

	@cached_property
	def is_admin(self):
		return self.session.get("is_admin") == True

	@cached_property
	def auth_type(self):
		return self.session.get('auth_type')

	@property
	def email(self):
		return self.session.get(self._user_email_field)
