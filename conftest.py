import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: [chrome/firefox]")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: [en/ru/es/fr/de]")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    user_language = None
    if language_name.lower() == 'ru':
        user_language = 'ru'
        print('\nLanguage: Русский')
    elif language_name.lower() == 'en':
        user_language = 'en-gb'
        print('\nLanguage: English')
    elif language_name.lower() == 'es':
        user_language = 'es'
        print('\nLanguage: Spanish')
    elif language_name.lower() == 'fr':
        user_language = 'fr'
        print('\nLanguage: French')
    elif language_name.lower() == 'de':
        user_language = 'de'
        print('\nLanguage: Deutsch')
    else:
        raise pytest.UsageError('\nUnknown language! Ru or En expected.\n')
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name.lower() == 'chrome':
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print('Start Google Chrome browser...\n')
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print('Star Mozilla Firefox browser...\n')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('\nUnknown browser! Chrome or Firefox expected.\n')
    yield browser

    print(f'\nQuit {browser_name} browser.\n')
    browser.quit()
