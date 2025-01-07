from playwright.sync_api import sync_playwright

URL = "https://www.thesun.co.uk/sport/football/"

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(URL)
    articles_content_xpath = "//div[contains(@class, 'teaser__copy-container')]"
    articles = page.locator(f"xpath={articles_content_xpath}").all()
    for article in articles:
        try:
            article_locator = article.locator("xpath=./a/h3")
            title = article_locator.text_content(timeout=100)
            print("Title: " + title)
        except Exception as e:
            print(e)
