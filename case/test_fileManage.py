import time
import allure
from base.connect_mobile import TestConnetMobile
from page.fileManagePage import TestFileManagePage


class TestFileManage:

    def setup_class(self):
        self.driver = TestConnetMobile().connectMobile()
        self.fileManage_page = TestFileManagePage(self.driver,10,1)

    # #点击刷新
    # allure.step("点击刷新测试用例")
    # def test_refresh(self):
    #    allure.attach("找到页面第一个元素","页面第一个元素的text")
    #    ele = self.fileManage_page.find_first_element_title()
    #    time.sleep(2)
    #    allure.attach("刷新","滑动页面后再点击刷新按钮")
    #    self.fileManage_page.click_refresh()
    #    time.sleep(2)
    #    allure.attach("再次找到页面第一个元素","找到页面第一个元素的text和之前的text对比看是否一致")
    #    ele2 = self.fileManage_page.find_first_element_title()
    #    assert  ele.text == ele2.text
    #
    # allure.step("添加书签")
    # def test_add_bookMark(self):
    #     allure.attach("添加书签","先看书签是否存在，存在先删除在添加，不存在就直接添加")
    #     self.fileManage_page.is_bookMarke_exit("0")
    #     allure.attach("判断书签是否添加成功","判断书签是否添加成功")
    #     result = self.fileManage_page.is_addbookMarke_sucess("0")
    #     assert result == True

    allure.step("添加快捷方式测试用例")
    def test_add_screencut(self):
        allure.attach("添加快捷方式","添加快捷方式")
        self.fileManage_page.add_shot_cut()
        time.sleep(2)
        allure.attach("判断是否添加成功","在桌面寻找有没有添加的快捷方式")
        result = self.fileManage_page.find_shotcut()
        assert result== True