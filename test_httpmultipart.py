# -*- coding:utf-8 -*-

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise
import os
import unittest

import httpmultipart

HTTPBIN = os.environ.get('HTTPBIN_URL', 'http://httpbin.org/')
HTTPBIN = HTTPBIN.rstrip('/') + '/'


class PostMultipartTestCase(unittest.TestCase):

    def test_post_files(self):
        url = HTTPBIN + 'post'

        r = httpmultipart.post(url, [], [('file', 'README', 'README.rst')])
        res = json.loads(r.read())

        assert r.code == 200
        assert 'multipart/form-data' in res['headers']['Content-Type']

    def test_qyweixin_upload(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload'

        r = httpmultipart.post(
            url,
            [
                ('access_token',
                 'dOlBFAjxJZFO3z_QKNipLsuI_3prH1L6UY6CADE2g-Pqwc3vhiTI3Q-KVgX_i8tVC85Nb6SgxI723ug-jVSXbQ'),
                ('type', 'file')], [('media', 'README', 'README.rst')])

        assert r.code == 200

    def test_post_fields(self):
        url = HTTPBIN + 'post'

        r = httpmultipart.post(url, [('a', 'foo'), ('b', 'bar')])
        res = json.loads(r.read())

        assert r.code == 200
        assert 'multipart/form-data' in res['headers']['Content-Type']
        assert res['form'].get('a') == 'foo'
        assert res['form'].get('b') == 'bar'

    def test_post_fields_and_files(self):
        url = HTTPBIN + 'post'

        r = httpmultipart.post(url, [('a', 'foo'), ('b', 'bar')], [('file1', 'README', 'README.rst'), ('file2', 'LICENSE', 'LICENSE')])

        res = json.loads(r.read())

        assert r.code == 200
        assert 'multipart/form-data' in res['headers']['Content-Type']
        assert res['form'].get('a') == 'foo'
        assert res['form'].get('b') == 'bar'
        assert 'file1' in res['files'].keys()
        assert 'file2' in res['files'].keys()


if __name__ == '__main__':
    unittest.main()
