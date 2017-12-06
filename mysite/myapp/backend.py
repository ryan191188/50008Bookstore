from django.contrib.auth import get_user_model


class UserAuthBackend(object):
    """
    User Authentication Backend
    """

    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = get_user_model().objects.get(login=username)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None 