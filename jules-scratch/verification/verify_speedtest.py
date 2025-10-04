import time
from playwright.sync_api import sync_playwright, Page, expect

def run_verification(page: Page):
    """
    Navigates to the web interface and verifies the speedtest feature.
    """
    # Navigate to the web interface
    page.goto("http://127.0.0.1:8787/web")

    # Wait for the table to load and for the status checks to run
    # We'll wait for a specific element to show a status other than "Checking..."
    # Let's give it a generous timeout
    page.wait_for_function("""
        () => {
            const statuses = Array.from(document.querySelectorAll('.status-cell'));
            return statuses.some(s => s.textContent !== 'Checking...');
        }
    """, timeout=15000)

    # Take a screenshot to verify the result
    page.screenshot(path="jules-scratch/verification/verification.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    run_verification(page)
    browser.close()

print("Verification script executed and screenshot taken.")