project_slug = '{{ cookiecutter.project_slug }}'

if hasattr(project_slug, 'isidentifier'):
    assert project_slug.isidentifier(), 'Project slug should be valid Python identifier!'

elasticbeanstalk = '{{ cookiecutter.use_elasticbeanstalk_experimental }}'.lower()
heroku = '{{ cookiecutter.use_heroku }}'.lower()
docker = '{{ cookiecutter.use_docker }}'.lower()
application_server = '{{ cookiecutter.application_server }}'.lower()
use_uwsgi_static = '{{ cookiecutter.use_uwsgi_static }}'.lower()
use_whitenoise = '{{ cookiecutter.use_whitenoise }}'.lower()

if use_uwsgi_static == 'y' and application_server != 'uwsgi':
    raise Exception('You can only use "use_uwsgi_static", if you use "uwsgi" as application_server')

if use_uwsgi_static == use_whitenoise and use_uwsgi_static == 'y': 
    raise Exception("Whitenoise and uWsgi static file handling cannot be used at the same time")

if elasticbeanstalk == 'y' and (heroku == 'y' or docker == 'y'):
    raise Exception("Cookiecutter Django's EXPERIMENTAL Elastic Beanstalk support is incompatible with Heroku and Docker setups.")
