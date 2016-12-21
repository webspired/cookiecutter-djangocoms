Cookiecutter Django CMS
=======================

.. image:: https://pyup.io/repos/github/webspired/cookiecutter-djangocms/shield.svg
     :target: https://pyup.io/repos/github/webspired/cookiecutter-djangocms/
     :alt: Updates

.. image:: https://travis-ci.org/webspired/cookiecutter-djangocms.svg?branch=master
     :target: https://travis-ci.org/webspired/cookiecutter-djangocms?branch=master
     :alt: Build Status

Powered by Cookiecutter_, Cookiecutter Django CMS is a framework for jumpstarting
production-ready Django CMS projects quickly.
It is based and forked of the famous `Cookiecutter Django`_ framework, and `Cookiecutter Django Webspired`_.


* Documentation: http://cookiecutter-django-webspired.readthedocs.io/en/latest/
* See Troubleshooting_ for common errors and obstacles

.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. _`Cookiecutter Django`: https://github.com/pydanny/cookiecutter-django

.. _`Cookiecutter Django Webspired`: https://github.com/webspired/cookiecutter-django-webspired

.. _Troubleshooting: http://cookiecutter-django-webspired.readthedocs.io/en/latest/troubleshooting.html

.. _528: https://github.com/pydanny/cookiecutter-django/issues/528#issuecomment-212650373


Why would you want to use Cookiecutter Django CMS
-------------------------------------------------

Cookiecutter Django CMS is a combination of: 

* `Cookiecutter Django Webspired`_ framework
* Django Cms Installer project.
* `Cookiecutter Django`_ framework and

It will provide you a fully featured Django project with a Django CMS setup at a mouse-click.
* Django Best practices
* Working CMS based on the standard `Django CMS installer`_ and Django CMS LTS version
* Deployment Ready
* With an optional Docker setup

.. _`Cookiecutter Django`: https://github.com/pydanny/cookiecutter-django
.. _`Django CMS installer`: abc 


Features
---------

* For Django 1.10 and Django CMS 3.4
* Renders Django projects with 100% starting test coverage
* 12-Factor_ based settings via django-environ_
* Optimized development and production settings
* Registration via django-allauth_
* Comes with custom user model ready to go
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Media storage using Amazon S3
* Docker support using docker-compose_ for development and production
* Procfile_ for deploying to Heroku
* Instructions for deploying to PythonAnywhere_
* Works with Python 2.7.x or 3.5.x
* Run tests with unittest or py.test
* Customizable PostgreSQL version
* Experimental support for Amazon Elastic Beanstalk


Optional Integrations
---------------------

*These CMS  features can be enabled during initial project setup. (planned)*

* Load a starting page with examples after installation (english language only). Choose "no" if you use a custom template set. (choices: yes, no) [default no]: yes
* Install and configure reversion support (only for django CMS 3.2 and 3.3) (choices: yes, no) [default yes]: 
* Activate CMS permission management (choices: yes, no) [default no]: yes
* Use `Twitter Bootstrap`_ Theme (choices: yes, no) [default no]: yes
* Languages to enable. Option can be provided multiple times, or as a comma separated list. Only language codes supported by Django can be used here. Example: en, fr-FR, it-IT: en, de-de

*These general project/Django features can be enabled during initial project setup.*

* Serve static files from Amazon S3 or Whitenoise_
* Configuration for Celery_
* Integration with MailHog_ for local email testing
* Integration with Sentry_ for error logging
* Integration with Opbeat_ for performance monitoring
* Integration with `uWsgi`_ as application server and static file server 

.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _django-allauth: https://github.com/pennersr/django-allauth
.. _django-avatar: https://github.com/grantmcconnaughey/django-avatar
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _Mailgun: http://www.mailgun.com/
.. _Whitenoise: https://whitenoise.readthedocs.io/
.. _Celery: http://www.celeryproject.org/
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose
.. _Opbeat: https://opbeat.com/
.. _PythonAnywhere: https://www.pythonanywhere.com/
.. _`uWsgi`: http://uwsgi-docs.readthedocs.io/en/latest


Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.2+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).
* uWsgi integration is only fully supported with a Docker setup; if you run it outside of Docker, you need to install und monitor uWsgi for your platform.
* django-compressor has been removed since it does not support offline compression with Sekizai


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.4.0"

