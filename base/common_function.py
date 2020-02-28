from selenium.webdriver.support.wait import WebDriverWait



class Fuction:

    def __init__(self,driver,timeout,clearance):
        self.driver=driver
        self.timeout=timeout
        self.clearance=clearance

    #找页面一个元素方法
    def find_element(self,loc):
        if not isinstance(loc,tuple):
                print("传的数据错误，如：loc=('id','value')")
        else:
                print("正在定位元素----定位方式：%s,value值---%s"%(loc[0],loc[1]))
                ele=WebDriverWait(self.driver,self.timeout,self.clearance).until(lambda x:x.find_element(*loc))
                return ele

    #找页面多个元素的方法
    def find_elements(self,loc):
        if not isinstance(loc,tuple):
                print("传的数据错误，如：loc=('id','value')")
        else:
                print("正在定位元素----定位方式：%s,value值---%s"%(loc[0],loc[1]))
                eles=WebDriverWait(self.driver,self.timeout,self.clearance).until(lambda x:x.find_elements(*loc))
                return eles

    #找到元素并点击
    def element_click(self,loc):
        ele=self.find_element(loc)
        ele.click()

    #找到元素发送内容
    def send_keys(self,loc,text):
        ele=self.find_element(loc)
        ele.send_keys(text)

    #截屏方法
    def screen_shoot(self, fileName):
        self.driver.get_screenshot_as_file("./picture" + fileName + ".png")

    #找页面的toast方法
    def find_toast(self,message,timeout,clearance,fileName,is_screen_shot=False):
        loc = ("xpath","//*contains[(@text,'"+message+"')]")
        ele = self.find_element(loc,timeout,clearance)
        if is_screen_shot:
            self.screen_shoot(fileName)
        return ele.text

    #判断toast是否存在
    def is_toast_exit(self,message,timeout,clearance,fileName,is_screen_shot=False):
        try:
            self.find_toast(message,timeout,clearance)
            if is_screen_shot:
                self.screen_shoot(fileName)
            return True
        except Exception:
            return False


    #向上滑屏，向下滑屏，向左滑屏向右滑屏方法
    def screen_swip(self,option,x_start_num,y_start_num,x_end_num,y_end_num,time):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        start_x = width * x_start_num
        start_y = height * y_start_num
        end_x = width * x_end_num
        end_y = height * y_end_num

        if option == "down" and y_start_num > y_end_num and x_start_num == x_end_num:
            self.driver.swipe(start_x,start_y,end_x,end_y,time)

        elif option == "up"and y_start_num < y_end_num and x_start_num == x_end_num:
            self.driver.swipe(start_x,start_y,end_x,end_y,time)

        elif option == "left" and y_start_num == y_end_num and x_start_num > x_end_num:
            self.driver.swipe(start_x,start_y,end_x,end_y,time)

        elif option == "right" and y_start_num == y_end_num and x_start_num < x_end_num:
           self.driver.swipe(start_x,start_y,end_x,end_y,time)

    #根据desried_crap["automationName"] = "uniautomator2"
    # 中uniautomator是1还是2来选择按键方式
    def press_code(self,code,automationName=2):
        if automationName == 2:
            self.driver.press_keycode(code)
        elif automationName == 1:
            self.driver.keyevent(code)