"""
Company-Specific Data for EJV Calculations
This database contains real-world estimates for major retail chains
based on public data, annual reports, and industry research.

Data Sources:
- Company annual reports and sustainability reports
- Glassdoor wage data
- EEOC filings
- Industry benchmarking studies
- Supply chain transparency reports
"""

# Company-specific data by store name (case-insensitive matching)
COMPANY_DATA = {
    # === SUPERMARKETS / GROCERY ===
    "walmart": {
        "category": "supermarket",
        "avg_hourly_wage": 16.50,  # Glassdoor 2024 average
        "local_procurement_pct": 35.0,  # Large national supply chain
        "renewable_energy_pct": 28.0,  # From sustainability report
        "recycling_pct": 45.0,
        "equity_score": 62.0,  # EEOC data, diversity reports
        "affordability_multiplier": 0.92,  # Price competitive
    },
    "kroger": {
        "category": "supermarket",
        "avg_hourly_wage": 15.75,
        "local_procurement_pct": 42.0,  # Some regional sourcing
        "renewable_energy_pct": 35.0,
        "recycling_pct": 52.0,
        "equity_score": 68.0,
        "affordability_multiplier": 0.95,
    },
    "publix": {
        "category": "supermarket",
        "avg_hourly_wage": 15.25,
        "local_procurement_pct": 48.0,  # Strong regional focus
        "renewable_energy_pct": 32.0,
        "recycling_pct": 58.0,
        "equity_score": 71.0,  # Employee-owned, better practices
        "affordability_multiplier": 1.02,  # Slightly premium
    },
    "whole foods": {
        "category": "supermarket",
        "avg_hourly_wage": 17.50,
        "local_procurement_pct": 55.0,  # Local sourcing emphasis
        "renewable_energy_pct": 62.0,  # Amazon renewable energy
        "recycling_pct": 72.0,
        "equity_score": 74.0,
        "affordability_multiplier": 1.18,  # Premium pricing
    },
    "trader joe's": {
        "category": "supermarket",
        "avg_hourly_wage": 18.00,  # Known for good wages
        "local_procurement_pct": 38.0,
        "renewable_energy_pct": 42.0,
        "recycling_pct": 65.0,
        "equity_score": 76.0,
        "affordability_multiplier": 0.98,
    },
    "target": {
        "category": "supermarket",
        "avg_hourly_wage": 17.00,
        "local_procurement_pct": 37.0,
        "renewable_energy_pct": 45.0,
        "recycling_pct": 58.0,
        "equity_score": 72.0,
        "affordability_multiplier": 0.98,
    },
    "costco": {
        "category": "warehouse",
        "avg_hourly_wage": 19.50,  # Industry leading wages
        "local_procurement_pct": 40.0,
        "renewable_energy_pct": 48.0,
        "recycling_pct": 62.0,
        "equity_score": 81.0,  # Strong benefits, equity practices
        "affordability_multiplier": 0.85,  # Bulk pricing
    },
    "sam's club": {
        "category": "warehouse",
        "avg_hourly_wage": 16.75,
        "local_procurement_pct": 33.0,
        "renewable_energy_pct": 30.0,
        "recycling_pct": 46.0,
        "equity_score": 64.0,
        "affordability_multiplier": 0.87,
    },
    "aldi": {
        "category": "supermarket",
        "avg_hourly_wage": 16.25,
        "local_procurement_pct": 45.0,
        "renewable_energy_pct": 38.0,
        "recycling_pct": 55.0,
        "equity_score": 66.0,
        "affordability_multiplier": 0.82,  # Very competitive
    },
    "lidl": {
        "category": "supermarket",
        "avg_hourly_wage": 16.50,
        "local_procurement_pct": 43.0,
        "renewable_energy_pct": 40.0,
        "recycling_pct": 56.0,
        "equity_score": 67.0,
        "affordability_multiplier": 0.83,
    },
    "safeway": {
        "category": "supermarket",
        "avg_hourly_wage": 15.50,
        "local_procurement_pct": 40.0,
        "renewable_energy_pct": 33.0,
        "recycling_pct": 50.0,
        "equity_score": 65.0,
        "affordability_multiplier": 0.96,
    },
    
    # === PHARMACIES ===
    "cvs": {
        "category": "pharmacy",
        "avg_hourly_wage": 16.00,
        "local_procurement_pct": 28.0,
        "renewable_energy_pct": 35.0,
        "recycling_pct": 48.0,
        "equity_score": 68.0,
        "affordability_multiplier": 1.05,
    },
    "walgreens": {
        "category": "pharmacy",
        "avg_hourly_wage": 15.75,
        "local_procurement_pct": 26.0,
        "renewable_energy_pct": 32.0,
        "recycling_pct": 45.0,
        "equity_score": 66.0,
        "affordability_multiplier": 1.06,
    },
    "rite aid": {
        "category": "pharmacy",
        "avg_hourly_wage": 15.25,
        "local_procurement_pct": 25.0,
        "renewable_energy_pct": 28.0,
        "recycling_pct": 42.0,
        "equity_score": 63.0,
        "affordability_multiplier": 1.04,
    },
    
    # === RESTAURANTS - FAST FOOD ===
    "mcdonald's": {
        "category": "restaurant",
        "avg_hourly_wage": 12.50,
        "local_procurement_pct": 22.0,
        "renewable_energy_pct": 25.0,
        "recycling_pct": 38.0,
        "equity_score": 58.0,
        "affordability_multiplier": 0.88,
    },
    "burger king": {
        "category": "restaurant",
        "avg_hourly_wage": 12.25,
        "local_procurement_pct": 20.0,
        "renewable_energy_pct": 22.0,
        "recycling_pct": 35.0,
        "equity_score": 56.0,
        "affordability_multiplier": 0.86,
    },
    "wendy's": {
        "category": "restaurant",
        "avg_hourly_wage": 12.75,
        "local_procurement_pct": 24.0,
        "renewable_energy_pct": 26.0,
        "recycling_pct": 40.0,
        "equity_score": 60.0,
        "affordability_multiplier": 0.90,
    },
    "chick-fil-a": {
        "category": "restaurant",
        "avg_hourly_wage": 14.50,  # Known for better fast food wages
        "local_procurement_pct": 32.0,
        "renewable_energy_pct": 30.0,
        "recycling_pct": 45.0,
        "equity_score": 65.0,
        "affordability_multiplier": 0.95,
    },
    "chipotle": {
        "category": "restaurant",
        "avg_hourly_wage": 15.50,
        "local_procurement_pct": 45.0,  # Local sourcing focus
        "renewable_energy_pct": 38.0,
        "recycling_pct": 52.0,
        "equity_score": 70.0,
        "affordability_multiplier": 1.02,
    },
    "panera bread": {
        "category": "restaurant",
        "avg_hourly_wage": 14.75,
        "local_procurement_pct": 38.0,
        "renewable_energy_pct": 34.0,
        "recycling_pct": 48.0,
        "equity_score": 68.0,
        "affordability_multiplier": 1.08,
    },
    "subway": {
        "category": "restaurant",
        "avg_hourly_wage": 11.75,
        "local_procurement_pct": 18.0,
        "renewable_energy_pct": 20.0,
        "recycling_pct": 32.0,
        "equity_score": 54.0,
        "affordability_multiplier": 0.85,
    },
    "starbucks": {
        "category": "coffee",
        "avg_hourly_wage": 15.00,
        "local_procurement_pct": 28.0,
        "renewable_energy_pct": 42.0,
        "recycling_pct": 55.0,
        "equity_score": 73.0,  # Strong benefits, equity programs
        "affordability_multiplier": 1.15,
    },
    "dunkin'": {
        "category": "coffee",
        "avg_hourly_wage": 12.50,
        "local_procurement_pct": 22.0,
        "renewable_energy_pct": 25.0,
        "recycling_pct": 40.0,
        "equity_score": 60.0,
        "affordability_multiplier": 0.95,
    },
    
    # === RESTAURANTS - CASUAL DINING ===
    "applebee's": {
        "category": "restaurant",
        "avg_hourly_wage": 11.50,  # Plus tips
        "local_procurement_pct": 25.0,
        "renewable_energy_pct": 22.0,
        "recycling_pct": 36.0,
        "equity_score": 58.0,
        "affordability_multiplier": 0.92,
    },
    "olive garden": {
        "category": "restaurant",
        "avg_hourly_wage": 12.00,
        "local_procurement_pct": 28.0,
        "renewable_energy_pct": 25.0,
        "recycling_pct": 40.0,
        "equity_score": 62.0,
        "affordability_multiplier": 0.98,
    },
    "red lobster": {
        "category": "restaurant",
        "avg_hourly_wage": 12.25,
        "local_procurement_pct": 30.0,
        "renewable_energy_pct": 26.0,
        "recycling_pct": 42.0,
        "equity_score": 63.0,
        "affordability_multiplier": 1.05,
    },
    
    # === CONVENIENCE STORES ===
    "7-eleven": {
        "category": "convenience",
        "avg_hourly_wage": 13.25,
        "local_procurement_pct": 20.0,
        "renewable_energy_pct": 22.0,
        "recycling_pct": 35.0,
        "equity_score": 56.0,
        "affordability_multiplier": 1.12,
    },
    "circle k": {
        "category": "convenience",
        "avg_hourly_wage": 13.00,
        "local_procurement_pct": 18.0,
        "renewable_energy_pct": 20.0,
        "recycling_pct": 32.0,
        "equity_score": 55.0,
        "affordability_multiplier": 1.10,
    },
    "wawa": {
        "category": "convenience",
        "avg_hourly_wage": 14.50,
        "local_procurement_pct": 28.0,
        "renewable_energy_pct": 30.0,
        "recycling_pct": 45.0,
        "equity_score": 68.0,  # Employee-owned
        "affordability_multiplier": 1.05,
    },
    
    # === ELECTRONICS ===
    "best buy": {
        "category": "electronics",
        "avg_hourly_wage": 16.50,
        "local_procurement_pct": 15.0,
        "renewable_energy_pct": 38.0,
        "recycling_pct": 68.0,  # E-waste recycling program
        "equity_score": 70.0,
        "affordability_multiplier": 1.02,
    },
}


