from playwright.sync_api import Page, expect


def test_wiki1(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='English').click()
    expect(page.get_by_text('Welcome to Wikipedia,')).to_be_visible()
    # pytest --headed


def test_wiki2(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='English').click()
    page.locator('#ca-talk').click()
    expect(page.locator('#firstHeading')).to_have_text('Talk:Main Page')
    expect(page.get_by_text('Talk:Main Page')).to_be_visible()
