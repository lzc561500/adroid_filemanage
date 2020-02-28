import time

from base.common_function import Fuction


class TestFileManagePage(Fuction):
    loc_menu = ("id","操作")
    loc_refresh = ("xpath","//*[@text='刷新']")
    loc_dirs = ("id","com.cyanogenmod.filemanager:id/navigation_view_item_name")
    loc_home = ("id","android:id/home")
    loc_bookMarke_list = ("id","com.cyanogenmod.filemanager:id/bookmarks_item_name")
    loc_dele_bookMarke = ("id","移除书签.")
    loc_add_bookMarke = ("xpath","//*[@text='添加到书签']")
    loc_add_shotcut = ("xpath","//*[@text='添加快捷方式']")
    loc_chart = ("xpath","//*[@text='0']")

    #找filemanage页面上的第一个元素的text
    def find_first_element_title(self):
        return self.find_element(self.loc_dirs)

    #点击刷新
    def click_refresh(self):
        #滑动屏幕
        self.screen_swip("down",0.5,0.8,0.5,0.2,5000)
        time.sleep(3)
        #点击菜单
        self.element_click(self.loc_menu)
        #点击刷新按钮
        self.element_click(self.loc_refresh)

    #添加书签
    def click_bookMarke(self):
        # 点击菜单
        self.element_click(self.loc_menu)
        # 点击添加书签按钮
        self.element_click(self.loc_add_bookMarke)

    #获得上层home键的列表并返回
    def find_bookMarke(self):
        #点击页面上层home键
        self.element_click(self.loc_home)
        #点击home键后获得列表上的元素的text值
        text = self.find_elements(self.loc_bookMarke_list)
        book_marke_list = list()
        for i in text:
            book_marke_list.append(i.text)
        return book_marke_list

    #判断页面上层home键列表里有没有要添加的书签如果有就删除没有就添加
    def is_bookMarke_exit(self,text):
        #获得home键列表
        list = self.find_bookMarke()
        #循环遍历看列表里有没有要添加的书签，书签如果有就删除没有就添加
        for i in list:
            if i == text:
                self.element_click(self.loc_dele_bookMarke)
        else:
            time.sleep(2)
            self.element_click(self.loc_menu)
            self.element_click(self.loc_add_bookMarke)

    #判断书签是否添加上
    def is_addbookMarke_sucess(self,text):
        try:
            marke_list = self.find_bookMarke()
            if text in marke_list:
                return True
        except Exception:
            return False

    #添加快捷方式
    def add_shot_cut(self):
        #点击菜单键
        self.element_click(self.loc_menu)
        #点击添加快捷方式键
        self.element_click(self.loc_add_shotcut)
        #点击手机home键
        self.press_code(3)


    #在手机桌面上查看快捷方式是否添加成功
    def find_shotcut(self):
        #通过while循环查找元素
        while True:
            try:
                self.find_element(self.loc_chart)
                break
            except Exception:
                #在一屏内没有找到，就滑动找
                self.screen_swip("left",0.9,0.5,0.1,0.5,1000)


        return True

