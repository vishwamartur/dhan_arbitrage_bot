import os
from dhanhq import dhanhq

# Replace with your actual API details
ACCESS_TOKEN = os.environ.get("DHAN_ACCESS_TOKEN")
CLIENT_ID = os.environ.get("DHAN_CLIENT_ID")

class DhanAPIClient:
    def __init__(self):
        if not ACCESS_TOKEN or not CLIENT_ID:
            raise ValueError("DHAN_ACCESS_TOKEN and DHAN_CLIENT_ID environment variables must be set.")
        self.dhan = dhanhq(CLIENT_ID, ACCESS_TOKEN)

    def get_market_status(self):
        try:
            market_status = self.dhan.get_market_status()
            return market_status
        except Exception as e:
            print(f"Error getting market status: {e}")
            return None

    # Add more API methods as needed

if __name__ == "__main__":
    # Example usage (for testing purposes)
    # Set environment variables before running this script
    # export DHAN_ACCESS_TOKEN="your_access_token"
    # export DHAN_CLIENT_ID="your_client_id"

    client = DhanAPIClient()
    status = client.get_market_status()
    if status:
        print("Market Status:", status)




    def get_historical_data(self, instrument_id, exchange_segment, security_id, start_date, end_date):
        try:
            historical_data = self.dhan.get_historical_data(instrument_id, exchange_segment, security_id, start_date, end_date)
            return historical_data
        except Exception as e:
            print(f"Error getting historical data: {e}")
            return None

    def get_option_chain(self, security_id):
        try:
            option_chain = self.dhan.get_option_chain(security_id)
            return option_chain
        except Exception as e:
            print(f"Error getting option chain: {e}")
            return None




    def place_order(self, security_id, exchange_segment, transaction_type, quantity, order_type, product_type, price=None):
        try:
            order_response = self.dhan.place_order(
                security_id=security_id,
                exchange_segment=exchange_segment,
                transaction_type=transaction_type, # "BUY" or "SELL"
                quantity=quantity,
                order_type=order_type, # "MARKET", "LIMIT", "STOPLOSS_MARKET", "STOPLOSS_LIMIT"
                product_type=product_type, # "CNC", "INTRADAY", "MARGIN", "NORMAL"
                price=price
            )
            return order_response
        except Exception as e:
            print(f"Error placing order: {e}")
            return None

    def get_order_book(self):
        try:
            order_book = self.dhan.get_order_book()
            return order_book
        except Exception as e:
            print(f"Error getting order book: {e}")
            return None




    def get_positions(self):
        try:
            positions = self.dhan.get_positions()
            return positions
        except Exception as e:
            print(f"Error getting positions: {e}")
            return None


