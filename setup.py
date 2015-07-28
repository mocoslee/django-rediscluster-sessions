from setuptools import setup
from rediscluster_sessions import __version__


packages = ['rediscluster_sessions']


setup(
    name='django-rediscluster-sessions',
    version=__version__,
    description= "RedisCluster Session Backend For Django",
    author='Mocos Lee',
    author_email='MocosLee@gmail.com',
    url='',
    packages=packages,
    zip_safe=False,
    install_requires=['redis>=2.4.10','redis-py-cluster==1.0.0'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
