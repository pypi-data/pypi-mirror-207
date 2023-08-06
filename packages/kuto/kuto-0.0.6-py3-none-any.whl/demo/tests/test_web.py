import kuto
from kuto import data

from page.web_page import PatentPage


class TestPatentSearch(kuto.TestCase):

    def start(self):
        self.page = PatentPage(self.driver)

    @data(["无人机", "华为"])
    def test_search(self, param):
        """搜索无人机"""
        self.open()
        self.page.search_input.set_text(param)
        self.page.search_submit.click()
        first_result = self.page.search_result_1.text
        assert param in first_result, f'{first_result} 不包含 {param}'
        self.driver.screenshot('搜索结果')


if __name__ == '__main__':
    kuto.main(
        platform='web',
        host='https://patents.qizhidao.com/'
    )
