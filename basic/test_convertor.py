import pytest

def select_option(page, role, name, index=1):
    options = page.get_by_role(role, name=name)
    if options.count() > index:
        options.nth(index).click()
    else:
        options.first.click()

@pytest.mark.parametrize("from_currency, to_currency, amount", [
    ("EUR", "AUD", "10"),
    ("RUB", "JPY", "100"),
])
def test_currency_conversion(page, from_currency, to_currency, amount):
    page.goto("https://finance.rambler.ru/calculators/converter/")

    page.locator("[data-finance_media-desktop='converter_first_select']").click()
    select_option(page, "option", from_currency, index=1)

    page.locator("[data-finance_media-desktop='converter_second_select']").click()
    select_option(page, "option", to_currency, index=1)

    page.locator("[data-finance_media-desktop='input']").click()
    page.locator("[data-finance_media-desktop='input']").fill(amount)

    page.locator("[data-finance_media-desktop='convert_link']").click()

    result = page.text_content('//*[@id="app"]/div[4]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]')
    result = result.replace(from_currency, f' {from_currency} ')
    result = result.replace(to_currency, f' = {to_currency} ')

    print(result)