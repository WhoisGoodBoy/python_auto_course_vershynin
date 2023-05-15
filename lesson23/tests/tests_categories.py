import time


def test_check_choose_category(dashboard):
    dashboard.click_on_navbar()
    time.sleep(1)
    pick_subcategory = dashboard.choose_subcategory('Ремонт')
    time.sleep(1)
    building_subcat = pick_subcategory.choose_building_materials_section()
    time.sleep(1)


def test_check_login(dashboard):
    login = dashboard.login_form()
    login.fill_row('test@gmail.com', '123445hjgj')
    time.sleep(5)