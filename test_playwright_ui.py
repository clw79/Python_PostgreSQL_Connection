from playwright.sync_api import Page


def test_example_site_loads(page: Page):
    page.goto("https://example.com")

    assert "Example Domain" in page.title()
    assert page.locator("h1").inner_text() == "Example Domain"
