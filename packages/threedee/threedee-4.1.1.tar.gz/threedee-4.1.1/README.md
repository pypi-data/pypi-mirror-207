threedee
========

A Wagtail app for 3D media items based on media-catalogue and Three-JS. Currently only supports extracted Paraview models.
Please bear with us while we prepare more detailed documentation.

Compatibility
-------------

`threedee`' major.minor version number indicates the Wagtail release it is compatible with. Currently this is Wagtail 4.1.x

Installation
------------

1. Install using `pip`:
  ```shell
  pip install threedee
  ```
2. Add
   `threedee` to your `INSTALLED_APPS` setting:
   ```python
   INSTALLED_APPS = [
     # ...
     'threedee'
     # ...
   ]
   ```
