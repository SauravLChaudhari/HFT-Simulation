# strategies.py
import random

class MarketMaker:
    def __init__(self, order_book):
        self.order_book = order_book

    def place_orders(self):
        top_buy = self.order_book.get_top_buy()
        top_sell = self.order_book.get_top_sell()

        if top_buy and top_sell:
            spread = top_sell.price - top_buy.price
            mid_price = (top_buy.price + top_sell.price) / 2

            buy_price = mid_price - spread / 2
            sell_price = mid_price + spread / 2

            # Place buy and sell orders
            self.order_book.add_order(price=buy_price, quantity=random.randint(1, 10), side='buy')
            self.order_book.add_order(price=sell_price, quantity=random.randint(1, 10), side='sell')

# Example usage
market_maker = MarketMaker(order_book)
market_maker.place_orders()
order_book.print_order_book()
