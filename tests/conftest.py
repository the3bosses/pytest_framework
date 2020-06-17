import os
import sys
import pytest
from main_config import WebConfigsFirefox
from selenium import webdriver
from lib.utils import create_folder


CFG = WebConfigsFirefox


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    global local_driver

    def tear_down():
        local_driver.quit()

    web_page_driver = webdriver.Firefox(executable_path=CFG.driver_path)
    web_page_driver.maximize_window()
    web_page_driver.get(CFG.driver_url)
    local_driver = web_page_driver
    request.addfinalizer(tear_down)
    return local_driver


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     folder_name = 'screenshots'
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     create_folder(folder_name=folder_name)
#     if report.when == 'call' or report.when == 'setup':
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_").split("/")[1] + ".png"
#             file_name = f'{folder_name}/{file_name}'
#             local_driver.get_screenshot_as_file(filename=file_name)
#             #################################################
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '\
#                        'oneclick="` swindow.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#     report.extra = extra


