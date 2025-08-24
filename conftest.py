import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1280
    browser.config.window_height = 800
    yield
    browser.quit()