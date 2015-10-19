#!/usr/bin/env python
# coding=utf-8
import base64
import mimetypes
import os
import urllib2


class PostMultipart(object):

    """
    This object has one post method which accept three arguments;
    """

    def _encode_multipart_data(self):
        BOUNDARY = ''.join(['-----', base64.urlsafe_b64encode(os.urandom(27))])
        CRLF = '\r\n'
        line = []

        for (key, value) in self.fields:
            line.append('--' + BOUNDARY)
            line.append('Content-Disposition: form-data; name="%s"' % key)
            line.append('')
            line.append(value)

        for (key, filename, filepath) in self.files:
            line.append('--' + BOUNDARY)
            line.append(
                'Content-Disposition: form-data; name="%s"; filename="%s"' %
                (key, filename))
            line.append(
                'Content-Type: %s' %
                (mimetypes.guess_type(filename)[0] or 'application/octet-stream'))
            line.append('')
            line.append(open(filepath, 'rb').read())

        line.append('--' + BOUNDARY + '--')
        line.append('')

        body = CRLF.join(line)
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
        return content_type, body

    def post(self, url, fields, files):
        self.url = url
        self.fields = fields
        self.files = files

        req = urllib2.Request(url=self.url)
        contentType, body = self._encode_multipart_data()

        req.add_header('Content-Length', '%d' % len(body))
        req.add_header('Content-Type', '%s' % contentType)

        return urllib2.urlopen(req, data=body)


def post(url, fields, files=[]):
    """
    fields and files are both sequence.
    each fields element like (name, value) is regular form fields.
    each files element like (name, filename, filepath) is upload files;
    """
    pm = PostMultipart()
    return pm.post(url, fields, files)
