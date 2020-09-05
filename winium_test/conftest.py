import os
import sys
import pytest
from pages.login import Actions as Login
from main_config import Configs
from selenium import webdriver
from lib.utils import create_folder


here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, here)

CFG = Configs()


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    global local_driver

    def tear_down():
        os.system("taskkill /f /im {0}".format(CFG.app_name))
        os.system("taskkill /f /im {0}".format(CFG.driver_name))

    os.system("taskkill /f /im {0}".format(CFG.driver_name))
    os.system("start /MIN {0} --verbose".format(CFG.driver_name))
    local_driver = webdriver.Remote(
        command_executor=CFG.driver_url,
        desired_capabilities={'app': CFG.app_path}
    )
    request.addfinalizer(tear_down)
    return local_driver


@pytest.fixture(scope="module", autouse=True)
def login():
    _login = Login(driver=local_driver)
    return _login.login()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    folder_name = 'screenshots'
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    create_folder(folder_name=folder_name)
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_").split("/")[1] + ".png"
            file_name = f'{folder_name}/{file_name}'
            local_driver.get_screenshot_as_file(filename=file_name)
            ################################################
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '\
                       'onclick="` swindow.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
    report.extra = extra



