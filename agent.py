import os
from typing import TypedDict, Annotated, List
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from IPython.display import Image, display
from langgraph.graph import StateGraph, END, START

# from langgraph_studio import start_trace_server

load_dotenv()

# Define the state for the graph
class AgentState(TypedDict):
   
    input_data: dict
    profit: float
    profit_status: str
    cac: float
    revenue_change: float
    cost_change: float
    alerts: List[str]
    recommendations: List[str]

# Input Node: Receives the initial data
def input_node(state: AgentState):
    """Receives and validates the initial business data."""
    print("---INPUT---")
    # Can validate the input data here
    return state

# Processing Node: Calculates key business metrics
def processing_node(state: AgentState):
    """Calculates profit, CAC, and percentage changes."""
    print("---PROCESSING---")
    data = state['input_data']
    today = data['today']
    yesterday = data['yesterday']

    # Calculate Profit
    profit = today['revenue'] - today['cost']
    profit_status = "Profitable" if profit > 0 else "Loss"

    # Calculate CAC (Customer Acquisition Cost)
    cac = today['cost'] / today['customers']

    # Calculate Percentage Changes
    revenue_change = ((today['revenue'] - yesterday['revenue']) / yesterday['revenue']) * 100
    cost_change = ((today['cost'] - yesterday['cost']) / yesterday['cost']) * 100

    return {
        "profit": profit,
        "profit_status": profit_status,
        "cac": cac,
        "revenue_change": revenue_change,
        "cost_change": cost_change,
    }

# Recommendation Node: Generates actionable advice
def recommendation_node(state: AgentState):
    """Generates recommendations based on the processed data."""
    
    print("---RECOMMENDING---")
    alerts = []
    recommendations = []

    # Check for negative profit
    if state['profit'] < 0:
        recommendations.append("Business is not profitable. Review pricing and reduce costs.")

    # Check for significant CAC increase (more than 20%)
    yesterday_cac = state['input_data']['yesterday']['cost'] / state['input_data']['yesterday']['customers']
    cac_increase_percent = ((state['cac'] - yesterday_cac) / yesterday_cac) * 100
    if cac_increase_percent > 20:
        alert = f"Warning: CAC increased by {cac_increase_percent:.2f}%. Review marketing campaigns."
        alerts.append(alert)
        recommendations.append("Analyze marketing channel performance to optimize CAC.")

    # Suggest actions based on sales growth
    # If revenue grew by more than 10%
    if state['revenue_change'] > 10:
        recommendations.append("Sales are growing strongly! Consider increasing the advertising budget to accelerate growth.")
    elif state['revenue_change'] < 0:
        recommendations.append("Sales are declining. Investigate market trends and competitor actions.")

    return {"alerts": alerts, "recommendations": recommendations}

# Build the graph
workflow = StateGraph(AgentState)
workflow.add_node("input", input_node)
workflow.add_node("processing", processing_node)
workflow.add_node("recommendation", recommendation_node)

# edges
workflow.add_edge(START, "input")
workflow.add_edge("input", "processing")
workflow.add_edge("processing", "recommendation")
workflow.add_edge("recommendation", END)

# Compile the graph
app = workflow.compile()

# Sample Data
sample_input = {
    "input_data": {
        "today": {"revenue": 1200, "cost": 950, "customers": 60},
        "yesterday": {"revenue": 1000, "cost": 700, "customers": 50},
    }
}

if __name__ == "__main__":
    # Run the agent
    final_state = app.invoke(sample_input)

    # Print the final output
    print("\n---FINAL REPORT---")
    print(f"Profit/Loss Status: {final_state['profit_status']} (${final_state['profit']:.2f})")
    print("Alerts:")
    for alert in final_state['alerts']:
        print(f"- {alert}")
    print("Recommendations:")
    for rec in final_state['recommendations']:
        print(f"- {rec}")


# for Graph bulding

# try:
#     png_data = app.get_graph().draw_mermaid_png()
    
#     # Save to file
#     with open("output_graph.png", "wb") as f:
#         f.write(png_data)
    
#     # Optionally display in notebook
#     display(Image(png_data))
# except Exception as e:
#     print(f"Error generating image: {e}")
