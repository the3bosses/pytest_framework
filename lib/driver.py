from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class Driver(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_name(self, element, wait=15):
        self.explicit_wait(locator_type=By.NAME, locator_value=element, wait=wait)
        return self.driver.find_element_by_name(element)

    def find_element_by_class_name(self, element, wait=15):
        self.explicit_wait(locator_type=By.CLASS_NAME, locator_value=element, wait=wait)
        return self.driver.find_element_by_class_name(element)

    def find_element_by_id(self, element, wait=15):
        self.explicit_wait(locator_type=By.ID, locator_value=element, wait=wait)
        return self.driver.find_element_by_id(element)

    def find_element_by_xpath(self, element, wait=15):
        self.explicit_wait(locator_type=By.NAME, locator_value=element, wait=wait)
        return self.driver.find_element_by_xpath(element)

    def find_element_by_css(self, element, wait=15):
        self.explicit_wait(locator_type=By.CSS_SELECTOR, locator_value=element, wait=wait)
        return self.driver.find_element_by_css(element)

    def find_element_by_link_text(self, element, wait=15):
        self.explicit_wait(locator_type=By.LINK_TEXT, locator_value=element, wait=wait)
        return self.driver.find_element_by_link_text(element)

    def find_element_by_tag_name(self, element, wait=15):
        self.explicit_wait(locator_type=By.TAG_NAME, locator_value=element, wait=wait)
        return self.driver.find_element_by_tag_name(element)

    def find_element_by_partial_link_text(self, element, wait=15):
        self.explicit_wait(locator_type=By.PARTIAL_LINK_TEXT, locator_value=element, wait=wait)
        return self.driver.find_element_by_partial_link_text(element)

    def refresh_page(self):
        return self.driver.refresh()

    def close_browser(self):
        return self.driver.quit()

    def new_tab(self, script):
        return self.driver.execute_scripts(script)

    def drop_down_menu(self, element, text):
        select = Select(self.driver.find_element_by_xpath(element))
        select.select_by_visible_text(text)

    def explicit_wait(self, locator_type, locator_value, wait):
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.presence_of_all_elements_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            pass

