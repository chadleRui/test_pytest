import time

import yaml

from test_framework.page.main_page import MainPage


class TestFrame:
    def setup(self):
        self.main=MainPage()

    def test_framework(self):
        self.main.search_things()
        time.sleep(2)