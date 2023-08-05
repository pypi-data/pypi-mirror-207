from rest_framework.permissions import BasePermission
from msb_auth.users import TokenUser
from .constants import AUTH_TOKEN_ACCESS_TYPE_ISR

class MsbPermisson(BasePermission):

	def has_permission(self, request, view):
		return True

	def has_object_permission(self, request, view, obj):
		return True


class LoginRequiredPermission(MsbPermisson):

	def has_permission(self, request, view):
		return bool(request.user and request.user.is_authenticated)


class AdminUserPermission(MsbPermisson):
	def has_permission(self, request, view):
		return bool(request.user and request.user.is_staff)


class IntraServiceRequest(LoginRequiredPermission):

	def has_permission(self, request, view):
		_user: TokenUser = request.user
		if _user.access_type == AUTH_TOKEN_ACCESS_TYPE_ISR:
			return True
		return False

