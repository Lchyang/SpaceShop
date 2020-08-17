from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户'

    def ready(self):
        """Django Document.
        signal handlers are usually defined in a signals submodule of the application they relate to.
        Signal receivers are connected in the ready() method of your application configuration class.
        If you’re using the receiver() decorator, import the signals submodule inside ready().
        """
        import users.signals
