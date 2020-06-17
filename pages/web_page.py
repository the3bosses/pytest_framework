from lib.driver import Driver
from test_data.data_set import TestData


class Elements(object):
    register = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'  # element by xpath
    first_name = 'firstName'  # element by name
    last_name = 'lastName'  # element by name
    phone = 'phone'  # element by name
    email_address = 'userName'  # element by name
    address = 'address1'  # element by name
    city = 'city'  # element by name
    state_province = 'state'  # element by name
    postal_code = 'postalCode'  # element by name
    country = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[' \
              '5]/td/form/table/tbody/tr[11]/td[2]/select'  # element by name
    user_name = 'email'  # element by id
    password = 'password'  # element by name
    confirm_password = 'confirmPassword'  # element by name
    submit_query_btn = 'submit'  # element by name
    user_name_landing_page = 'userName'  # element by name
    password_landing_page = 'password'  # element by name
    submit_btn_landing_page = 'submit'  # element by name
    home_link = '/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[' \
                '2]/font/a '  # element by xpath



class Actions(object):
    def __init__(self, driver):
        self.elements = Elements()
        self.driver = Driver(driver=driver)
        self.data = TestData()

    def click_on_register_link(self):
        return self.driver.find_element_by_xpath(self.elements.register).click()

    def enter_first_name(self, value):
        self.driver.find_element_by_name(self.elements.first_name).click()
        return self.driver.find_element_by_name(self.elements.first_name).send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element_by_name(self.elements.last_name).click()
        return self.driver.find_element_by_name(self.elements.last_name).send_keys(value)

    def enter_phone_number(self, value):
        self.driver.find_element_by_name(self.elements.phone).click()
        return self.driver.find_element_by_name(self.elements.phone).send_keys(value)

    def enter_email_address(self, value):
        self.driver.find_element_by_name(self.elements.email_address).click()
        return self.driver.find_element_by_name(self.elements.email_address).send_keys(value)

    def enter_address(self, value):
        self.driver.find_element_by_name(self.elements.address).click()
        return self.driver.find_element_by_name(self.elements.address).send_keys(value)

    def enter_city(self, value):
        self.driver.find_element_by_name(self.elements.city).click()
        return self.driver.find_element_by_name(self.elements.city).send_keys(value)

    def enter_state_province(self, value):
        self.driver.find_element_by_name(self.elements.state_province).click()
        return self.driver.find_element_by_name(self.elements.state_province).send_keys(value)

    def enter_postal_code(self, value):
        self.driver.find_element_by_name(self.elements.postal_code).click()
        return self.driver.find_element_by_name(self.elements.postal_code).send_keys(value)

    def enter_country(self, value):
        self.driver.find_element_by_name(self.elements.country).click()
        return self.driver.find_element_by_name(self.elements.country).send_keys(value)

    def enter_user_name(self, value):
        self.driver.find_element_by_id(self.elements.user_name).click()
        return self.driver.find_element_by_id(self.elements.user_name).send_keys(value)

    def enter_password(self, value):
        self.driver.find_element_by_name(self.elements.password).click()
        return self.driver.find_element_by_name(self.elements.password).send_keys(value)

    def enter_confirm_password(self, value):
        self.driver.find_element_by_name(self.elements.confirm_password).click()
        return self.driver.find_element_by_name(self.elements.confirm_password).send_keys(value)

    def click_submit_btn(self):
        return self.driver.find_element_by_name(self.elements.submit_query_btn).click()

    def enter_user_name_landing_page(self, value):
        self.driver.find_element_by_name(self.elements.user_name_landing_page).click()
        return self.driver.find_element_by_name(self.elements.user_name_landing_page).send_keys(value)

    def enter_password_landing_page(self, value):
        self.driver.find_element_by_name(self.elements.password_landing_page).click()
        return self.driver.find_element_by_name(self.elements.password_landing_page).send_keys()

    def click_submit_btn_landing_page(self):
        return self.driver.find_element_by_name(self.elements.submit_btn_landing_page).click()

    def click_home_link(self):
        return self.driver.find_element_by_xpath(self.elements.home_link).click()

    def web_page(self):
        self.click_on_register_link()
        self.enter_first_name(value=self.data.register_first_name)
        self.enter_last_name(value=self.data.register_last_name)
        self.enter_phone_number(value=self.data.phone)
        self.enter_email_address(value=self.data.email_address)
        self.enter_address(value=self.data.address)
        self.enter_city(value=self.data.city)
        self.enter_state_province(value=self.data.state_province)
        self.enter_postal_code(value=self.data.postal_code)
        self.driver.drop_down_menu(element=self.elements.country, text=self.data.country_text)
        self.enter_user_name(value=self.data.username)
        self.enter_password(value=self.data.password)
        self.enter_confirm_password(value=self.data.password)
        self.click_submit_btn()
















