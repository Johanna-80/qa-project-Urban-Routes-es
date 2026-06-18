import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.utilities import retrieve_phone_code


class UrbanRoutesPage:

    # ============================================================================
    # LOCATORS
    # ============================================================================

    # Route
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    # Phone
    phone_trigger = (By.CSS_SELECTOR, '.np-text')
    phone_modal_input = (By.ID, 'phone')
    phone_modal_confirm = (By.XPATH, "//button[contains(@class,'full') and text()='Siguiente']")
    phone_modal_confirm_code = (By.XPATH, "//button[contains(@class,'full') and text()='Confirmar']")

    # Payment
    payment_trigger = (By.CSS_SELECTOR, '.pp-text')
    payment_add_card_btn = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_input = (By.CSS_SELECTOR, 'input[name="number"].card-input')
    card_cvv_input = (By.CSS_SELECTOR, 'input[name="code"].card-input')
    card_add_button = (By.XPATH, "//button[text()='Agregar']")
    close_section = (By.CSS_SELECTOR, '.close-button.section-close')

    # Extras
    message_field = (By.ID, 'comment')
    blanket_switch = (By.CSS_SELECTOR, '.switch')
    ice_cream_plus = (By.CSS_SELECTOR, '.counter-plus')
    counter_value = (By.CSS_SELECTOR, '.counter-value')

    # Order
    order_header = (By.CSS_SELECTOR, '.order-header')
    driver_info_css = (By.CSS_SELECTOR, '.driver-info')

    # ============================================================================
    # INIT
    # ============================================================================

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ============================================================================
    # PRIVATE HELPERS
    # ============================================================================

    def _js_click(self, element):
        """Click con JavaScript para evitar ElementClickInterceptedException."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'}); arguments[0].click();", element)

    def _js_set_react(self, element, value):
        """Establece valor en input React usando nativeInputValueSetter + Tab."""
        self.driver.execute_script("""
            var setter = Object.getOwnPropertyDescriptor(
                window.HTMLInputElement.prototype, 'value').set;
            setter.call(arguments[0], arguments[1]);
            arguments[0].dispatchEvent(new Event('input', {bubbles: true}));
            arguments[0].dispatchEvent(new Event('change', {bubbles: true}));
            arguments[0].dispatchEvent(new KeyboardEvent('keyup', {bubbles: true}));
        """, element, value)
        element.send_keys(Keys.TAB)

    def _wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def _wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def _close_active_section(self):
        """Cierra el modal activo usando el botón close o Escape."""
        time.sleep(0.4)
        close_buttons = [btn for btn in self.driver.find_elements(*self.close_section)
                         if btn.is_displayed()]
        if close_buttons:
            self._js_click(close_buttons[0])
        else:
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(0.5)

    def _get_order_button(self):
        """Busca el botón de pedir taxi usando múltiples estrategias."""
        time.sleep(1)

        strategies = [
            (By.XPATH, "//button[contains(@class, 'smart-button') and contains(., 'Pedir')]"),
            (By.CSS_SELECTOR, '.smart-button'),
            (By.CSS_SELECTOR, '.order-button'),
            (By.XPATH, "//button[contains(@class, 'full') and contains(text(), 'Pedir')]"),
            (By.XPATH, "//button[contains(text(), 'Pedir')]"),
            (By.CSS_SELECTOR, '.button.round'),
        ]

        for by, selector in strategies:
            try:
                candidates = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located((by, selector)))
                visible = [btn for btn in candidates if btn.is_displayed() and btn.is_enabled()]
                if visible:
                    return visible[0]
            except Exception:
                continue

        # Último recurso: buscar por JavaScript
        script = """
        var elementos = document.querySelectorAll('button, div[role="button"]');
        for (var i = 0; i < elementos.length; i++) {
            if (elementos[i].textContent.includes('Pedir un taxi') &&
                elementos[i].offsetParent !== null) {
                return elementos[i];
            }
        }
        return null;
        """
        button = self.driver.execute_script(script)
        if button is None:
            raise RuntimeError("No se encontró el botón 'Pedir'")
        return button

    # ============================================================================
    # GETTERS
    # ============================================================================

    def get_from_field(self):
        return self._wait_clickable(self.from_field)

    def get_to_field(self):
        return self._wait_clickable(self.to_field)

    def get_request_taxi_button(self):
        return self._wait_clickable(self.request_taxi_button)

    def get_comfort_icon(self):
        return self._wait_clickable(self.comfort_icon)

    def get_phone_trigger(self):
        return self._wait_clickable(self.phone_trigger)

    def get_phone_modal_input(self):
        return self._wait_visible(self.phone_modal_input)

    def get_phone_modal_confirm(self):
        return self._wait_clickable(self.phone_modal_confirm)

    def get_phone_modal_confirm_code(self):
        return self._wait_clickable(self.phone_modal_confirm_code)

    def get_payment_trigger(self):
        return self._wait_clickable(self.payment_trigger)

    def get_payment_add_card(self):
        return self._wait_clickable(self.payment_add_card_btn)

    def get_card_number_input(self):
        return self._wait_visible(self.card_number_input)

    def get_card_cvv_input(self):
        return self._wait_visible(self.card_cvv_input)

    def get_card_add_button(self):
        return self._wait_clickable(self.card_add_button)

    def get_message_field(self):
        return self._wait_clickable(self.message_field)

    def get_blanket_switches(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.blanket_switch))

    def get_ice_cream_plus(self):
        return self._wait_clickable(self.ice_cream_plus)

    def get_counter_value(self):
        return self._wait_visible(self.counter_value)

    def get_order_header(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.order_header))

    def get_driver_info(self):
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.driver_info_css))

    # ============================================================================
    # SETTERS
    # ============================================================================

    def set_from(self, address):
        self.get_from_field().send_keys(address)

    def set_to(self, address):
        self.get_to_field().send_keys(address)

    def set_phone_number(self, phone):
        self.get_phone_modal_input().send_keys(phone)

    def set_otp_code(self, code):
        code_inputs = self.driver.find_elements(By.ID, 'code')
        otp = next(
            (c for c in code_inputs
             if c.is_displayed() and 'card-input' not in (c.get_attribute('class') or '')),
            None
        )
        if otp is None:
            raise RuntimeError("No se encontró el campo OTP visible")
        otp.send_keys(code)

    def set_card_number(self, number):
        self._js_set_react(self.get_card_number_input(), number)

    def set_card_cvv(self, cvv):
        self._js_set_react(self.get_card_cvv_input(), cvv)

    def set_message(self, message):
        self.get_message_field().send_keys(message)

    # ============================================================================
    # CLICKERS
    # ============================================================================

    def click_request_taxi(self):
        self.get_request_taxi_button().click()
        time.sleep(1)

    def click_comfort(self):
        self.get_comfort_icon().click()
        time.sleep(0.5)

    def click_phone_trigger(self):
        self.get_phone_trigger().click()
        time.sleep(0.8)

    def click_phone_confirm(self):
        self.get_phone_modal_confirm().click()
        time.sleep(1.5)

    def click_phone_confirm_code(self):
        self.get_phone_modal_confirm_code().click()
        time.sleep(0.8)

    def click_payment_trigger(self):
        self._js_click(self.get_payment_trigger())
        time.sleep(1)

    def click_payment_add_card(self):
        self._js_click(self.get_payment_add_card())
        time.sleep(1)

    def click_card_add_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.card_add_button)
        ).click()
        time.sleep(1)

    def click_blanket_switch(self):
        switches = self.get_blanket_switches()
        for switch in switches:
            if switch.is_displayed():
                self._js_click(switch)
                time.sleep(0.3)
                return
        raise RuntimeError("No se encontró ningún switch visible para manta y pañuelos")

    def click_ice_cream_plus(self):
        self._js_click(self._wait_clickable(self.ice_cream_plus))
        time.sleep(0.3)

    def click_order_button(self):
        button = self._get_order_button()
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", button)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)

    # ============================================================================
    # READERS
    # ============================================================================

    def get_from(self):
        return self.get_from_field().get_attribute('value')

    def get_to(self):
        return self.get_to_field().get_attribute('value')

    def get_ice_cream_count(self):
        return self.get_counter_value().text.strip()

    def is_order_header_visible(self):
        try:
            modal_selectors = [
                (By.CSS_SELECTOR, '.order-modal'),
                (By.CSS_SELECTOR, '.order-header'),
                (By.CSS_SELECTOR, '.driver-info'),
                (By.XPATH, "//div[contains(@class, 'order')]"),
            ]
            for by, selector in modal_selectors:
                try:
                    element = self.driver.find_element(by, selector)
                    if element.is_displayed():
                        return True
                except Exception:
                    continue
            return False
        except Exception:
            return False

    def is_driver_info_visible(self):
        try:
            return self.get_driver_info().is_displayed()
        except Exception:
            return False

    # ============================================================================
    # COMPOSITE ACTIONS
    # ============================================================================

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        time.sleep(0.4)
        self.set_to(to_address)
        time.sleep(0.8)

    def select_comfort_tariff(self):
        self.click_request_taxi()
        self.click_comfort()

    def fill_phone_number(self, phone):
        self.click_phone_trigger()
        self.set_phone_number(phone)
        self.click_phone_confirm()
        real_code = retrieve_phone_code(self.driver)
        self.set_otp_code(real_code)
        self.click_phone_confirm_code()
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(0.8)

    def add_credit_card(self, card_number, card_cvv):
        self.click_payment_trigger()
        self.click_payment_add_card()
        self.set_card_number(card_number)
        self.set_card_cvv(card_cvv)
        self.click_card_add_button()
        self._close_active_section()
        self._close_active_section()

    def add_message_for_driver(self, message):
        self.set_message(message)

    def request_blanket_and_tissues(self):
        self.click_blanket_switch()

    def order_ice_creams(self, quantity):
        for _ in range(quantity):
            self.click_ice_cream_plus()

    def request_taxi_final(self):
        time.sleep(1)
        self.click_order_button()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".order-modal, .order-header, .driver-info"))
            )
        except Exception:
            pass