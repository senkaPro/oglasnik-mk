from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings



class DualAuthentication(ModelBackend):

    def authenticate(self,username=None,password=None):
        UserModel = get_user_model()
        try:
            if True:
                kwargs = {'email': username}
            else:
                kwargs = {'email__iexact': username}
            user = UserModel.objects.get(**kwargs)
        except:
            if True:
                kwargs = {'username': username}
            else:
                kwargs = {'username__iexact': username}
            user = UserModel.objects.get(**kwargs)
        finally:
            try:
                if user.check_password(password):
                    return user
            except:
                return None


    def get_user(self,username):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=username)
        except UserModel.DoesNotExist():
            return None
        return user if self.user_can_authenticate(user) else None
