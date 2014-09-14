=====
Offline
=====

Offline is a simple Django app to put a Django Web application under 
maintenance/offline mode using a simple interface under admin role.

Installation
------------

django-offline works with python >= 2.5 and django >= 1.2 

Recommended way to install is by using pip as below:

pip install django-offline

Quick start
-----------

1. Add "offline" to your INSTALLED_APPS setting like this:

      INSTALLED_APPS = (
          ...
          'offline',
      )

2. Add the OfflineMiddleware to MIDDLEWARE_CLASSES list 
   (after SessionMiddleware and AuthenticationMiddleware) in settings.py 
   file of your project:

   MIDDLEWARE_CLASSES = (
    ...
    'offline.middleware.OfflineMiddleware',
)


3. Run `python manage.py syncdb` to create the polls models.

4. Visit the admin site to set your Web application to offline mode by 
   setting offline flag (you'll need the Admin app enabled).

5. You can customize the message shown on the website.


