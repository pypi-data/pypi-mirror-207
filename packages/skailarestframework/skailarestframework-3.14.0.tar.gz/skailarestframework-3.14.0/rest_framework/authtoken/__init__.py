import skailar

if skailar.VERSION < (3, 2):
    default_app_config = 'rest_framework.authtoken.apps.AuthTokenConfig'
