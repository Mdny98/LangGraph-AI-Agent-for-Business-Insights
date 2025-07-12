import pytest
from agent import app # Import the compiled LangGraph app

def test_agent_logic():
    """
    Tests the agent's output for a sample input where CAC has increased significantly.
    """
    # Sample input data for the test
    test_input = {
        "input_data": {
            "today": {"revenue": 1200, "cost": 950, "customers": 60},
            "yesterday": {"revenue": 1000, "cost": 700, "customers": 50},
        }
    }

    # Run the agent with the test data
    result = app.invoke(test_input)

    # 1. Validate the output keys
    expected_keys = ["input_data", "profit", "profit_status", "cac", "revenue_change", "cost_change", "alerts", "recommendations"]
    for key in expected_keys:
        assert key in result

    # 2. Validate the calculation accuracy
    assert result['profit'] == 250  # 1200 - 950
    assert result['profit_status'] == "Profitable"
    assert round(result['cac'], 2) == 15.83 # 950 / 60
    assert round(result['revenue_change'], 2) == 20.00 # ((1200-1000)/1000)*100

    # 3. Validate the recommendations and alerts
    yesterday_cac = 700 / 50
    cac_increase_percent = ((result['cac'] - yesterday_cac) / yesterday_cac) * 100
    print(cac_increase_percent)
    print('tested1')
    
    expected_recommendations = [
        "Sales are growing strongly! Consider increasing the advertising budget to accelerate growth."
    ]
    for rec in expected_recommendations:
        assert rec in result['recommendations']

def test_agent_profit_loss():
    """
    Tests the agent's response when there is a profit loss.
    """
    # Sample input data for the test
    test_input_loss = {
        "input_data": {
            "today": {"revenue": 800, "cost": 900, "customers": 40},
            "yesterday": {"revenue": 850, "cost": 800, "customers": 45},
        }
    }
    # Run the agent
    result = app.invoke(test_input_loss)

    # Validate results
    assert result['profit'] == -100
    assert result['profit_status'] == "Loss"
    assert "Business is not profitable. Review pricing and reduce costs." in result['recommendations']