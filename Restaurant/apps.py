from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Restaurant'

    def ready(self):
        import Restaurant.Signals