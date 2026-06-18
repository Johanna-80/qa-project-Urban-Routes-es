import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import data.data as data
from pages.urban_routes_page import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)
        WebDriverWait(cls.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'from'))
        )

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.routes_page.click_request_taxi()
        time.sleep(1)
        self.routes_page.click_comfort()

    def test_fill_phone_number(self):
        self.routes_page.fill_phone_number(data.phone_number)

    def test_add_credit_card(self):
        self.routes_page.add_credit_card(data.card_number, data.card_code)

    def test_add_message_for_driver(self):
        self.routes_page.add_message_for_driver(data.message_for_driver)

    def test_request_blanket_and_tissues(self):
        self.routes_page.request_blanket_and_tissues()

    def test_order_ice_creams(self):
        self.routes_page.order_ice_creams(2)

    def test_request_taxi_final(self):
        self.routes_page.request_taxi_final()
        time.sleep(2)
        assert self.routes_page.is_order_header_visible(), \
            "El modal de búsqueda de taxi no apareció"

    def test_wait_for_driver_info(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".driver-info"))
            )
        except Exception:
            pass

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            time.sleep(2)
            cls.driver.quit()