from django.apps import AppConfig


class UsersRegConfig(AppConfig):
    name = 'users_reg'

    def ready(self): # telling django to import signals we created and then use its functionality
        import users_reg.signals