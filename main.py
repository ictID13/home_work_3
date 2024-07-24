import pytest, time
from selene import browser,  have

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    #browser.config.base_url = 'https://duckduckgo.com/'
    browser.config.timeout = 10
    browser.config.driver_name = ('firefox')

def test_duckduck_find_text():
    browser.open('https://duckduckgo.com/')
    browser.element('.searchbox_input__bEGm3').type('QAGURU').press_enter()
    browser.element('.react-results--main').should(have.text('это крутые знания прямиком'))


def test_habr_find ():
    browser.open('https://habr.com/ru/articles/762532/')
    browser.element('.tm-header-user-menu__search').click()
    browser.element('.tm-input-text-decorated__input').type('mail.ru').press_enter()
    time.sleep(3)
    browser.element('.tm-articles-list__item').should(have.text('Spark в Kubernetes'))