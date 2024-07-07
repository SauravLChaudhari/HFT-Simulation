# performance.py
import matplotlib.pyplot as plt

class PerformanceMetrics:
    def __init__(self):
        self.trades = []
        self.profits = []

    def record_trade(self, trade_price, trade_quantity, trade_side):
        trade_value = trade_price * trade_quantity
        if trade_side == 'buy':
            self.trades.append(-trade_value)
        else:
            self.trades.append(trade_value)
        self.profits.append(sum(self.trades))

    def plot_performance(self):
        plt.plot(self.profits)
        plt.xlabel('Trade Number')
        plt.ylabel('Cumulative Profit')
        plt.title('Trading Performance')
        plt.show()

# Example usage
metrics = PerformanceMetrics()
metrics.record_trade(trade_price=100, trade_quantity=10, trade_side='buy')
metrics.record_trade(trade_price=102, trade_quantity=10, trade_side='sell')
metrics.plot_performance()
