HttpMultipart
======

Just a Python Http Multipart Post Handler.
You can use it to post multipart requests.


Usage
------

- PostMultipart

.. code-block:: python

    >>> import httpmultipart
    >>> multipart = httpmultipart.PostMultipart()
    >>> multipart.post(url, fields, files)
    ...


The fields and files are both sequence.
After run post function, it will return the response.