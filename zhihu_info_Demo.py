# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json


class WeiBo:
    def __init__(self):
        self.start_url = 'https://www.zhihu.com/api/v4/members/kaifulee/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            "Cookie": 'ALF=1554689630; SCF=Agk73soAs_wI_KMj1xD_Tjp6skFq_xra-SOjeMvemIEw5nprJukENV8JKmm7IWNHy88JFvCVXWQGohJnc-kLv1s.; SUB=_2A25xh9VvDeRhGeVI61AV9CbFwzyIHXVSi_snrDV6PUJbktANLXmskW1NTA50IkjM-hVv0pppp_5xpMQm4sInE8CC; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFDPAQMPiQJajRR6WpWahnI5JpX5K-hUgL.FoecehzXShn41h52dJLoI0YLxK-LBK-LBK-LxKqL1KqLB-qLxKnL122LB-BLxKnL1K-LB.-LxKBLB.2L1-2LxKnLBK5L1-zLxKnL1-BLBoqt; SUHB=0JvwtYUvUbA7gp; SSOLoginState=1552131391; MLOGIN=1; _T_WM=f0514621764cd032150e5fceda3227b3; WEIBOCN_FROM=1110003030; XSRF-TOKEN=9a73a9; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1005052866934782%26fid%3D231051_-_fans_intimacy_-_2866934782%26uicode%3D10000011'
        }

    def get_start_json(self):
        url = self.start_url
        resp = requests.get (url, headers=self.headers)
        resp = resp.content.decode ()
        jsons = json.loads (resp)

        return jsons

    def get_page(self):
        json = self.get_start_json ()

        total = json['paging']['totals']
        if total % 20 == 0:
            page = total // 20
        else:
            page = (total // 20) + 1

        return page

    def get_url_list(self):
        page = self.get_page ()
        url_list = []
        for i in range (page + 1):
            url = self.start_url.format (i * 20)
            url_list.append (url)

        return url_list

    def get_json_list(self):
        url_list = self.get_url_list ()
        json_list = []
        for url in url_list:
            resp = requests.get (url, headers=self.headers)
            resp = resp.content.decode ()
            json_str = json.loads (resp)
            json_list.append (json_str)
        return json_list

    def get_user_info(self):
        json_list = self.get_json_list ()
        # print (json_list)
        user_info =[]
        try:
            for json in json_list:
                for i in range (20):
                    info = json['data'][i]
                    name = info['name']
                    headline = str(info['headline'])
                    user_url = str(info['url'])
                    url_token = str(info['url_token'])
                    fans = str(info['follower_count'])
                    head_pic = str(info['avatar_url'])
                    gender = str(info['gender'])
                    is_vip = str(info['vip_info']['is_vip'])
                    answer = str(info['answer_count'])
                    user_info.append(name)
                    user_info.append(headline)
                    user_info.append(answer)


            print(user_info)





                    # print('名字:'+name+'\n'+'头像:'+head_pic+'\n'+'介绍:'+headline+'\n'+'知乎地址:'+'https://www.zhihu.com/people/'+url_token+'/following'+'\n'+'粉丝数:'+fans+'\n'+'性别:'+gender+'\n'+'是否为会员:'+is_vip+'\n'+'他的回答数:'+answer)
                    # print('-------------------------------------------------------------------------')
        except Exception as e:
            print(user_info)
            print(len(user_info))



if __name__ == '__main__':
    a = WeiBo ()
    a.get_user_info ()





