from django.conf import settings
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from msb_auth.users import TokenUser
from msb_http import RequestWrapper


class JwtTokenValidator(JWTTokenUserAuthentication):
	"""
	This class overrides the "JWTTokenUserAuthentication", so that we can implement
	custom authentication rules over the default system

	"""

	_request: RequestWrapper = None

	def _validate_token_owner(self, token: TokenUser = None):
		if getattr(settings, "MSB_JWT_VERIFY_OWNER", False):
			if self._request.ip in getattr(settings, "MSB_JWT_TRUSTED_OWNERS", []):
				return True
			return f"{self._request.user_agent}@{self._request.ip}" == token.owner
		return True

	def _validate_token_integrity(self, token: TokenUser = None) -> bool:
		_validation_status = [
			token.is_authenticated,
			self._validate_token_owner(token=token)
		]
		return all(_validation_status)

	def authenticate(self, request):
		try:
			self._request = RequestWrapper(request=request)
			auth_result = super(JWTTokenUserAuthentication, self).authenticate(request=request)
			if auth_result:
				token_user: TokenUser = auth_result[0]
				token_is_valid = self._validate_token_integrity(token=token_user)
				token_user.set_validation_status(token_is_valid)
			return auth_result
		except Exception as e:
			return None
