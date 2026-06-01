import json, pathlib
DATA_FILE = pathlib.Path(__file__).parent / "bitfields.json"
def load_bitfields():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
