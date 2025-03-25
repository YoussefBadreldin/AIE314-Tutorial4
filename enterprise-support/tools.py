from langchain.tools import StructuredTool

def create_support_ticket(issue: str, customer_id: str, priority: str) -> str:
    return f"Ticket created for {customer_id} (Priority: {priority})"

def check_order_status(order_id: str) -> str:
    return f"Order {order_id} status: Shipped"

support_tools = [
    StructuredTool.from_function(create_support_ticket),
    StructuredTool.from_function(check_order_status),
]