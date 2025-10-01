🚀 Welcome to plc_reader!

plc_reader is your go-to Python project for reading real PLC (Programmable
Logic Controller) devices, processing their signals, and exporting the
results into clean CSV files. This is a powerful tool for engineers,
developers, and data enthusiasts who want to bridge physical PLC hardware
with modern data workflows.

With plc_reader, you get:
✅ Real-time PLC data acquisition
✅ Flexible signal analysis
✅ Clean CSV exports for further analysis
✅ A modular design that makes extension a breeze

---
Installation:

1. Clone this repository:
   git clone https://github.com/charleswhitesun/plc_reader.git

2. Navigate into the project directory:
   cd plc_reader

3. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate      # Linux / MacOS
   venv\Scripts\activate         # Windows

4. Install dependencies:
   pip install -r requirements.txt

---
Usage:

Ready to start reading your PLC devices?

1. Configure your PLC connection in `src/app/config.py`.

2. Run the main program:
   python plc_reader/main.py

3. Watch as your PLC data gets transformed and written into CSV files.

---
Features:

- **PLC Data Reader** — Connects directly to your PLC device for real-time
  signal reading.
- **Signal Analyzer** — Processes raw data into meaningful values.
- **CSV Result Handler** — Automatically stores results in organized CSV files.
- **Extensible Architecture** — Easily add new strategies or handlers.

---
API:

This project is primarily run as a standalone tool. The main.py entry point
coordinates device reading and result exporting. You can extend it to
integrate with APIs or other processing pipelines.

---
License:

This project is licensed under the Apache License 2.0.
