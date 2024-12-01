import click
import time
from healthcheck.checker import check_url
from healthcheck.logger import log_results
from healthcheck.config import load_config

#The main entry point for the CLI.
@click.command()
@click.option("--config", default="config.json", help="Path to configuration file.")
def run(config):
    settings = load_config(config)
    urls = settings.get("urls", [])
    interval = settings.get("check_interval", 60)

    if not urls:
        print("No URLs found in the configuration.")
        return

    while True:
        results = []
        for url in urls:
            result = check_url(url)
            print(result)
            results.append(result)
        log_results(results)
        time.sleep(interval)


if __name__ == "__main__":
    run()
