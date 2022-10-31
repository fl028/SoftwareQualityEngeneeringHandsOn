import json
import pytest
import os

from screenplay.pattern import Actor
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def config(scope='session'):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.json')
    with open(path) as config_file:
        config = json.load(config_file)
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return config


@pytest.fixture
def browser(config: dict):
    if config['browser'] == 'Chrome':
        b = webdriver.Chrome(ChromeDriverManager().install())
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()


@pytest.fixture
def actor(browser: WebDriver):
    a = Actor()
    a.can_use(browser=browser)
    return a