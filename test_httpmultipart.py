# -*- coding:utf-8 -*-
import unittest
import httpmultipart
import qyweixin


class PostMultipartTestCase(unittest.TestCase):

    def test_upload_files(self):
        pm = httpmultipart.PostMultipart()

        r = pm.post('https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=0Qah_iaf7fsy5lZAwRe_56-NjrX9wIh-S22UpyU2cDLJjbp2ukHYV_sKH6DX5TRScFgYF9znmN_nFJo0fKQKwQ&type=image', [('type', 'image')], [('media', 't.jpg', 't.jpg')])

        print r.read()


if __name__ == '__main__':
    unittest.main()
