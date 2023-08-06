# 介绍

[Gitee](https://gitee.com/bluepang2021/kuto)

[![PyPI version](https://badge.fury.io/py/kuto.svg)](https://badge.fury.io/py/kuto) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kuto)
![visitors](https://visitor-badge.glitch.me/badge?page_id=kuto_new.kuto)

AppUI/WebUI/HTTP automation testing framework based on pytest.

> 基于pytest 的 App UI/Web UI/HTTP自动化测试框架。

## 特点

* 集成`facebook-wda`/`uiautomator2`/`selenium`/`requests`，支持安卓 UI/IOS UI/Web UI/HTTP测试。
* 集成`allure`, 支持HTML格式的测试报告。
* 提供脚手架，快速生成自动化测试项目。
* 提供强大的`数据驱动`。
* 提供丰富的断言。
* 支持生成随机测试数据。
* 支持设置用例依赖。


## 三方依赖

* Allure：https://github.com/allure-framework/allure2
* WebDriverAgent：https://github.com/appium/WebDriverAgent

## Install

```shell
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple kuto
```

## 🤖 Quick Start

1、查看帮助：
```shell
usage: kuto [-h] [-v] [-n PROJECT_NAME] [-p PLATFORM] [-i INSTALL]

全平台自动化测试框架

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         版本号
  -p PLATFORM, --platform PLATFORM
                        所属平台
  -i INSTALL, --install INSTALL
                        浏览器驱动名称

```

2、创建项目：
```shell
> kuto -p android
```

3、运行项目：

* ✔️ 在`pyCharm`中右键执行(需要把项目的单元测试框架改成unittests)

* ✔️ 通过命令行工具执行。

4、查看报告

运行`allure server report`浏览器会自动调起报告（需先安装配置allure）


## 🔬 Demo

[demo](/demo) 提供了丰富实例，帮你快速了解kuto的用法。

### 安卓APP 测试

```python
import kuto

from page.adr_page import HomePage


class TestSearch(kuto.TestCase):

    def start(self):
        self.page = HomePage(self.driver)

    def test_pom(self):
        self.page.my_entry.click()
        self.page.setting_entry.click()
        self.assert_in_page('设置')
```

__说明：__

* 创建测试类必须继承 `kuto.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* kuto的封装了`assertText`、`assertElement` 等断言方法。
* 如果用例间有耦合关系，建议使用pom模式，方便复用；否则，使用普通模式即可
  - pom模式需要继承kuto.Page
  - 页面初始化的时候需要传入driver

### IOS APP 测试

```python
import kuto


class TestSearch(kuto.TestCase):

    def test_normal(self):
        self.elem(text='我的', desc='我的入口').click()
        self.elem(text='settings navi', desc='设置入口').click()
        self.assert_in_page('设置')
```

__说明：__

* 创建测试类必须继承 `kuto.IosTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* kuto的封装了`assertText`、`assertElement` 等断言方法。
* 如果用例间有耦合关系，建议使用pom模式，方便复用；否则，使用普通模式即可
  - pom模式需要继承kuto.Page
  - 页面初始化的时候需要传入driver

### Web 测试

```python
import kuto

from page.web_page import PatentPage


class TestPatentSearch(kuto.TestCase):

    def start(self):
        self.page = PatentPage(self.driver)

    def test_pom(self):
        self.open()
        self.page.search_input.set_text('无人机')
        self.page.search_submit.click()
        self.assert_in_page('无人机')
```

__说明：__

* 创建测试类必须继承 `kuto.WebTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* kuto的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。
* 如果用例间有耦合关系，建议使用pom模式，方便复用；否则，使用普通模式即可
  - pom模式需要继承kuto.Page
  - 页面初始化的时候需要传入driver

### HTTP 测试

```python
import kuto


class TestGetToolCardListForPc(kuto.TestCase):

    def test_getToolCardListForPc(self):
        payload = {"type": 2}
        headers = {"user-agent-web": "X/b67aaff2200d4fc2a2e5a079abe78cc6"}
        self.post('/qzd-bff-app/qzd/v1/home/getToolCardListForPc', headers=headers, json=payload)
        self.assert_eq('code', 0)
```

__说明：__

* 创建测试类必须继承 `kuto.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* kuto的封装了`assertEq`、`assertLenEq` 和 `assertLenGt`等断言方法。

### Run the test

```python
import kuto

kuto.main()  # 当前文件，pycharm中需要把默认的测试框架从pytest改成unittest，才能右键run
kuto.main(path="./")  # 当前目录下的所有测试文件
kuto.main(path="./test_dir/")  # 指定目录下的所有测试文件
kuto.main(path="./test_dir/test_api.py")  # 指定目录下的测试文件
```

### 感谢

感谢从以下项目中得到思路和帮助。

* [seldom](https://github.com/SeldomQA/seldom)

* [selenium](https://www.selenium.dev/)

* [uiautomator2](https://github.com/openatx/uiautomator2)
  
* [facebook-wda](https://github.com/openatx/facebook-wda)

* [requests](https://github.com/psf/requests)

## 高级用法

### 随机测试数据

测试数据是测试用例的重要部分，有时不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就需要随机生成一些测试数据。

kuto 提供了随机获取测试数据的方法。

```python
import kuto
from kuto import testdata


class TestYou(kuto.TestCase):
    
    def test_case(self):
        """a simple test case """
        word = testdata.get_word()
        print(word)
        
if __name__ == '__main__':
    kuto.main()
```

通过`get_word()` 随机获取一个单词，然后对这个单词进行搜索。

**更多的方法**

```python
from kuto.testdata import *
# 随机一个名字
print("名字：", first_name())
print("名字(男)：", first_name(gender="male"))
print("名字(女)：", first_name(gender="female"))
print("名字(中文男)：", first_name(gender="male", language="zh"))
print("名字(中文女)：", first_name(gender="female", language="zh"))
# 随机一个姓
print("姓:", last_name())
print("姓(中文):", last_name(language="zh"))
# 随机一个姓名
print("姓名:", username())
print("姓名(中文):", username(language="zh"))
# 随机一个生日
print("生日:", get_birthday())
print("生日字符串:", get_birthday(as_str=True))
print("生日年龄范围:", get_birthday(start_age=20, stop_age=30))
# 日期
print("日期(当前):", get_date())
print("日期(昨天):", get_date(-1))
print("日期(明天):", get_date(1))
# 数字
print("数字(8位):", get_digits(8))
# 邮箱
print("邮箱:", get_email())
# 浮点数
print("浮点数:", get_float())
print("浮点数范围:", get_float(min_size=1.0, max_size=2.0))
# 随机时间
print("当前时间:", get_now_datetime())
print("当前时间(格式化字符串):", get_now_datetime(strftime=True))
print("未来时间:", get_future_datetime())
print("未来时间(格式化字符串):", get_future_datetime(strftime=True))
print("过去时间:", get_past_datetime())
print("过去时间(格式化字符串):", get_past_datetime(strftime=True))
# 随机数据
print("整型:", get_int())
print("整型32位:", get_int32())
print("整型64位:", get_int64())
print("MD5:", get_md5())
print("UUID:", get_uuid())
print("单词:", get_word())
print("单词组(3个):", get_words(3))
print("手机号:", get_phone())
print("手机号(移动):", get_phone(operator="mobile"))
print("手机号(联通):", get_phone(operator="unicom"))
print("手机号(电信):", get_phone(operator="telecom"))
```

* 运行结果

```shell
名字： Hayden
名字（男）： Brantley
名字（女）： Julia
名字（中文男）： 觅儿
名字（中文女）： 若星
姓: Lee
姓（中文）: 白
姓名: Genesis
姓名（中文）: 廉高义
生日: 2000-03-11
生日字符串: 1994-11-12
生日年龄范围: 1996-01-12
日期（当前）: 2022-09-17
日期（昨天）: 2022-09-16
日期（明天）: 2022-09-18
数字(8位): 48285099
邮箱: melanie@yahoo.com
浮点数: 1.5315717275531858e+308
浮点数范围: 1.6682402084146244
当前时间: 2022-09-17 23:33:22.736031
当前时间(格式化字符串): 2022-09-17 23:33:22
未来时间: 2054-05-02 11:33:47.736031
未来时间(格式化字符串): 2070-08-28 16:38:45
过去时间: 2004-09-03 12:56:23.737031
过去时间(格式化字符串): 2006-12-06 07:58:37
整型: 7831034423589443450
整型32位: 1119927937
整型64位: 3509365234787490389
MD5: d0f6c6abbfe1cfeea60ecfdd1ef2f4b9
UUID: 5fd50475-2723-4a36-a769-1d4c9784223a
单词: habitasse
单词组（3个）: уж pede. metus.
手机号: 13171039843
手机号(移动): 15165746029
手机号(联通): 16672812525
手机号(电信): 17345142737
```

### 用例的依赖

**depend**

`depend` 装饰器用来设置依赖的用例。

```python
import kuto
from kuto import depend


class TestDepend(kuto.TestCase):
    
    @depend(name='test_001')
    def test_001(self):
        print("test_001")
        
    @depend("test_001", name='test_002')
    def test_002(self):
        print("test_002")
        
    @depend(["test_001", "test_002"])
    def test_003(self):
        print("test_003")
        
if __name__ == '__main__':
    kuto.main()
```

* 被依赖的用例需要用name定义被依赖的名称，因为本装饰器是基于pytest.mark.dependency，它会出现识别不了被装饰的方法名的情况
  ，所以通过name强制指定最为准确
  ```@depend(name='test_001')```
* `test_002` 依赖于 `test_001` , `test_003`又依赖于`test_002`。当被依赖的用例，错误、失败、跳过，那么依赖的用例自动跳过。
* 如果依赖多个用例，传入一个list即可
```@depend(['test_001', 'test_002'])```
  
### 发送邮件

```python
import kuto
from kuto.utils.mail import Mail


if __name__ == '__main__':
    kuto.main()
    mail = Mail(host='xx.com', user='xx@xx.com', password='xxx')
    mail.send_report(title='Demo项目测试报告', report_url='https://www.baidu.com', receiver_list=['xx@xx.com'])
```

- title：邮件标题
- report_url: 测试报告的url
- receiver_list: 接收报告的用户列表


### 发送钉钉

```python
import kuto
from kuto.utils.dingtalk import DingTalk


if __name__ == '__main__':
    kuto.main()
    dd = DingTalk(secret='xxx',
                  url='xxx')
    dd.send_report(msg_title='Demo测试消息', report_url='https://www.baidu.com')
```

- `secret`: 如果钉钉机器人安全设置了签名，则需要传入对应的密钥。
- `url`: 钉钉机器人的Webhook链接
- `msg_title`: 消息标题
- `report_url`: 测试报告url

## 数据驱动

数据驱动是测试框架非常重要的功能之一，它可以有效的节约大量重复的测试代码。kuto针对该功能做强大的支持。

### @data()方法

当测试数据量比较少的情况下，可以通过`@data()`管理测试数据。


**参数化测试用例**

```python
import kuto
from kuto import data


class TestDataDriver(kuto.TestCase):
    @data('name,keyword', [
        ("First case", "kuto"),
        ("Second case", "selenium"),
        ("Third case", "unittest"),
    ])
    def test_tuple_data(self, name, keyword):
        """
        Used tuple test data
        :param name: case desc
        :param keyword: case data
        """
        print(f"test data: {name} + {keyword}")

    @data('name,keyword', [
        ["First case", "kuto"],
        ["Second case", "selenium"],
        ["Third case", "unittest"],
    ])
    def test_list_data(self, name, keyword):
        """
        Used list test data
        """
        print(f"test data: {name} + {keyword}")

    @data('json', [
        {"scene": 'First case', 'keyword': 'kuto'},
        {"scene": 'Second case', 'keyword': 'selenium'},
        {"scene": 'Third case', 'keyword': 'unittest'},
    ])
    def test_dict_data(self, json):
        """
        used dict test data
        """
        print(f"case desc: {json['scene']}")
        print(f"test data: {json['keyword']}")
    
    @data('param', [
            ("First case", "kuto"),
            ("Second case", "selenium"),
            ("Third case", "unittest"),
        ])
    def test_tuple_single_param(self, param):
        """
        Used tuple test data
        :param name: case desc
        :param keyword: case data
        """
        print(f"test data: {param[0]} + {param[1]}")
    
    @data('param_a', [1, 2])
    @data('param_b', ['c', 'd'])
    def test_cartesian_product(self, param_a, param_b):
        """
        笛卡尔积
        :param param_a: case desc
        :param param_b: case data
        """
        print(f"test data: {param_a} + {param_b}")
```

通过`@data()` 装饰器来参数化测试用例。

### @file_data() 方法

当测试数据量比较大的情况下，可以通过`@file_data()`管理测试数据。

**JSON 文件参数化**

kuto 支持将`JSON`文件的参数化。

json 文件：

```json
{
  "login1": [
    [1, 2],
    [3, 4]
  ],
  "login2": [
    {"username":  1, "password":  2},
    {"username":  3, "password": 4}
  ]
}

```

> 注：`login1` 和 `login2` 的调用方法一样。 区别是前者更简洁，后者更易读。
```python
import kuto
from kuto import file_data


class TestYou(kuto.TestCase):

    @file_data("login1")
    def test_default(self, login1):
        """文件名使用默认值
        file: 'data.json'
        """
        print(login1[0], login1[1])

    @file_data(key="login2", file='data.json')
    def test_full_param(self, login2):
        """参数都填上"""
        print(login2["username"], login2["password"])
```

- key: 指定字典的 key，默认不指定解析整个 JSON 文件。
- file : 指定 JSON 文件的路径。

# Web UI 测试

## 浏览器与驱动

### 下载浏览器驱动

> kuto集成webdriver_manager管理浏览器驱动。
和Selenium一样，在使用kuto运行自动化测试之前，需要先配置浏览器驱动，这一步非常重要。

kuto 集成 [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) ，提供了`chrome/firefox/edge`浏览器驱动的自动下载。

__自动下载__

如果你不配置浏览器驱动也没关系，kuto会根据你使用的浏览器版本，自动化下载对应的驱动文件。

kuto 检测到的`Chrome`浏览器后，自动化下载对应版本的驱动，并保存到本地，以便于下次执行的时候就不需要下载了。
并且，非常贴心的将`chromedriver`的下载地址从 google 切换成了 taobao 的镜像地址。

__手动下载__

通过`kuto`命令下载浏览器驱动。
```shell
> kuto --install chrome
> kuto --install firefox
> kuto --install ie
> kuto --install edge
```
1. 默认下载到当前的`C:\Users\username\.wdm\drivers\` 目录下面。
2. Chrome: `chromedriver` 驱动，众所周知的原因，使用的taobao的镜像。
3. Safari: `safaridriver` （macOS系统自带，默认路径:`/usr/bin/safaridriver`）

指定浏览器驱动

```python
import kuto
from kuto import ChromeConfig


if __name__ == '__main__':
    ChromeConfig.command_executor = '/Users/UI/Documents/chromedriver'
    kuto.main(platform='web', browser="chrome")
```

### 指定不同的浏览器

我们运行的自动化测试不可能只在一个浏览器下运行，我们分别需要在chrome、firefox浏览器下运行。在kuto中需要只需要修改一个配置即可。

```python
import kuto
# ……
if __name__ == '__main__':
    kuto.main(browser="chrome") # chrome浏览器,默认值
    kuto.main(browser="gc")     # chrome简写
    kuto.main(browser="firefox") # firefox浏览器
    kuto.main(browser="ff")      # firefox简写
    kuto.main(browser="edge")    # edge浏览器
    kuto.main(browser="safari")  # safari浏览器
```
在`main()`方法中通过`browser`参数设置不同的浏览器，默认为`Chrome`浏览器。

## kuto API

### 查找元素

* id_
* name
* class_name
* tag
* link_text
* partial_link_text
* css
* xpath

__使用方式__

```python
import kuto


class TestDemo(kuto.TestCase):
    
    def test_demo(self):
        self.elem(id_="kw", desc='xxx')
        self.elem(name="wd", desc="xxx")
        self.elem(class_name="s_ipt", desc="xxx")
        self.elem(tag_name="input", desc="xxx")
        self.elem(xpath="//input[@id='kw']", desc="xxx")
        self.elem(css="#kw", desc="xxx")
        self.elem(link_text="hao123", desc='xxx')
        self.elem(partial_link_text="hao", desc='xxx')
```

__帮助信息__

* [CSS选择器](https://www.w3school.com.cn/cssref/css_selectors.asp)
* [xpath语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)

# APP UI 测试

## 公共依赖

* [weditor](https://github.com/alibaba/web-editor)
  - 用于查看控件属性
    
* 手机通过usb连接电脑

## 安卓 UI 测试

### 依赖环境

* [adb](https://formulae.brew.sh/cask/android-platform-tools)
    - 用于查看手机设备id
    
### kuto API

#### 查找元素

* id_
* class_name
* text
* xpath

__使用方式__

```python
self.elem(res_id="kw", desc='xxx')
self.elem(class_name="wd", desc="xxx")
self.elem(text="s_ipt", desc="xxx")
self.elem(xpath="input", desc="xxx")

```

## IOS UI 测试

### 依赖环境

* [WebDriverAgent](https://testerhome.com/topics/7220)
    - 把代码操作转化成原生操作
* [tidevice](https://github.com/alibaba/taobao-iphone-device)
    - 查看手机设备id
    - 启动WebDriverAgent
    
### kuto API

#### 查找元素

* name
* label
* value
* text
* class_name
* xpath

__使用方式__

```python
self.elem(name="kw", desc='xxx')
self.elem(label="wd", desc="xxx")
self.elem(value="s_ipt", desc="xxx")
self.elem(text="input", desc="xxx")
self.elem(class_name="input", desc="xxx")
self.elem(xpath="input", desc="xxx")

```
