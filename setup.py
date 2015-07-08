import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-offline',
    version='0.2',
    packages=['offline'],
    include_package_data=True,
    license='BSD License',  
    description='A simple Django app to swith your Django project between offline/online mode and display a 503 error page, while your django site is offline (under maintenance)',
    long_description=README,
    url='https://github.com/ankitjaiswal07/django-offline',
    author='Ankit Jaiswal',
    author_email='ankit.jaiswal07@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
