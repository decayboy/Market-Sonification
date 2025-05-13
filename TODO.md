# 🎯 Market Sonifier – Master Development Roadmap

This is the internal development checklist for Market Sonifier.
Use this file to track core milestones, enhancements, and experiments.

Maintainer: William Madison  
Version: 3.5 (Current)

---

## ✅ Version 1 — Proof of Concept (Completed)

- [x] Create historical market data → MIDI sonification system
- [x] Implement data scaling + pitch mapping
- [x] Export to MIDI files

---

## ✅ Version 2 — Composed Historical Market Music (Completed)

- [x] Add scale-constrained melodies
- [x] Add trend-based chord generation (major = uptrend, minor = downtrend)
- [x] Add humanization (velocity & timing offsets)

---

## ✅ Version 3 — Live Market Music Instrument (Completed)

- [x] Integrate Kraken (crypto) live price feed
- [x] Integrate Alpaca (stocks) live price feed
- [x] Add real-time rolling buffer + trend detection
- [x] Send real-time live MIDI output
- [x] Add percussion trigger on volume spikes
- [x] Add RSI → tempo control
- [x] Add swing timing
- [x] Modular, class-based architecture (`core/` package)

---

## 🔨 Version 4 — Professional Market Performance System (Planned)

### 🎵 Core System Upgrades
- [ ] Migrate polling to async event loop (true concurrency)
- [ ] Add Binance + Coinbase Pro feeds
- [ ] Add IBKR stock feeds
- [ ] Create market “personality” profiles (asset → unique sound rules)
- [ ] Build plugin architecture for easy community add-ons

### 🎹 Music & MIDI Engine
- [ ] Add multiple instrument routing
- [ ] Build a MIDI effects module (e.g. auto arpeggios, echoes)
- [ ] Add tempo shifting based on global market volatility

### 🖥️ Visuals
- [ ] Start TouchDesigner visualizer module
- [ ] Add audio-reactive market particle engine
- [ ] Sync visuals with MIDI events via OSC

### 🎛️ Performance Mode
- [ ] Create internal “performance mode” UI (start/stop feeds, map assets to channels)
- [ ] Add support for physical MIDI controllers (Launchpad, APC40)
- [ ] Record and export full performances

---

## 🎯 Stretch Goals

- [ ] Package as standalone app (PyInstaller or Docker)
- [ ] Create web interface for configuring sonification engine
- [ ] Develop "alert mode" for extreme market events
- [ ] Explore possible mobile companion app

---

## 📝 Notes

This checklist reflects the evolving scope of Market Sonifier from an experimental art/research project to a fully functional market performance platform.

Only William Madison holds authority to approve feature merges or changes.

