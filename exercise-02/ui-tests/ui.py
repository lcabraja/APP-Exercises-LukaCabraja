from playwright.sync_api import Playwright, sync_playwright
import pytest

@pytest.fixture(scope="module")
def playwright() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright

def test_search_algebra(playwright):
    with playwright.chromium.launch(headless=False) as browser:
        page = browser.new_page()
        page.goto("https://www.google.com/")
        page.wait_for_selector('//*[@id="W0wltc"]')
        page.click('//*[@id="W0wltc"]')
        page.fill('input[name="q"]', "algebra")
        page.press('input[name="q"]', "Enter")
        page.wait_for_selector('a[href="https://www.algebra.hr/"]')
        assert page.inner_text('.eKjLze > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3') == "Algebra: Naslovnica"

def test_incorrect_login(playwright):
    with playwright.chromium.launch(headless=False) as browser:
        page = browser.new_page()
        page.goto("https://student.racunarstvo.hr/")
        page.fill('input[id="username"]', "incorrect_username")
        page.fill('input[id="pass"]', "incorrect_password")
        page.click('input[value="Prijava"]')
        page.wait_for_selector('//*[@id="form_login"]/div/center/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td')
        assert page.inner_text('//*[@id="form_login"]/div/center/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td') == "Greska 001: Korisničko ime i/ili lozinka nije točna."