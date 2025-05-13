import alpaca_trade_api as tradeapi
import krakenex
from indicators import calculate_rsi, scale_price_to_note
import numpy as np
from collections import deque

class KrakenStream:
    def __init__(self, midi_engine, symbol, note_range, trend_window, rsi_period):
        self.k = krakenex.API()
        self.symbol = symbol
        self.midi = midi_engine
        self.buffer = deque(maxlen=trend_window)
        self.prices = deque(maxlen=rsi_period)
        self.note_range = note_range

    def poll_price(self):
        # Kraken free API polling (real WebSocket requires extra setup)
        response = self.k.query_public('Ticker', {'pair': self.symbol.replace('/', '')})
        result = list(response['result'].values())[0]
        price = float(result['c'][0])
        self.process_price(price)

    def process_price(self, price):
        self.buffer.append(price)
        self.prices.append(price)

        min_p, max_p = min(self.buffer), max(self.buffer)
        note = scale_price_to_note(price, min_p, max_p, self.note_range)
        rsi = calculate_rsi(self.prices)

        trend = price - np.mean(self.buffer)
        if trend > 0:
            self.midi.play_note(note + 4)
        else:
            self.midi.play_note(note - 3)

        if rsi > 70:  # very strong movement
            self.midi.percussion_hit()

class AlpacaStream:
    def __init__(self, midi_engine, symbol, note_range, trend_window, rsi_period, key, secret, url):
        self.api = tradeapi.REST(key, secret, url)
        self.symbol = symbol
        self.midi = midi_engine
        self.buffer = deque(maxlen=trend_window)
        self.prices = deque(maxlen=rsi_period)
        self.note_range = note_range

    def poll_price(self):
        barset = self.api.get_barset(self.symbol, '1Min', limit=1)
        price = barset[self.symbol][0].c
        self.process_price(price)

    def process_price(self, price):
        self.buffer.append(price)
        self.prices.append(price)

        min_p, max_p = min(self.buffer), max(self.buffer)
        note = scale_price_to_note(price, min_p, max_p, self.note_range)
        rsi = calculate_rsi(self.prices)

        trend = price - np.mean(self.buffer)
        if trend > 0:
            self.midi.play_note(note + 4)
        else:
            self.midi.play_note(note - 3)

        if rsi > 70:
            self.midi.percussion_hit()
