from app.analytics import calculate_labor_ratio

# MUST start with lowercase "test_"
def test_calculate_labor_ratio_normal():
    assert calculate_labor_ratio(2000, 10000) == 0.2

# MUST start with lowercase "test_"
def test_calculate_labor_ratio_zero_sales():
    assert calculate_labor_ratio(1500, 0) == 0.0