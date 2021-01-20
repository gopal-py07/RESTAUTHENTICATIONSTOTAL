from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentictionTwo(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        key = request.GET.get('key')
        if username is None or key is None:
            return None
        c1 = len(key) == 7
        c2 = key[0] == username[-1].lower()
        c3 = key[2] == 'Z'
        c4 = key[4] == username[0]

        try:
            user = User.objects.get(username=username)
        except user.DoesNotExist:
            raise AuthenticationFailed('username invalid,provide valid one')
        if c1 and c2 and c3 and c4:
            return (user,None)
            raise AuthenticationFailed('key is invalid,plz provid valid key')
