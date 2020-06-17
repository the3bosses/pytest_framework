import pytest
from pages.web_page import Actions as Navigate


@pytest.fixture
def navigate(driver):
    return Navigate(driver=driver)


def test_web_page(navigate):
    return navigate.web_page()

