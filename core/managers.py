# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

from time import time

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, mobile, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given mobile and password.
        """
        now = timezone.now()
        if not mobile:
            raise ValueError('The given contact no must be set')
        
        user = self.model(
            mobile=mobile,
            email='test{}@test.com'.format(time()),
            name='Test {}'.format(time()),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile, password=None, **extra_fields):
        return self._create_user(mobile, password, False, False, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        return self._create_user(mobile, password, True, True, **extra_fields)
