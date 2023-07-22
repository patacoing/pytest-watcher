from app.argument_parser import ArgumentParser
from app.logging import logger
from app.watcher import Watcher, run_pytest


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    logger.info(f"Starting pytest watcher... {argument_parser.path_arg}")

    watcher = Watcher(argument_parser.path_arg, target=run_pytest, args=argument_parser.pytest_args)
    watcher.run()

    logger.info("Pytest watcher stopped.")
    exit(0)
