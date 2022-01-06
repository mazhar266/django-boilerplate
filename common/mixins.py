import logging
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count

from django.conf import settings
from sorl.thumbnail import get_thumbnail

logger = logging.getLogger(__name__)

from projectile.settings import (
    THUMB_QUALITY,
    THUMB_SMALL,
    THUMB_MEDIUM,
    THUMB_LARGE,
)


class ImageMixin(object):
    """Adds a few thumb helpers for models with a single image field named image"""

    DEFAULT_IMAGE_PATH = {
        THUMB_SMALL: u"{}images/placeholders/image_{}.png".format(
            settings.STATIC_URL, THUMB_SMALL
        ),
        THUMB_MEDIUM: u"{}images/placeholders/image_{}.png".format(
            settings.STATIC_URL, THUMB_MEDIUM
        ),
        THUMB_LARGE: u"{}images/placeholders/image_{}.png".format(
            settings.STATIC_URL, THUMB_LARGE
        )
    }

    VALID_LITERAL_SIZES = [
        'small',
        'medium',
        'large',
    ]

    def create_thumbnails(self):
        pool = ThreadPool(cpu_count())
        result = pool.map_async(
            lambda size: getattr(self, 'get_thumb_{}'.format(size))(),
            self.VALID_LITERAL_SIZES
        )
        result.wait()
        # pool.terminate()

    def get_thumb(self, size=THUMB_SMALL, quality=THUMB_QUALITY):
        # Validate size to avoid unnecessary caching
        if size not in self.DEFAULT_IMAGE_PATH.keys():
            size = THUMB_SMALL

        try:
            if not self.image:
                return self.DEFAULT_IMAGE_PATH.get(size)
            else:
                path = self.image.path
                thumb = get_thumbnail(
                    path, size, crop='center', quality=quality
                )
                return thumb.url
        except Exception as error:  # pylint: disable=broad-except
            # Returns default placeholder if error occurs
            logger.warning(error)
            logger.warning(
                'Could not get thumbnail for <User: {}> with <Image: {}>'.format(
                    self,
                    self.image.path
                )
            )
            return self.DEFAULT_IMAGE_PATH.get(size)

    def get_thumb_small(self):
        return self.get_thumb(size=THUMB_SMALL)

    def get_thumb_medium(self):
        return self.get_thumb(size=THUMB_MEDIUM)

    def get_thumb_large(self):
        return self.get_thumb(size=THUMB_LARGE)
