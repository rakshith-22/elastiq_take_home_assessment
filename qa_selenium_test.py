import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/selenium-playgroundb /table-sort-search-demo")
driver.maximize_window()

# Get total entries count from the info text
info_text = driver.find_element(By.ID, "example_info").text
total_entries_count = int(info_text.split("of")[-1].strip().split(" ")[0])

# Assertion 1: Check if total records are 24
assert total_entries_count == 24, f"Expected total records to be 24, but found {total_entries_count}"
print(f"Assertion passed: Total records are {total_entries_count}")

# Check if table is present
table = driver.find_element(By.ID, "example")
assert table.is_displayed(), "Assertion failed: Table is not visible on the page."
print("Assertion passed: Table is displayed.")

# Search for "New York"
search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
assert search_box.is_displayed(), "Assertion failed: Search box is not visible."
search_box.clear()
search_box.send_keys("New York")
driver.implicitly_wait(3)

# Get filtered rows
table_rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")

# Assertion 2: Check if 5 rows are displayed after searching
assert len(table_rows) == 5, f"Expected 5 rows after search, but found {len(table_rows)}"
print("Assertion passed: Exactly 5 rows are displayed after search.")

# Assertion 3: Verify "New York" is present in all filtered rows
for row in table_rows:
    assert "New York" in row.text, f"Assertion failed: 'New York' not found in row: {row.text}"
print("Assertion passed: All filtered rows contain 'New York'.")

driver.quit()
