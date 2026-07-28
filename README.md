# Spree Commerce QA Project

Manual and automated QA testing for [Spree Commerce](https://demo.spreecommerce.org) — an open-source e-commerce storefront — covering the customer-facing (storefront) flows: Login, Sign Up, Catalog, Cart, and Checkout.

## What's in this repo

- **`Manual_Test_Plan.xlsx`** — Full manual QA artifact: test plan, 73 test cases across 5 modules, and a bug tracker with 20 logged defects (severity, priority, and reproduction steps).
- **`pages/`** — Page Object Model classes for the automated suite (Login, Sign Up, Checkout).
- **`tests/`** — Playwright (Python/pytest) automated tests covering Login, Sign Up, Cart, and Checkout end-to-end, including two payment methods (Stripe card, Affirm).

## Approach

Testing was scoped to storefront-only functionality (no admin backend access). Manual testing came first — test plan, test case design (equivalence partitioning / boundary value analysis), execution, and defect logging — followed by Playwright automation of the highest-value flows using Page Object Model for maintainability.

### Notable findings
- A checkout subtotal miscalculation causing incorrect order totals
- A data integrity issue where a deleted checkout field's stale value persisted through to the order confirmation
- A sitewide gap in email format validation (no format enforced anywhere on signup/checkout)

## Tech stack

- **Manual testing:** Test plan, EP/BVA test design, bug tracking (Excel)
- **Automation:** Playwright, pytest, Python
- **Pattern:** Page Object Model

## Running the tests

```bash
pip install pytest-playwright
playwright install
python -m pytest tests/
```
Link to test cases: https://docs.google.com/spreadsheets/d/1xw4wxgtClK5H6X7W6VnqHZ-GJzTQN2kd9ODi8kh4lxE/edit?usp=sharing
