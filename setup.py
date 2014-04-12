"""Setup script of zinnia-url-shortener-bitly"""
from setuptools import setup
from setuptools import find_packages

setup(
    name='zinnia-url-shortener-bitly',
    version='1.0',

    description='Bit.ly URL shortener backend for django-blog-zinnia',
    long_description=open('README.rst').read(),
    keywords='django, zinnia, url, bit.ly',

    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='https://github.com/Fantomas42/zinnia-url-shortener-bitly',

    packages=find_packages(exclude=['demo_zinnia_bitly']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license='BSD License',
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-bitly']
)
