def test_wiki(page):
    page.goto("https://en.wikipedia.org")
    assert page.title() == "Wikipedia, the free encyclopedia"