# Django Spages

Lightweight single page app for Django using only Jquery and [Page.js](https://github.com/visionmedia/page.js) (7.8 Ko). 

- Fast: load the page once and update the content using rest
- Old school friendly: straigthforward vanila js, no npm and friends steps

## Install

  ```bash
pip install djangorestframework
pip install git+https://github.com/synw/django-spages.git
  ```

Migrate.

Installed apps:

  ```python
`"rest_framework",`
`"spages",`
  ```

Urls: append this at the end of urls.py:

  ```python
urlpatterns.append(url(r'^',include('spages.urls')))
  ```

## Usage

Create pages in the admin. The page.js routes will be autogenerated in ``templates/spages/auto/routes.js``. A 
management command is also available to rebuild the routes: ``python manage.py build_routes``. 

Just link to your pages normaly in the navigation and the routes will be applied, retrieving json 
from the server to update content.

## Why?

The goal is to get faster render speed for pages, and to improve the user experience,
specialy the ones that use low bandwidth connections.

## Todo

Better admin interface