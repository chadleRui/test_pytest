import time

import pytest

from test_PO.page.home_page import HomePage


class TestAddContact:
    #setup方法，存个变量方便下面使用
    def setup(self):
        self.home=HomePage()

    def test_add_contact(self):
        addmember=self.home.add_member()
        addmember.add_member_detail("aaaa","1","13111111111")
        result=addmember.check_add("aaaaa91")
        assert result


