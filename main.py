import time
from core.config import *
from core.midi_engine import MidiEngine
from core.data_feed import KrakenStream, AlpacaStream

def main():
    midi = MidiEngine()
    feeds = []

    for symbol in SYMBOLS_CRYPTO:
        feeds.append(KrakenStream(midi, symbol, MIDI_NOTE_RANGE, TREND_WINDOW, RSI_PERIOD))

    for symbol in SYMBOLS_STOCKS:
        feeds.append(AlpacaStream(midi, symbol, MIDI_NOTE_RANGE, TREND_WINDOW, RSI_PERIOD,
                                  ALPACA_API_KEY, ALPACA_SECRET, ALPACA_BASE_URL))

    # Basic polling loop (placeholder → replace with async or websocket)
    while True:
        for feed in feeds:
            try:
                feed.poll_price()
                time.sleep(0.5)  # minimal delay between markets
            except Exception as e:
                print(f"Error polling {feed.symbol}: {e}")

if __name__ == "__main__":
    main()

