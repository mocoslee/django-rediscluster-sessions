django-redis-sessions
=======================
Redis database backend for your sessions

.. image:: https://travis-ci.org/martinrusev/django-redis-sessions.svg?branch=master
    :target: https://travis-ci.org/martinrusev/django-redis-sessions

------------
Installation
------------

1. Run ``pip install django-rediscluster-sessions`` or alternatively  download the tarball and run ``python setup.py install``,

For Django < 1.4 run ``pip install django-redis-sessions==0.3``

2. Set ``redis_sessions.session`` as your session engine, like so::

    SESSION_ENGINE = 'redis_sessions.session'

3. Optional settings::

    SESSION_REDIS_CLUSTER_HOST = 'localhost'
    SESSION_REDIS_CLUSTER_PORT = 6379
    SESSION_REDIS_CLUSTER_DB = 0
    SESSION_REDIS_CLUSTER_PASSWORD = 'password'
    SESSION_REDIS_CLUSTER_PREFIX = 'session'


4. That's it::

See: `django-redis-sessions <http://pypi.python.org/pypi/django-redis-sessions>`_ on pypi

5. Tests::

    $ pip install django nose redis
    # Make sure you have redis running on localhost:6379
    $ nosetests
