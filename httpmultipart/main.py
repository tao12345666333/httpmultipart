#!/usr/bin/env python
# coding=utf-8
import base64
import mimetypes
import os


def encode_multipart_formdata(fields, files):

    BOUNDARY = ''.join(['------', base64.urlsafe_b64encode(os.urandom(33))])
    CRLF = '\r\n'
    line = []

    for (key, value) in fields:
        line.append('--' + BOUNDARY)
        line.append('Content-Disposition: form-data; name="%s"' % key)
        line.append('')
        line.append(value)

    for (key, filename, value) in files:
        print key, filename
        line.append('--' + BOUNDARY)
        line.append(
            'Content-Disposition: form-data; name="%s"; filename="%s"' %
            (key, filename))
        line.append(
            'Content-Type: %s' %
            (mimetypes.guess_type(filename)[0] or 'application/octet-stream'))
        line.append('')
        line.append(value)

    line.append('--' + BOUNDARY + '--')
    line.append('')

    body = CRLF.join(line)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body
