import time


def test_check_choose_category(dashboard):
    dashboard.click_on_navbar()
    dashboard.choose_subcategory('Ремонт')
    time.sleep(5)