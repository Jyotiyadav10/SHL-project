# crawl_shl.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# SHL product catalog URL
BASE_URL = "https://www.shl.com/products/product-catalog/"

def scrape_shl_catalog():
    options = Options()
    options.add_argument("--headless")       # Run browser in background
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(BASE_URL)
    time.sleep(5)  # Wait for JS content to load

    # Scroll and load all products
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for products to load

        # Click "Load More" button if present
        try:
            load_more = driver.find_element(By.XPATH, "//button[contains(text(),'Load More')]")
            load_more.click()
            time.sleep(3)
        except:
            pass

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Collect all product links
    product_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='/products/product-catalog/view/']")
    products = []
    seen_urls = set()

    for el in product_elements:
        try:
            name = el.text.strip()
            url = el.get_attribute("href")

            # Skip duplicates or Pre-packaged Job Solutions
            if not name or url in seen_urls or "Pre-packaged Job Solutions" in name:
                continue
            seen_urls.add(url)

            # Heuristic for category and test type
            if "Personality" in name or "Behavior" in name:
                test_type = "P"
                category = "Personality & Behavior"
            else:
                test_type = "K"
                category = "Knowledge & Skills"

            products.append({
                "name": name,
                "url": url,
                "category": category,
                "test_type": test_type
            })
        except:
            continue

    driver.quit()

    # Save to catalog.csv in the same backend folder
    df = pd.DataFrame(products)
    df.to_csv("catalog.csv", index=False)
    print(f"Saved {len(products)} products to catalog.csv")

if __name__ == "__main__":
    scrape_shl_catalog()
