import os
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"file://{os.getcwd()}/index.html")
    # Take a screenshot of the login screen first
    page.screenshot(path="jules-scratch/verification/login_screen.png")
    page.locator("#login-email").fill("admin@merlacol.co")
    page.locator("#login-password").fill("123456")
    page.locator("#login-role").select_option("Administrativo")
    # Use a more specific selector for the login button
    page.locator("#screen-login button[type='submit']").click()
    # Wait for the dashboard to be visible
    page.wait_for_selector("#screen-dashboard")
    page.screenshot(path="jules-scratch/verification/dashboard_screen.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
