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

	def _validate_token_owner(self, token_user: TokenUser = None) -> bool:
		if settings.MSB_JWT_VERIFY_OWNER:
			if self._request.ip in settings.MSB_JWT_TRUSTED_OWNERS:
				return True
			return f"{self._request.user_agent}@{self._request.ip}" == token_user.owner
		return True

	def _validate_subscription(self, token_user: TokenUser = None):
		if settings.MSB_JWT_VERIFY_SUBSCRIPTIONS:
			_request_path = self._request.path.strip("/").split('/')[0]
			return token_user.subscriptions.has_access(url=f"/{_request_path}")
		return False

	def authenticate(self, request):
		try:
			self._request = RequestWrapper(request=request)

			# authenticate the request from parent class
			if auth_result := super().authenticate(request=request):
				token_user: TokenUser = auth_result[0]

				# validate the token user properties
				token_user_is_valid = all([
					# check if the token_user is authenticated
					token_user.is_authenticated,

					# check if the token owner is valid
					self._validate_token_owner(token_user=token_user),

					# check if the user is subscribed to the service he is trying to access
					self._validate_subscription(token_user=token_user)
				])

				# update the token user properties
				token_user.set_validation_status(token_user_is_valid)

			# return the authentication result
			return auth_result
		except Exception as e:
			return None
