# -*- coding: utf-8 -*-
from flask import current_app, abort
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from common import bos_client
import cvman.cvapp.txtLAdjust as txtLAdjust 

import wget


class TextimgResource(Resource):
    """
    Text Img 资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        data = {
            'url': "hello" 
        }
        return pretty_result(code.OK, data=data)

    def post(self):
        """ 
        文本校正
        ---
        consumes: application/json
        parameters:
          - name: url 
            in: body 
            required: true
            description: 输入文本图片url 
          - name: urli2
            in: body 
            required: true
            description: 输入文本图片url 

        responses:
          200:
            description: 生成的URL
        """
        # get URL
        self.parser.add_argument("url", type=str, location="json", required=True)
        args = self.parser.parse_args()

        # download
        fileName = wget.download(args.url)

        # handle
        txtLAdjust.run(fileName, "./txt.jpg")
        bos_client.upload_file_to_bos('./txt.jpg')
        url = bos_client.get_bos_file_url('txt.jpg')

        # return
        data = {
            'url': url 
        }
        return pretty_result(code.OK, data=data)
