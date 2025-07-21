import logging
from django.contrib.auth.backends import ModelBackend
from .models import User

logger = logging.getLogger(__name__)

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.warning("Trying to authenticate user: %s", username)

        try:
            # Try email or username
            user = User.objects.get(email=username) or User.objects.get(username=username)
        except User.DoesNotExist:
            logger.warning("User not found: %s", username)
            return None

        if user.check_password(password): # type: ignore
            logger.warning("Authentication successful for user: %s", username)
            return user
        else:
            logger.warning("Authentication failed for user: %s (wrong password)", username)
            return None