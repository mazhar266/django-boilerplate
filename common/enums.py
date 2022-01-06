from django.db import models

class StatusTypes(models.IntegerChoices):
    ACTIVE = 1
    INACTIVE = 2
    DELETED = 3
    DRAFTED = 4
    PUBLISHED = 5
    BANNED = 6
    SUSPENDER = 7
