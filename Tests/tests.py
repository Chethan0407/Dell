import pytest
from playwright.sync_api import sync_playwright
from Utils.config import BASE_URL
from Utils.data import PRODUCT_NAME
from Pages.SearchPage import SearchPage


def test_add_to_search_page(page):
    search_page = SearchPage(page)
    search_page.goto(BASE_URL)
    search_page.search_product(PRODUCT_NAME)
    search_page.add_product()



