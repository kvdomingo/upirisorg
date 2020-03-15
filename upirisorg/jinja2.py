from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from datetime import datetime


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'now': datetime.now(),
        'nav_items': [
            'Home',
            'About',
            'Members',
            'Alumni',
            'Gallery',
            'Contact',
        ]
    })
    return env
