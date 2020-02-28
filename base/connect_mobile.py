from appium import webdriver


class TestConnetMobile:

    def connectMobile(self):
        desried_crap={}
        #设备信息
        desried_crap["platformName"] = "Android"
        desried_crap["platformVersion"] ="5.1"
        desried_crap["deviceName"] = "192.168.161.101:5555"
        #app信息  desried_crap["automationName"] = "uniautomator2"
        desried_crap["appPackage"] = "com.cyanogenmod.filemanager"
        desried_crap["appActivity"] = ".activities.NavigationActivity"
        #可以检测toast
        desried_crap["automationName"] = "uniautomator2"
        #可以输入中文
        desried_crap["unicodeKeyboard"] = True
        desried_crap["resetKeyboard"] = True
        #不重置应用默认是False
        desried_crap["noReset"] = True

        return webdriver.Remote("http://localhost:4723/wd/hub",desried_crap)




