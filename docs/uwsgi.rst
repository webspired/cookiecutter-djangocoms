uWsgi
=====

By default, this project uses gunicorn as application server. But during the bootstrapping, you will be asked to choose between gunicorn and `uWsgi`_. While gunicorn is a very stable application server that is recommended by the community, `uWsgi`_ provides more options and is therefore more complex to setup and configure. 

Please only choose this option, if you know what you are doing. Especially if you do not use it within a Docker container. 

Configuration
-------------

This project contains a well documented uwsgi.ini file in the config directory, next to the wsgi.py file. Please checkout this file and adapt it to your needs, if need should be.


Setup with Docker
-----------------

If you have chosen to run this project with Docker and `uWsgi`_, this should work out of the box:

    - uWsgi is installed
    - uWsgi server is started within the Docker container
    - the ini file is used and will use proper defaults.


Setup without Docker
--------------------

If you have chosen to run this project with `uWsgi`_, but without Docker, you are responsible, to install `uWsgi`_ on your platform, make sure to start with a proper start script and call the project with the included INI file.


Static Files
------------

`uWsgi`_ does offer an option, to serve static files very efficiently as well. With that option, any static file serving via AWS S3 is disabled.


Dependencies & Conflicts with other options and features
--------------------------------------------------------

    - You will not be able to serve static files via `uWsgi`_, unless you have chosen `uWsgi`_ as application server.
    - You will not be able to serve static files via `uWsgi`_ and use Whitnoise.
    - If you to serve static files via `uWsgi`_, *none* of the AWS S3 features of this template will be available.

.. _`uWsgi`: http://uwsgi-docs.readthedocs.io/en/latest