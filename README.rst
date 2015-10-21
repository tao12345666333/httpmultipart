HttpMultipart
==============

.. image:: https://img.shields.io/pypi/v/httpmultipart.svg
    :target: https://pypi.python.org/pypi/httpmultipart

.. image:: https://travis-ci.org/tao12345666333/httpmultipart.svg?branch=master
    :target: https://travis-ci.org/tao12345666333/httpmultipart

.. image:: https://coveralls.io/repos/tao12345666333/httpmultipart/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/tao12345666333/httpmultipart?branch=master

.. image:: https://img.shields.io/pypi/dm/httpmultipart.svg
    :target: https://pypi.python.org/pypi/httpmultipart

.. image:: https://img.shields.io/pypi/wheel/httpmultipart.svg
    :target: https://pypi.python.org/pypi/httpmultipart

.. image:: https://img.shields.io/pypi/status/httpmultipart.svg
    :target: https://pypi.python.org/pypi/httpmultipart

.. image:: https://img.shields.io/pypi/l/httpmultipart.svg
    :target: https://pypi.python.org/pypi/httpmultipart

Just a Python Http Multipart Post Handler.
You can use it to post multipart requests.


Usage
------

**Post**

.. code-block:: python

    >>> import httpmultipart
    >>> multipart.post(url, fields, files)
    ...


The fields and files are both sequence.
After run post function, it will return the response.


Installation
--------------

**Automatic installation**::

    pip install httpmultipart


**Manual installation**: Download the latest source from `PyPI
<https://pypi.python.org/pypi/httpmultipart>`_.

.. parsed-literal::

    tar xzvf httpmultipart-$VERSION.tar.gz
    cd httpmultipart-$VERSION
    python setup.py build
    sudo python setup.py install

The HttpMultipart source code is `hosted on GitHub
<https://github.com/tao12345666333/httpmultipart>`_.
