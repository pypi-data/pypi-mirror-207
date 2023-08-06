# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_bunny']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.0.0', 'python-dateutil>=2.8.2,<3.0.0', 'requests>=2.30.0,<3.0.0']

setup_kwargs = {
    'name': 'django-bunny',
    'version': '1.0.21',
    'description': 'A django storage for bunny.net',
    'long_description': '# django-bunny\n\nA bunny.net storage for Django. It was created as a replacement for [django-bunny-storage](https://github.com/willmeyers/django-bunny-storage).\n\n\n## Installation\n\nYou can install the library using `pip`:\n\n```bash\npip install django-bunny\n```\n\n\n## Configuration\n\nFirst, add `django_bunny` to your `INSTALLED_APPS`:\n\n```py\nINSTALLED_APPS = [\n    ...,\n    "django_bunny",\n    ...\n]\n```\n\nNow, create the following variables inside your `settings.py` file. These are required if you are using Django < `4.2`. Otherwise, you can use `OPTIONS` in the `STORAGES` setting.\n\n```py\n# These can be found in your storage\'s dashboard under `FTP & API Access`\nBUNNY_USERNAME = "my-storage-name"\nBUNNY_PASSWORD = "my-storage-password"\n\n# This is the storage region\'s code. E.g. Los Angeles is `la`, Singapore is\n# `sg`, etc. The default is `ny` (New York).\nBUNNY_REGION = "my-storage-region"\n\n# Optional. For example, `https://myzone.b-cdn.net/`. `MEDIA_URL` will be used\n# if this is not set.\nBUNNY_HOSTNAME = "my-pullzone-hostname"\n```\n\nFinally, depending on which version of Django you are using you\'ll need to create one of these variables:\n\n```py\n# Django < 4.2\nDEFAULT_FILE_STORAGE = \'django_bunny.storage.BunnyStorage\'\n\n# Django >= 4.2. Set `BunnyStorage` where you want to use bunny.net\'s storage.\n{\n    "default": {\n        "BACKEND": "django_bunny.storage.BunnyStorage",\n\n        # Add this if you did not create the BUNNY_* settings before. They are\n        # the same as BUNNY_* variables.\n        "OPTIONS": {\n            "username": "my-storage-name",\n            "password": "my-storage-password",\n            \n            # Optional. Defaults to `ny`\n            "region": "my-storage-region",\n            \n            # Optional. `MEDIA_URL` will be used if it is not set\n            "hostname": "my-pullzone-hostname"\n        }\n    },\n}\n```\n\nIn Django >= 4.2 you can set different credentials for the different storages. This allows you to, for example, use a separate storage for static files.\n\n\n## Using in templates\n\nIn templates, you can use `{{ instance.file.url }}` directly. For example:\n\n```html\n<img src="{{ instance.file.url }}" />\n```\n',
    'author': 'Neki',
    'author_email': 'neki@nekidev.com',
    'maintainer': 'Neki',
    'maintainer_email': 'neki@nekidev.com',
    'url': 'https://github.com/Nekidev/django-bunny/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
