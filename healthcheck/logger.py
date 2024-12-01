import json
from datetime import datetime

#Logs results into a file.
def log_results(results, log_file="healthcheck.log"):
    with open(log_file, "a") as f:
        timestamp = datetime.now().isoformat()
        for result in results:
            result["timestamp"] = timestamp
            f.write(json.dumps(result) + "\n")
