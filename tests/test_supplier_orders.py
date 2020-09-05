import pytest
from pages.supplier_orders import Actions as Orders

# pytestmark = pytest.mark.skip('Skipping Login Process')

# @pytest.mark.skip(reason='Skipping Login Process')


@pytest.fixture
def orders(driver, login):
    return Orders(driver=driver)


def test_supplier_orders(orders):
    orders.supplier_orders()
