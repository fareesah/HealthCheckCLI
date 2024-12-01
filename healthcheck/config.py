import json

#Manages the configuration file.
def load_config(config_file="config.json"):
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"urls": [], "check_interval": 60, "alert_threshold": 3}
