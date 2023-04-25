from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.users'
    verbose_name = _('Users')

# The UsersConfig class inherits from Django's AppConfig, which allows you to define app-specific settings.
# default_auto_field is an optional setting that defines the default primary key field type for your models in this app. 
# In this case, it's set to 'django.db.models.BigAutoField', which means new models in this app will use a 64-bit integer as the primary key field if you don't explicitly specify one.
# name is set to 'core_apps.users', which is the full Python path to the app. This is important because it tells Django the correct location of your users app within the core_apps directory.
# verbose_name is set to the translated string 'Users'. This is used as a human-readable name for the app when displayed in the Django admin interface or other places that need a more user-friendly name. 
# The gettext_lazy function allows for translation of the string if you plan to support multiple languages in your application.