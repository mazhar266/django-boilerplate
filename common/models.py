import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField

from .enums import StatusTypes


class BaseModel(models.Model):
    alias = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        unique=True
    )
    status = models.IntegerField(
        choices=StatusTypes.choices,
        default=StatusTypes.ACTIVE,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class NameBaseModel(BaseModel):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(
        populate_from='name',
        always_update=True,
        unique=True,
        allow_unicode=True
    )

    class Meta:
        abstract = True
        ordering = ('-created_at',)
