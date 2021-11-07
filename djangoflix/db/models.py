from django.db import models

class PublishStateOptions(models.TextChoices):
        # Constant = DB_Value, user_display_va
        PUBLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
        # UNLISTED = 'UN', 'Unlisted'
        # Private = 'PR', 'Private'

