# NaturePulse 🌲

**Your Screen-Free, Offline Eco-Trail & Bio-Sound Companion**

*Built for the Hacktoberfest Open-Source AI Challenge: Week 1 — "Touch Grass"*

---

## What It Does

NaturePulse is a **100% offline** nature companion that uses **open-weight AI acoustic pattern matching** to help hikers, birders, and outdoor explorers identify local wildlife species without needing an internet connection on the trail.

The goal is simple: **minimize screen time and maximize time outside.** You open the app before you leave, and it runs entirely on your local machine — no API calls, no telemetry, no signal required.

## Why Open-Source AI Was Essential

- **Zero Signal on Trails**: Cloud AI APIs are useless without connectivity. Open-weight models run locally.
- **Data Privacy**: Nature journals, GPS data, and wildlife observations stay on your device.
- **No Subscription Cost**: Free to run indefinitely on any laptop or Raspberry Pi.
- **Model Swappability**: Easily swap in a fine-tuned bird-call model (like BirdNET) without vendor lock-in.

## Quickstart

```bash
pip install flask
python app.py
```

Open browser at `http://localhost:5001`

## License

MIT License — See [LICENSE](./LICENSE)
