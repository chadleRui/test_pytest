import yaml

from test_framework.page.base_page import BasePage
# from test_framework.page.search_things import SearchThings


class MainPage(BasePage):
    def search_things(self):
        # self.base_url=path
        with open("test_search_value.yaml",encoding="utf-8") as f:
            search_value=yaml.safe_load(f)
            # print(f"search_value['data']====={str(search_value['data'])}")
            self.search_params.append(str(search_value['data']))
            self.steps("../page/main_page.yaml")
            return True