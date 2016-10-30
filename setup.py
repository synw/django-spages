from setuptools import setup, find_packages


version = __import__('spages').__version__

setup(
  name = 'django-spages',
  packages=find_packages(),
  include_package_data=True,
  version = version,
  description = 'Lightweight single page app for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-spages', 
  download_url = 'https://github.com/synw/django-spages/releases/tag/'+version, 
  keywords = ['django', 'spa', 'page.js'],
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  zip_safe=False,
  install_requires=[
        'pytz',
        "djangorestframework",
        'django-ckeditor',
        'django-codemirror2',
        "django-mptt-graph",
    ],
)
