import requests

corpid = "ww2393fdc0f430a71e"
corpsecret = "eucizd0ntrbfNTdtwDvsNWIMlUY7ySaYWi8MVNjMd3c"
class Tag:

    def __init__(self):
        self.token=""

    # 生成token
    def generate_token(self):
        r=requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={"corpid":corpid,"corpsecret":corpsecret}
        )
        self.token=r.json()['access_token']

    # 获取tag
    def get_tag_list(self,tag_id=[]):
        # 如果传入了tag_id，则根据id返回tag信息
        if len(tag_id) !=0:
            tag=requests.post(
                "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                params={"access_token":self.token},
                json={
                    "tag_id":tag_id
                }
            )
            return tag
        #其他情况就返回页面的tag
        all_tag = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token}
        )
        return all_tag

    # 添加tag
    def add_tag(self,group_name,tags):
        r=requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token":self.token},
            json={
                "group_name":group_name,
                "tag":tags
            }
        )
        return r


    # 删除tag
    def delete_tag(self,group_id=[],tag_id=[]):
        if group_id==[] and tag_id==[]:
            return "传入group_id和tag_id为空，未删除成功"
        r=requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "tag_id":tag_id,
                "group_id":group_id
            }
        )
        return r

    def get_page_group_ids(self):
        # 先获取到所有的tag信息，且将group_id保存起来
        all = self.get_tag_list().json()
        # 将页面所有group_id返回
        return [group_id["group_id"] for group_id in all["tag_group"]]

    def get_page_tag_ids(self):
        # 先获取到所有的tag信息，且将tag_id保存起来
        all = self.get_tag_list().json()
        # 将所有tag_id返回
        return [id["id"] for tag_id in all["tag_group"] for id in tag_id["tag"]]

    # 编辑tag
    def edit(self,id,name):
        pass