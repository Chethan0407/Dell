from .BasePage import BasePage
from playwright.sync_api import  Page


class SearchPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)
        self.search_box_selector = '#mh-search-input'
        self.search_button_selector = 'button.mh-search-btn.mh-search-submit[aria-label="Search Dell"]'
        self.add_to_cart_button_selector = '//a[@aria-label="Buy Now New XPS 13 Laptop"]'

    def search_product(self, productname):
        self.page.fill(self.search_box_selector, productname)
        self.click(self.search_button_selector)

    def add_product(self):
        self.click(self.add_to_cart_button_selector)

