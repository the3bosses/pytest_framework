import time
import pyautogui
from test_data.account_data import TestData
from lib.driver import Driver
from lib.utils import db_connection, select_query_builder2

class Elements(object):
    stock_menu = "Stock"
    orders_button = "Orders"
    account_radio_button = "rbnAccount"
    select_button = "btnOk"
    insert_button = "Insert"
    continue_button = "btnContinue"
    find_button = "btnFind"
    enter_product_name = "txtString"
    enter_product_quantity = "txtQuantity"
    find_next_item = "btnNextItem"
    update_button = "btnUpdate"
    yes_button = "6"
    no_button = "7"
    supplier_order_number = "Order No. Row 0"
    close_button = "Close"
    transactions = "Transactions"
    supplier_receipts = "Supplier Receipts"
    order_number = "txtOrderNo"
    reference_number1 = "txtReference"
    reference_number2 = "txtReference2"
    check_box = "chkBTN"
    total_amount = "txtTotalAmount"
    scrape_total = "/*[@ClassName='WindowsForms10.EDIT.app.0.141b42a_r9_ad1' and @ControlType='ControlType.Edit']"


class Expects(object):
    @staticmethod
    def run_query(query):
        query_results = db_connection(query=query)
        results = [row for row in query_results]
        return results
    


class Actions(Expects):
    def __init__(self, driver):
        self.elements = Elements()
        self.driver = Driver(driver=driver)
        self.data = TestData()

    def click_stock_menu(self):
        return self.driver.find_element_by_name(self.elements.stock_menu).click()

    def click_orders_button(self):
        return self.driver.find_element_by_name(self.elements.orders_button).click()

    @staticmethod
    def click_radio_option():
        return pyautogui.click(418, 791)
        # return self.driver.find_element_by_id(self.elements.account_radio_button).click()

    @staticmethod
    def click_txt_box(value):
        pyautogui.click(345, 816)
        return pyautogui.typewrite(value)
        # self.driver.find_element_by_id(self.elements.enter_product_name).click()
        # return self.driver.find_element_by_id(self.elements.enter_product_name).send_key(value)
        
    def click_select_button(self):
        return self.driver.find_element_by_id(self.elements.select_button).click()

    @staticmethod
    def click_insert_button():
        return pyautogui.click(195, 1204)
        # return self.driver.find_element_by_name(self.elements.insert_button).click()

    def click_continue_button(self):
        return self.driver.find_element_by_id(self.elements.continue_button).click()

    def enter_product_name(self, value):
        return self.driver.find_element_by_id(self.elements.enter_product_name).send_keys(value)

    @staticmethod
    def product_quantity(value):
        # self.driver.find_element_by_id(self.elements.enter_product_quantity).clear()
        pyautogui.doubleClick(422, 820)
        return pyautogui.typewrite(value)


    def click_find_button(self):
        for product in self.data.product_names:
            self.driver.find_element_by_id(self.elements.find_button).click()
            self.enter_product_name(value=product)
            self.click_select_button()
            self.product_quantity(value=self.data.supplier_order_product_quantity)
            self.driver.find_element_by_id(self.elements.find_next_item).click()
        return ""

    def click_accept(self):
        return self.driver.find_element_by_id(self.elements.select_button).click()

    def click_update_button(self):
        return self.driver.find_element_by_id(self.elements.update_button).click()

    def click_yes_button(self):
        return self.driver.find_element_by_id(self.elements.yes_button).click()

    def click_no_button(self):
        return self.driver.find_element_by_id(self.elements.no_button).click()

    @staticmethod
    def click_close_button():
        pyautogui.click(871, 1208)
        # return self.driver.find_element_by_name(self.elements.close_button).click()

    def click_radio_button(self):
        return self.driver.find_element_by_id(self.elements.account_radio_button).click()

    def click_text_field(self, value):
        self.driver.find_element_by_id(self.elements.enter_product_name).click()
        self.driver.find_element_by_id(self.elements.enter_product_name).send_keys(value)

    def order_number_text(self, value):
        return self.driver.find_element_by_id(self.elements.order_number).send_keys(value)

    def transaction_option(self):
        return self.driver.find_element_by_name(self.elements.transactions).click()

    def supplier_receipts_option(self):
        return self.driver.find_element_by_name(self.elements.supplier_receipts).click()

    def enter_reference1(self, value):
        return self.driver.find_element_by_id(self.elements.reference_number1).send_keys(value)

    def enter_reference2(self, value):
        return self.driver.find_element_by_id(self.elements.reference_number2).send_keys(value)

    def click_check_box(self):
        return self.driver.find_element_by_id(self.elements.check_box).click()

    def enter_total_amount(self, value):
        self.driver.find_element_by_id(self.elements.total_amount).clear()
        return self.driver.find_element_by_id(self.elements.total_amount).send_keys(value)

    # @staticmethod
    # def scrape_total():
    #     pyautogui.doubleClick(882, 276)
    #     return pyautogui.hotkey('ctrl', 'c')
        
        
    def supplier_orders(self):
        time.sleep(5)
        self.click_stock_menu()
        self.click_orders_button()
        time.sleep(2)
        self.click_radio_option()
        time.sleep(2)
        self.click_txt_box(value=self.data.creditor_code[0])
        self.click_select_button()
        time.sleep(3)
        self.click_insert_button()
        self.click_continue_button()
        self.click_find_button()
        self.click_accept()
        scrape = self.driver.get_attribute_by_id(element=self.elements.total_amount, attribute='value')
        time.sleep(3)
        self.click_update_button()
        self.click_yes_button()
        self.click_no_button()
        self.click_no_button()
        self.click_close_button()
        query = select_query_builder2("ORDNO",
         "[POSWINSQL_PTA_QA].[dbo].[CRORDHD]",
         "WHERE ACCOUNT = '3' AND ODATE = Convert(DATE, GetDate())", 
          "DESC"
          )
        result = self.run_query(query=query)
        self.click_stock_menu()
        self.transaction_option()
        self.supplier_receipts_option()
        self.click_radio_button()
        self.click_text_field(value=self.data.creditor_code)
        self.click_select_button()
        self.order_number_text(value=result[0])
        self.enter_reference1(value="651000")
        self.enter_reference2(value="100")
        self.click_check_box()
        self.enter_total_amount(scrape)
        self.click_continue_button()
        return result


        # time.sleep(10)

# SELECT TOP 10 ORDNO FROM [POSWINSQL_PTA_QA].[dbo].[CRORDHD] 
# WHERE ACCOUNT = '3' AND ODATE = Convert(DATE, GetDate())
# ORDER BY ORDNO DESC;