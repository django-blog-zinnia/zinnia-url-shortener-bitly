===========================
Zinnia-url-shorterner-bitly
===========================

Zinnia-url-shortener-bitly is a package providing URL shortening within
`django-blog-zinnia`_ via `Bit.ly`_.

Installation
============

* Install the package on your system: ::

  $ pip install zinnia-url-shortener-bitly

  `django-bitly`_ will also be installed as a dependency.

* Add ``'django_bitly'`` in your ``INSTALLED_APPS`` settings and do a **syncdb**.

* Put this setting to enable the URL shortener backend:

  ``ZINNIA_URL_SHORTENER_BACKEND = 'zinnia_bitly'``

* Define these following settings with your credentials:

  ``BITLY_LOGIN`` Your Bit.ly username

  ``BITLY_API_KEY`` Your Bit.ly API Key

.. _django-blog-zinnia: http://django-blog-zinnia.com
.. _Bit.ly: http://bit.ly
.. _django-bitly: https://github.com/discovery/django-bitly