Now run it against this repo::

    $ cookiecutter https://github.com/pydanny/cookiecutter-djangocms

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Juergen  Schackmann', etc to your own information.

Answer the prompts with your own desired options_. For example::

    Cloning into 'cookiecutter-djangocms'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Project Name]: Reddit Clone
    project_slug [reddit_clone]: reddit
    author_name [Daniel Roy Greenfeld]: Daniel Greenfeld
    email [you@example.com]: pydanny@gmail.com
    description [A short description of the project.]: A reddit clone.
    domain_name [example.com]: myreddit.com
    version [0.1.0]: 0.0.1
    timezone [UTC]: America/Los_Angeles
    application_server
    1 - gunicorn
    2 - uwsgi
    Choose from 1, 2 [1]: 2
    use_uwsgi_static [y]: y
    use_whitenoise [n]: n
    use_celery [n]: y
    use_mailhog [n]: n
    use_sentry_for_error_reporting [y]: y
    use_opbeat [n]: y
    use_pycharm [n]: y
    windows [n]: n
    use_python3 [y]: y
    use_docker [y]: y
    use_heroku [n]: y
    Select postgresql_version:
    1 - 9.5
    2 - 9.4
    3 - 9.3
    4 - 9.2
    Choose from 1, 2, 3, 4 [1]: 1
    Select js_task_runner:
    1 - Gulp
    2 - Grunt
    3 - Webpack
    4 - None
    Choose from 1, 2, 3, 4 [1]: 1
    use_lets_encrypt [n]: n
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    use_elasticbeanstalk_experimental: n

Enter the project and take a look around::

    $ cd reddit/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:pydanny/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For local development, see the following:

* `Developing locally`_
* `Developing locally using docker`_

.. _options: http://cookiecutter-djangocms.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://cookiecutter-djangocms.readthedocs.io/en/latest/developing-locally.html
.. _`Developing locally using docker`: http://cookiecutter-djangocms.readthedocs.io/en/latest/developing-locally-docker.html


Community
-----------

* Have questions? **Before you ask questions anywhere else**, please post your question on `Stack Overflow`_ under the *cookiecutter-django* tag. We check there periodically for questions.
* If you think you found a bug or want to request a feature, please open an issue_.

.. _`Stack Overflow`: http://stackoverflow.com/questions/tagged/cookiecutter-djangocms
.. _`issue`: https://github.com/webspired/cookiecutter-djangocms/issues


"Your Stuff"
-------------

Scattered throughout the Python and HTML of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.

Releases
--------

Need a stable release? You can find them at https://github.com/webspired/cookiecutter-djangocms/releases


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:


Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~

We accept pull requests if they're small, atomic, and make our own project development
experience better.

Articles
---------

* `Development and Deployment of Cookiecutter-Django on Fedora`_ - Jan. 18, 2016
* `Development and Deployment of Cookiecutter-Django via Docker`_ - Dec. 29, 2015
* `How to create a Django Application using Cookiecutter and Django 1.8`_ - Sept. 12, 2015
* `Introduction to Cookiecutter-Django`_ - Feb. 19, 2016
* `Django and GitLab - Running Continuous Integration and tests with your FREE account`_ - May. 11, 2016

Have a blog or online publication? Write about your cookiecutter-django tips and tricks, then send us a pull request with the link.

.. _`Development and Deployment of Cookiecutter-Django via Docker`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-via-docker/
.. _`Development and Deployment of Cookiecutter-Django on Fedora`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-on-fedora/
.. _`How to create a Django Application using Cookiecutter and Django 1.8`: https://www.swapps.io/blog/how-to-create-a-django-application-using-cookiecutter-and-django-1-8/
.. _`Introduction to Cookiecutter-Django`: http://krzysztofzuraw.com/blog/2016/django-cookiecutter.html
.. _`Django and GitLab - Running Continuous Integration and tests with your FREE account`: http://dezoito.github.io/2016/05/11/django-gitlab-continuous-integration-phantomjs.html


Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/



webspired
Optional default time zone. Example: Europe/Rome [default Europe/Berlin]: 
Activate Django timezone support (choices: yes, no) [default yes]: 
Activate Django I18N / L10N setting; this is automatically activated if more than language is provided (choices: yes, no) [default yes]: 
Database configuration (in URL format). Example: sqlite://localhost/project.db [default sqlite://localhost/project.db]:

 