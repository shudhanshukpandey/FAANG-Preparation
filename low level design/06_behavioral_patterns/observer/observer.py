"""Observer Pattern: Pub-Sub event dispatching for real-time market updates."""

from abc import ABC, abstractmethod
from typing import Dict, List


# 1. Observer Interface
class StockObserver(ABC):
    @abstractmethod
    def on_price_change(self, symbol: str, old_price: float, new_price: float) -> None:
        pass


# 2. Concrete Observer 1: Mobile Push Alert
class MobileAlertSubscriber(StockObserver):
    def __init__(self, username: str) -> None:
        self.username = username

    def on_price_change(self, symbol: str, old_price: float, new_price: float) -> None:
        print(f"[Mobile Push -> {self.username}]: {symbol} shifted from ${old_price:.2f} to ${new_price:.2f}")


# 3. Concrete Observer 2: Automated Trading Algorithm
class TradingBotSubscriber(StockObserver):
    def __init__(self, bot_id: str, buy_threshold: float) -> None:
        self.bot_id = bot_id
        self.buy_threshold = buy_threshold

    def on_price_change(self, symbol: str, old_price: float, new_price: float) -> None:
        if new_price < self.buy_threshold:
            print(f"[Bot #{self.bot_id} EXECUTE BUY]: {symbol} dip detected at ${new_price:.2f} (< ${self.buy_threshold:.2f})!")


# 4. Subject / Publisher
class StockMarketTicker:
    def __init__(self) -> None:
        self._prices: Dict[str, float] = {}
        self._subscribers: Dict[str, List[StockObserver]] = {}

    def subscribe(self, symbol: str, observer: StockObserver) -> None:
        if symbol not in self._subscribers:
            self._subscribers[symbol] = []
        self._subscribers[symbol].append(observer)

    def unsubscribe(self, symbol: str, observer: StockObserver) -> None:
        if symbol in self._subscribers and observer in self._subscribers[symbol]:
            self._subscribers[symbol].remove(observer)

    def set_price(self, symbol: str, price: float) -> None:
        old_price = self._prices.get(symbol, price)
        self._prices[symbol] = price
        self._notify(symbol, old_price, price)

    def _notify(self, symbol: str, old_price: float, new_price: float) -> None:
        for observer in self._subscribers.get(symbol, []):
            observer.on_price_change(symbol, old_price, new_price)


if __name__ == "__main__":
    ticker = StockMarketTicker()

    alice_phone = MobileAlertSubscriber("Alice")
    alpha_bot = TradingBotSubscriber("BOT_ALPHA", buy_threshold=145.0)

    # Register subscribers for AAPL
    ticker.subscribe("AAPL", alice_phone)
    ticker.subscribe("AAPL", alpha_bot)

    # Initial prices
    ticker.set_price("AAPL", 150.0)

    # Price drops -> triggers notifications and bot logic
    print("\n--- Price Drop Event ---")
    ticker.set_price("AAPL", 142.50)

    # Unsubscribe Alice
    ticker.unsubscribe("AAPL", alice_phone)
    print("\n--- Price Rises after Alice Unsubscribed ---")
    ticker.set_price("AAPL", 155.0)
