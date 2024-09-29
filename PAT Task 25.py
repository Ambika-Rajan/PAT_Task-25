from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Set the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the IMDb search page
    driver.get("https://www.imdb.com/search/name/")

    # Step 2: Wait for the input fields to be present and fill them out
    # Example: Fill in "Tom Hanks" in the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name_search"))
    )
    search_box.send_keys("Tom Hanks")

    # Optionally select other fields, such as gender or known for, if available
    # For this example, let's just proceed with the search

    # Step 3: Submit the search
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    search_button.click()

    # Optional: Wait for the results page to load and verify the results
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "findResult"))
    )
    print("Search completed. Results found:", len(results))

finally:
    # Close the browser
    driver.quit()
