from slugify import slugify


def unicode_slugify(name):
    """
    Makes a slug from a given string
    :param name: any string
    :return: slug from that string
    """
    return slugify(name.lower().strip())
