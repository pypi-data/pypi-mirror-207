import inspect
import os

import pytest

from kuto.core.sonic.sib_util import SibUtil
from kuto.running.config import Qrunner
from kuto.utils.config import config
from kuto.utils.log import logger
from kuto.core.android.driver import AndroidDriver
from kuto.core.ios.driver import IosDriver


class TestMain(object):
    """
    Support for app、web、http
    """
    def __init__(self,
                 platform: str = 'api',
                 device_id: str = None,
                 pkg_name: str = None,
                 browser: str = 'chrome',
                 path: str = None,
                 rerun: int = 0,
                 xdist: bool = False,
                 host: str = None,
                 headers: dict = None,
                 timeout: int = 10,
                 screen: bool = False,
                 errors: list = None
                 ):
        """
        @param platform：平台，支持api、ios、android、web，默认api
        @param device_id: 设备id，针对安卓和ios
        @param pkg_name: 应用包名，针对安卓和ios
        @param browser: 浏览器类型，chrome、firefox、edge、safari
        @param path: 用例目录，默认代表当前文件、.代表当前目录
        @param rerun: 失败重试次数
        @param xdist: 是否并发执行，针对接口
        @param host: 域名，针对接口和web
        @param headers: 登录和游客请求头，针对接口和web，格式: {
            "login": {},
            "visit": {}
        }
        @param timeout: 超时时间，针对接口和web
        @param screen: APP和Web操作是否截图（定位成功），默认不截图
        @param errors: 异常弹窗，报错会自动处理异常弹窗
        """
        # app driver 初始化
        if platform == 'android':
            Qrunner.driver = AndroidDriver(device_id, pkg_name)
        elif platform == 'ios':
            Qrunner.driver = IosDriver(device_id, pkg_name)

        # 接口默认请求头设置
        if headers is not None:
            if 'login' not in headers.keys():
                raise KeyError("headers必须要要有login字段")
            login_ = headers.pop('login', {})
            config.set_common('login', login_)
            visit_ = headers.pop('visit', {})
            config.set_common('visit', visit_)

        # 其它参数保存
        config.set_common('platform', platform)
        config.set_common('timeout', timeout)
        config.set_common('screenshot', screen)
        config.set_app('errors', errors)
        config.set_web('browser', browser)
        config.set_common('base_url', host)

        # 执行用例
        logger.info('执行用例')
        if path is None:
            stack_t = inspect.stack()
            ins = inspect.getframeinfo(stack_t[1][0])
            file_dir = os.path.dirname(os.path.abspath(ins.filename))
            file_path = ins.filename
            if "\\" in file_path:
                this_file = file_path.split("\\")[-1]
            elif "/" in file_path:
                this_file = file_path.split("/")[-1]
            else:
                this_file = file_path
            path = os.path.join(file_dir, this_file)
        logger.info(f'用例路径: {path}')
        cmd_list = [
            '-sv',
            '--reruns', str(rerun),
            '--alluredir', 'reports', '--clean-alluredir'
        ]
        if path:
            cmd_list.insert(0, path)
        if xdist:
            """仅支持http接口测试和web测试，并发基于每个测试类，测试类内部还是串行执行"""
            cmd_list.insert(1, '-n')
            cmd_list.insert(2, 'auto')
            cmd_list.insert(3, '--dist=loadscope')
        logger.info(cmd_list)
        pytest.main(cmd_list)

        # 配置文件恢复默认
        config.set_web('host', None)
        config.set_common('headers', {})


main = TestMain


if __name__ == '__main__':
    main()

