# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'jingdong'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '京东商城'
    __url__ = 'http://www.jd.com/'

    def register(self, target):
        self.information = {
            'username': {
                'url': 'https://reg.jd.com/validateuser/isPinEngaged',
                'method': 'post',
                'settings': {
                    'data': {
                        'regName': target,
                        'pin': target
                    },
                    'headers': {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                },
                'safe': {
                    'url': 'https://reg.jd.com/reg/person',
                    'method': 'get'
                },
                'result': {
                    'type': 'json',
                    'value': 'success=1'
                }
            }
        }
