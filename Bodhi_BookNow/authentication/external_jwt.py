import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExternalJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("ExternalJWTAuthentication ")
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]
        print(token)

        try:
            # ✅ This is Step 3:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")

        user_id = payload.get("user_id")
        if not user_id:
            raise AuthenticationFailed("Invalid token payload")

        return (SimpleUser(user_id), None)


class SimpleUser:
    def __init__(self, user_id):
        self.id = user_id
        self.is_authenticated = True
