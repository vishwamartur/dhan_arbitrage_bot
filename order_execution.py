from dhan_api_client import DhanAPIClient

class OrderExecution:
    def __init__(self):
        self.dhan_client = DhanAPIClient()

    def place_simultaneous_orders(self, orders):
        # orders is expected to be a list of dictionaries, each containing order parameters
        # Example: [{
        #    "security_id": "12345",
        #    "exchange_segment": "NSE_EQ",
        #    "transaction_type": "BUY",
        #    "quantity": 1,
        #    "order_type": "MARKET",
        #    "product_type": "INTRADAY"
        # }, ...]
        
        responses = []
        for order in orders:
            print(f"Attempting to place order: {order}")
            response = self.dhan_client.place_order(
                security_id=order["security_id"],
                exchange_segment=order["exchange_segment"],
                transaction_type=order["transaction_type"],
                quantity=order["quantity"],
                order_type=order["order_type"],
                product_type=order["product_type"],
                price=order.get("price")
            )
            responses.append(response)
            if response and response.get("status") == "success":
                print(f"Order placed successfully: {response}")
            else:
                print(f"Failed to place order: {response}")
        return responses


