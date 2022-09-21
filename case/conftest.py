import pytest
import sys, os
import datetime
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from api import public_api
from tools import read_json
from tools import dispose_method
from py._xmlgen import html



@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    # cells.insert(1,html.th("Test_nodeid"))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td((datetime.datetime.now() + datetime.timedelta(minutes=0)).strftime("%Y-%m-%d %H:%M:%S"), class_='col-time'))
    # cells.insert(1,html.td(report.nodeid))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='session')
def _api():
    """全局变量requests"""

    return public_api.PkApi()


@pytest.fixture(scope='session')
def _methods():
    """全局变量 公共方法"""

    return dispose_method.Methods()


@pytest.fixture(scope='session')
def _domain():
    """全局变量 活动域名"""
    return read_json.ReadJson("service_configuration.json").read_json()["activity_admin_domain"]["url"]


