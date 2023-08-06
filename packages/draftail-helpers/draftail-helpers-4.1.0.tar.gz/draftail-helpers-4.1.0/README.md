draftail-helpers
================

Supplementary code when developing custom features for the Draftail editor in Wagtail. Please bear with us while we prepare more detailed documentation.

Compatibility
-------------

`django-helpers`' major.minor version number indicates the Wagtail release it is compatible with. Currently this is Wagtail 4.1.x.

Additional dependencies are:
- Django 4.1

Installation
------------

1. Install using `pip`:
  ```shell
  pip install draftail-helpers
  ```
2. Add `draftail_helpers` to your `INSTALLED_APPS` setting:
   ```python
   INSTALLED_APPS = [
     # ...
     'draftail_helpers'
     # ...
   ]
   ```
