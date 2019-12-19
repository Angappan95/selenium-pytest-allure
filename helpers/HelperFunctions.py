def locate(driver, loc_value, locator='XPATH'):
    if isinstance(locator, str):
        locator = locator.upper()

    if locator == 'ID':
        return driver.find_element_by_id(loc_value)

    elif locator == 'NAME':
        return driver.find_element_by_name(loc_value)

    elif locator == 'LINK':
        return driver.find_element_by_link_text(loc_value)

    elif locator == 'PARTIALLINK':
        return driver.find_element_by_partial_link_text(loc_value)

    elif locator == 'CLASS':
        return driver.find_element_by_class_name(loc_value)

    elif locator == 'XPATH':
        return driver.find_element_by_xpath(loc_value)

    elif locator == 'CSS':
        return driver.find_element_by_css_selector(loc_value)
