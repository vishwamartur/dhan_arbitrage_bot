# Dhan Options Arbitrage Bot

This project implements a Python-based options arbitrage trading system using the Dhan API. It is designed to identify mispricings using machine learning models and execute arbitrage strategies, including index arbitrage and volatility arbitrage, with simultaneous order placement.

## Project Structure

- `dhan_api_client.py`: Handles communication with the Dhan API for market data, historical data, option chains, and order placement.
- `data_preprocessing.py`: Contains functions for preprocessing historical and option chain data for use in machine learning models.
- `mispricing_model.py`: Implements a machine learning model (RandomForestRegressor) to identify mispricings in options prices.
- `index_arbitrage.py`: Contains logic for calculating synthetic index prices and identifying index arbitrage opportunities.
- `volatility_arbitrage.py`: Provides functions for calculating implied volatility, identifying volatility spread opportunities, and managing delta-neutral positions.
- `order_execution.py`: Manages the placement of simultaneous orders through the Dhan API.
- `risk_management.py`: Implements basic risk management features, including exposure checks and trade logging.
- `telegram_bot.py`: Handles sending notifications and updates to a Telegram bot.
- `mistral_ai_client.py`: Provides an interface to the Mistral AI API for advanced ML operations.
- `main.py`: The main application file that orchestrates the data collection, mispricing identification, arbitrage strategy execution, and order placement.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Setup and Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <repository_url>
    cd dhan_arbitrage_bot
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Dhan API Credentials:**
    You need to obtain your `ACCESS_TOKEN` and `CLIENT_ID` from Dhan. Set these as environment variables:
    ```bash
    export DHAN_ACCESS_TOKEN="your_access_token"
    export DHAN_CLIENT_ID="your_client_id"
    ```

4.  **Set up Telegram Bot Credentials:**
    To receive live updates, you need to create a Telegram bot and obtain its `TELEGRAM_BOT_TOKEN` and your `TELEGRAM_CHAT_ID`. Set these as environment variables:
    ```bash
    export TELEGRAM_BOT_TOKEN="your_bot_token"
    export TELEGRAM_CHAT_ID="your_chat_id"
    ```

5.  **Set up Mistral AI API Credentials:**
    To enable advanced ML operations, you need to obtain your `MISTRAL_API_KEY` from Mistral AI. Set this as an environment variable:
    ```bash
    export MISTRAL_API_KEY="your_mistral_api_key"
    ```
    **Note:** For security, it is highly recommended to use environment variables or a secure configuration management system for API keys, rather than hardcoding them directly in the code.

## Usage

To run the arbitrage bot, execute the `main.py` file:

```bash
python main.py
```

The `main.py` script includes a `run_arbitrage_cycle()` function that performs a single cycle of data fetching, arbitrage opportunity identification, and (simulated) order placement. You can uncomment the `bot.start(interval_seconds=30)` line in `main.py` to run the bot in a continuous loop at a specified interval.

## Key Features

-   **Machine Learning for Mispricing:** Utilizes `scikit-learn` and Mistral AI to build models for identifying discrepancies in options pricing and providing advanced analysis.
-   **Index Arbitrage:** Compares NSE spot index with synthetic index prices derived from options to find arbitrage opportunities.
-   **Volatility Arbitrage:** Identifies opportunities based on differences in implied and realized volatility, and supports delta-neutral strategies.
-   **Simultaneous Order Placement:** Designed to execute multiple legs of an arbitrage trade concurrently to minimize slippage.
-   **Basic Risk Management:** Includes checks for maximum exposure and loss per trade.
-   **Live Telegram Updates:** Sends real-time notifications on arbitrage opportunities, trade executions, and other important events directly to your Telegram chat.
-   **Mistral AI Integration:** Leverages Mistral AI for enhanced mispricing analysis and potentially other ML-driven insights.

## Disclaimer

This code is provided for educational and informational purposes only. Trading in financial markets carries significant risk, and you could lose money. Always conduct your own due diligence and consult with a financial professional before making any investment decisions. The author and contributors are not responsible for any financial losses incurred from using this software.

## Future Enhancements

-   Integration with real-time market data feeds.
-   More sophisticated machine learning models and feature engineering.
-   Advanced risk management features (e.g., dynamic position sizing, circuit breakers).
-   Backtesting and simulation framework.
-   Logging and reporting improvements.
-   Support for more complex options strategies.


