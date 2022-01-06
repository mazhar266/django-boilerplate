from django.db import models

class GenderTypes(models.IntegerChoices):
    MALE = 1
    FEMALE = 2
    EUNUCH = 3
    UNKNOWN = 4
