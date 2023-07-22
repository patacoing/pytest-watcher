from watchfiles import watch
from typing import Callable
from threading import Thread
from .logging import logger
import os

class Watcher:
    def __init__(self, *paths, target: Callable, args: str):
        self.paths = paths
        self.target = target
        self.args = args
        self.thread = Thread(target=self.target, args=(self.args,))
        self.thread.start()

    def run(self):
        for _ in watch(*self.paths, raise_interrupt=False):
            logger.info(f"Changes detected, reloading pytest...")
            self.thread._stop()
            self.thread = Thread(target=self.target, args=(self.args,))
            self.thread.start()


def run_pytest(args: str):
    logger.info(f"Running pytest with arguments: {args}")
    os.system(f"pytest {args}")