import requests
import time

#Handles the URL checks.
def check_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        latency = time.time() - start_time
        return {
            "url": url,
            "status_code": response.status_code,
            "latency": round(latency, 3),
        }
    except requests.exceptions.RequestException as e:
        return {"url": url, "error": str(e)}
