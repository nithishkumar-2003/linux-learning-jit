import pathlib, json, datetime

BASE = pathlib.Path(__file__).parent

def save_config(cfg):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = BASE / f"config_{ts}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
    # update current config file
    with open(BASE / "config.json", "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
    return str(fname)
