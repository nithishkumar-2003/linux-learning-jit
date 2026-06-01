GMSL Microservices-like Local Setup
----------------------------------
This package runs two lightweight Flask services locally and a Tkinter UI that interacts with them via HTTP.
The goal is to mimic microservices communicating over APIs while keeping everything runnable on a single machine
(modular monolithic for local development).

Structure:
- devices_service/     (Flask service on port 5001)
- registers_service/   (Flask service on port 5002)
- ui_client/           (Tkinter UI that calls the services)
- run_all.py           (starts both services in separate processes then launches the UI)
- requirements.txt     (Flask, requests)

Run:
1. Create a virtualenv and activate it:
   python -m venv venv
   source venv/bin/activate   (Linux/macOS)
   venv\Scripts\activate    (Windows)

2. Install:
   pip install -r requirements.txt

3. From this folder, run:
   python run_all.py

Notes:
- The services are simple and meant for local development/demo only (no auth).
- If ports 5001 or 5002 are busy, edit run_all.py and the service apps to use different ports.
