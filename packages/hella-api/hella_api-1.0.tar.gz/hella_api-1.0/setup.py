from setuptools import setup

setup(
    name='hella_api',
    version='1.0',
    author='tembz',
    author_email='ap11dlayt@gmail.com',
    description='module for api.hella.team',
    long_description_content_type='text/markdown',
    url='https://github.com/tembz/hella_api',
    packages=['hella_api'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='hella_api',
    install_requires=['requests'],
)
