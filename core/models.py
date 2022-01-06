import logging
logger = logging.getLogger(__name__)

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_delete
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel, NameBaseModel
from common.fields import TimestampImageField
from common.mixins import ImageMixin

from .enums import GenderTypes
from .managers import UserManager
from .signals import delete_images


class User(AbstractBaseUser, PermissionsMixin, NameBaseModel, ImageMixin):
    """
    A custom User model

    A fully featured User model with admin-compliant permissions that uses
    a full-length contact_no field as the username.

    Contact No and password are required. Other fields are optional.

    A more descriptive tutorial can be found here
    http://www.caktusgroup.com/blog/2013/08/07/migrating-custom-user-model-django/
    """
    mobile = models.CharField(db_index=True, unique=True, max_length=30)
    email = models.CharField(max_length=200)

    dob = models.DateField(null=True, blank=True)
    gender = models.IntegerField(
        choices=GenderTypes.choices,
        default=GenderTypes.UNKNOWN
    )

    image = TimestampImageField(
        upload_to='profiles',
        blank=True,
        null=True
    )
    
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Whether this user should be treated as active. Unselect\
             this instead of deleting accounts.'))
    is_email_active = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    # REQUIRED_FIELDS = (,)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return u"Mobile: {}".format(self.mobile)

    def get_full_name(self):
        """ Returns the full name """
        name = u"{}".format(self.name)
        return name.strip()

    def get_short_name(self):
        return u"{}".format(self.mobile)

    def __str__(self):
        return self.get_full_name()


post_delete.connect(delete_images, sender=User)