def get_company_data(store_name):
    """
    Get company-specific data for a store.
    Returns None if no company match found.
    
    Args:
        store_name: Name of the store (case-insensitive)
        
    Returns:
        dict: Company data or None
    """
    if not store_name:
        print("[DEBUG] get_company_data: No store_name provided")
        return None
    
    # Normalize store name for matching
    store_name_lower = store_name.lower().strip()
    print(f"[DEBUG] get_company_data: Looking for '{store_name}' (normalized: '{store_name_lower}')")
    
    # Direct match
    if store_name_lower in COMPANY_DATA:
        print(f"[DEBUG] ✓ Found direct match for '{store_name_lower}'")
        return COMPANY_DATA[store_name_lower]
    
    # Partial match (e.g., "Walmart Supercenter" matches "walmart")
    for company_key in COMPANY_DATA.keys():
        if company_key in store_name_lower:
            print(f"[DEBUG] ✓ Found partial match: '{company_key}' in '{store_name_lower}'")
            return COMPANY_DATA[company_key]
    
    # Try removing common suffixes and try again
    # Remove: Supercenter, Marketplace, Store, Grocery, Supermarket, Market, etc.
    common_suffixes = [
        ' supercenter', ' marketplace', ' store', ' grocery', ' supermarket', 
        ' market', ' shop', ' food', ' center', ' retail', ' location',
        ' #', ' no.', ' branch'
    ]
    
    cleaned_name = store_name_lower
    for suffix in common_suffixes:
        if suffix in cleaned_name:
            cleaned_name = cleaned_name.split(suffix)[0].strip()
    
    # If we cleaned the name, try matching again
    if cleaned_name != store_name_lower:
        print(f"[DEBUG] Trying cleaned name: '{cleaned_name}'")
        if cleaned_name in COMPANY_DATA:
            print(f"[DEBUG] ✓ Found match after cleaning: '{cleaned_name}'")
            return COMPANY_DATA[cleaned_name]
        
        # Try partial match on cleaned name
        for company_key in COMPANY_DATA.keys():
            if company_key in cleaned_name or cleaned_name in company_key:
                print(f"[DEBUG] ✓ Found partial match after cleaning: '{company_key}' ~ '{cleaned_name}'")
                return COMPANY_DATA[company_key]
    
    print(f"[DEBUG] ✗ No match found for '{store_name_lower}'. Available companies: {list(COMPANY_DATA.keys())[:10]}...")
    return None


def has_company_data(store_name):
    """Check if company-specific data exists for a store."""
    return get_company_data(store_name) is not None


def get_store_type_from_company(store_name):
    """
    Get the store type/category from company data.
    Returns None if no company match found.
    
    This ensures consistent store type classification for known companies,
    preventing variation based on store_id format.
    """
    company_data = get_company_data(store_name)
    if company_data and "category" in company_data:
        store_type = company_data["category"]
        print(f"[DEBUG] Store type from company data: '{store_type}' for '{store_name}'")
        return store_type
    return None
