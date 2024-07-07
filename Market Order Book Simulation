# order_book.py
import heapq
import random

class Order:
    def __init__(self, order_id, price, quantity, side):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.side = side  # 'buy' or 'sell'

    def __lt__(self, other):
        if self.side == 'buy':
            return self.price > other.price  # Max-heap for buy orders
        return self.price < other.price  # Min-heap for sell orders

class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.order_id = 0

    def add_order(self, price, quantity, side):
        self.order_id += 1
        order = Order(self.order_id, price, quantity, side)
        if side == 'buy':
            heapq.heappush(self.buy_orders, order)
        else:
            heapq.heappush(self.sell_orders, order)

    def get_top_buy(self):
        return self.buy_orders[0] if self.buy_orders else None

    def get_top_sell(self):
        return self.sell_orders[0] if self.sell_orders else None

    def remove_order(self, order_id, side):
        # For simplicity, we're not implementing this in detail
        pass

    def print_order_book(self):
        print("Buy Orders:")
        for order in self.buy_orders:
            print(f"ID: {order.order_id}, Price: {order.price}, Quantity: {order.quantity}")

        print("Sell Orders:")
        for order in self.sell_orders:
            print(f"ID: {order.order_id}, Price: {order.price}, Quantity: {order.quantity}")

# Example usage
order_book = OrderBook()
order_book.add_order(price=100, quantity=10, side='buy')
order_book.add_order(price=101, quantity=5, side='buy')
order_book.add_order(price=99, quantity=8, side='sell')
order_book.add_order(price=98, quantity=15, side='sell')
order_book.print_order_book()
