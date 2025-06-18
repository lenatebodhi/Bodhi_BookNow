from django.apps import AppConfig


class BookNowConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "book_now"

    def ready(self):
        print("check booking ready")
        import book_now.signals
