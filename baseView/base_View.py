class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_element(*loc)

    def find_path(self, *loc):
        return self.driver.find_element_by_xpath(*loc)

    def find_paths(self, *loc):
        return self.driver.find_elements_by_xpath(*loc)

    def find_id(self, *loc):
        return self.driver.find_element_by_id(*loc)

    def find_ids(self, *loc):
        return self.driver.find_elements_by_id(*loc)

    def get_window_size(self):
        return self.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)


