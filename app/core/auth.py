import os
from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
import firebase_admin
from firebase_admin import credentials, auth
from dotenv import load_dotenv
from starlette.requests import Request
from starlette.responses import JSONResponse

load_dotenv()

cred = credentials.Certificate(os.getenv("FIREBASE_ADMIN_SERVICE_ACCOUNT"))
app = firebase_admin.initialize_app(cred)

class AuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if conn.scope['type'] == 'websocket':
            return
            # id_token = self._authenticate_websocket(conn)
        else:
            if "Authorization" not in conn.headers:
                return
            id_token = conn.headers["Authorization"]
        try:
            user = auth.verify_id_token(id_token)
            return AuthCredentials(["authenticated"]), user['uid']
        except Exception:
            raise AuthenticationError("Invalid authorization token")

    def _authenticate_websocket(self, conn) -> str:
        try:
            return conn.query_params['Authorization']
        except KeyError:
            raise AuthenticationError("Missing query parameters")
        
def on_auth_error(request: Request, exc: Exception):
    return JSONResponse({"error": str(exc)}, status_code=401)

auth_middleware = [
    Middleware(AuthenticationMiddleware, backend=AuthBackend(), on_error=on_auth_error)
]
