from django.apps import AppConfig


class HotelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Hotel'
    def ready(self):
        import Hotel.Signals
