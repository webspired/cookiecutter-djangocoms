{% if cookiecutter.use_python3 == 'y' -%}
FROM python:3.5
{% else %}
FROM python:2.7
{%- endif %}
ENV PYTHONUNBUFFERED 1

{% if cookiecutter.application_server == 'uwsgi' -%}
RUN pip install uwsgi==2.0.14

{%- endif %}
# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

RUN pip install -r /requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django

COPY . /app
RUN chown -R django /app

COPY ./compose/django/{{ cookiecutter.application_server }}.sh /{{ cookiecutter.application_server }}.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /{{ cookiecutter.application_server }}.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /{{ cookiecutter.application_server }}.sh \
    && chown django /{{ cookiecutter.application_server }}.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
