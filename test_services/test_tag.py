import pytest

from test_services.tag import Tag

class TestTag:

    # 实例化tag，生成token
    def setup_class(self):
        self.tag=Tag()
        self.tag.generate_token()
        self.group_ids=self.tag.get_page_group_ids()
        self.tag_ids=self.tag.get_page_tag_ids()
        #每次运行该类都把所有的group_id 给delete掉
        self.tag.delete_tag(self.group_ids)

    # 测试获取tag成功的用例
    @pytest.mark.parametrize("tag_id",[
        [],
        ["etId3CEAAAzbg90d5Qh-sY4se7fXxMPg"],
        ["etId3CEAAA0OXxACuf1JL-hoQMCWjPJQ","etId3CEAAAvjX9OU6v6Tu32tk62XNs0A"]
    ])
    def test_get_tag_list(self,tag_id):
        # 调用方法，发起请求获取tag list，并将响应结果格式化为json保存
        # 方法内部做判断，判断传入的tag_id是否为空，为空则返回全部，否则返回指定tag_id的内容
        list=self.tag.get_tag_list(tag_id).json()
        print(list)
        # 判断返回业务码
        assert list['errcode']==0

    # 测试获取tag失败的用例
    def test_get_tag_list_fail(self):
        # 传入一个不存在的tag_id
        list=self.tag.get_tag_list(tag_id=["lalala"]).json()
        print(list)
        assert list['errcode'] !=0

    @pytest.mark.parametrize("group_name,tags",[
        ["test_group_1",[{"name":"test_tag_1"}]],
        ["test_group_2",[{"name":"test_tag_2_1"},{"name":"test_tag_2_2"}]]
    ])
    def test_add_tag(self,group_name,tags):
        list=self.tag.add_tag(group_name,tags)
        assert list.status_code==200
        all_tags_r=self.tag.get_tag_list()
        all_tags_json=all_tags_r.json()
        # 将返回json内容中的group_name读取出来
        group=[group for group in all_tags_json["tag_group"] if group["group_name"] == group_name][0]
        # 将返回json内容中的tag_name读取出来
        tags_tmp=[{"name":tag["name"]} for tag in group["tag"]]
        print(group)
        print(tags_tmp)
        # 判断添加的值是否与返回报文中一致
        assert group["group_name"]==group_name
        assert tags_tmp==tags

    @pytest.mark.parametrize("group_id,tag_id", [
        [[],[]],
        [["etId3CEAAAzt-p4Z44pjgMcN8RrKs5_A"],[]],
        [[],["etId3CEAAAdY3F37xdn8M5zhY4cRu3iA"]]
    ])
    def test_delete_tag(self,group_id,tag_id):
        # 删除指定id的内容
        r=self.tag.delete_tag(group_id,tag_id)
        print(r)
        # 获取页面的tag信息
        list=self.tag.get_tag_list().json()
        # 如果获取的tag为空，则说明删除成功
        if list =={}:
            assert True
        id_group = self.tag.get_page_group_ids()
        print(id_group)
        # 如果传入的id不在页面中了，说明删除成功
        if group_id not in id_group:
            assert True
        id_tags = self.tag.get_page_tag_ids()
        print(id_tags)
        if tag_id not in id_tags:
            assert True



    def test_edit_tag(self):
        pass
