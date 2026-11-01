#!/usr/bin/env python3
"""Apify vs ScraperAPI Google Shopping TCO Calculator 2026."""
import argparse

def calculate(serp_pages=50000):
    # Apify: Platform compute unit model. $49/mo starter includes $49 platform credits.
    # Google Shopping Actor consumes ~$4.00 per 1k full SERP queries -> 50k queries = $200.00/mo.
    apify_total = (serp_pages / 1000.0) * 4.00

    # ScraperAPI: Google Shopping SERP queries consume 5 credits per page.
    # 50k queries * 5 credits = 250,000 credits. Covered by Hobby ($44.10/mo) or Startup ($134.10/mo).
    scraperapi_total = 44.10 if (serp_pages * 5) <= 100000 else 134.10

    diff = apify_total - scraperapi_total

    print("=" * 65)
    print(f"Apify vs ScraperAPI: {serp_pages:,} Google Shopping Pages")
    print("=" * 65)
    print(f"Apify Actor Total:         ${apify_total:.2f}/mo (@$4.00/1k SERPs)")
    print(f"ScraperAPI Direct API:     ${scraperapi_total:.2f}/mo (Startup Plan)")
    print(f"Monthly Savings:           ${diff:.2f}/mo ({'ScraperAPI Cheaper' if diff > 0 else 'Apify Cheaper'})")
    print("=" * 65)
    return scraperapi_total, apify_total

if __name__ == "__main__":
    calculate()
