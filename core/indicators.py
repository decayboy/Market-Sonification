import numpy as np

def calculate_rsi(prices, period=14):
    if len(prices) < period:
        return 50
    gains = [max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))]
    losses = [max(0, prices[i-1] - prices[i]) for i in range(1, len(prices))]
    avg_gain = np.mean(gains)
    avg_loss = np.mean(losses)
    return 100 - (100 / (1 + (avg_gain / (avg_loss + 1e-6))))

def scale_price_to_note(price, min_price, max_price, note_range):
    return int(np.clip(
        (price - min_price) / (max_price - min_price) * (note_range[1] - note_range[0]) + note_range[0],
        note_range[0], note_range[1]
    ))
