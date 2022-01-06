from sorl.thumbnail import delete


def delete_images(sender, instance, **kwargs):
    """
    deletes the images from the directory
    """
    # logger.debug('Deleting image with data {} {} {}'.format(sender, instance, kwargs))
    if instance.image:
        # Delete the thumbnail image
        delete(instance.image)
        # Delete the image file from filesystem
        instance.image.delete(False)
