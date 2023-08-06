from pytestifyx import TestCase
from pytestifyx.driver.api import APIRequestMeta
from pytestifyx.utils.requests.requests_config import Config


class APIExample(TestCase, metaclass=APIRequestMeta):
    """
    额度账户
    """

    def httpbin_get(self, config: Config):
        """
        get请求
        应用：httpbin
        接口：https://httpbin.org/get
        :return:
        """
        config.set_attr(request_method='GET')

    def httpbin_post(self):
        """
        post请求
        应用：httpbin
        接口：https://httpbin.org/post
        :return:
        """
