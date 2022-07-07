import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_is(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector('button.btn-add-to-basket'), 'No button'
    time.sleep(30)
    
