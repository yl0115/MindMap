from common.desired_caps import mind_desired
from common.functions import Common


class Home_Page(Common):

    def left_delete(self):
        self.find_path(self.abs_path('首页', 't')).click()
        text = self.find_path(self.class_path('.b', 't'))
        self.slide(text)
        self.find_path(self.abs_path('删除', 't')).click()



if __name__ == '__main__':
    driver = mind_desired()
    hp = Home_Page(driver)
    hp.left_delete()