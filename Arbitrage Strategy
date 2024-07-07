# strategies.py
class Arbitrageur:
    def __init__(self, order_book1, order_book2):
        self.order_book1 = order_book1
        self.order_book2 = order_book2

    def find_arbitrage_opportunity(self):
        top_buy1 = self.order_book1.get_top_buy()
        top_sell1 = self.order_book1.get_top_sell()
        top_buy2 = self.order_book2.get_top_buy()
        top_sell2 = self.order_book2.get_top_sell()

        if top_buy1 and top_sell2 and top_buy1.price > top_sell2.price:
            # Buy from book2 and sell on book1
            print(f"Arbitrage opportunity: Buy at {top_sell2.price} and sell at {top_buy1.price}")
        if top_buy2 and top_sell1 and top_buy2.price > top_sell1.price:
            # Buy from book1 and sell on book2
            print(f"Arbitrage opportunity: Buy at {top_sell1.price} and sell at {top_buy2.price}")

# Example usage
order_book2 = OrderBook()
order_book2.add_order(price=97, quantity=10, side='buy')
order_book2.add_order(price=102, quantity=5, side='sell')

arbitrageur = Arbitrageur(order_book, order_book2)
arbitrageur.find_arbitrage_opportunity()
