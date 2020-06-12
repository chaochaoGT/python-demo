# utf-8
import requests as req
import json
from urllib.parse import quote


class Musicinfo():

    def __init__(self, input, name, type, page):
        self.input = input
        self.name = name
        self.type = type
        self.page = page

    def __str__(self):
        return '''input=%s,name=%s,type=%s,page=%d'''%(self.input, self.name, self.type, self.page)


#
# type=["kuwo",'netease','qq','xiami','baidu','kugou','1ting','migu','lizhi','qingting','ximalaya','kg','5singyc']
#

# 无损 type =['song']
# params={'input':'陈奕迅',}

def getdata(input, type):
    return Musicinfo(input, 'name', type, '1')


def downSong1(url, data):
    header={'origin':'https://www.769sc.com',
            'ec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest'}
    resp = req.post(url, data,headers=header)
    if len(resp.text)>0:
        ms = (json.loads(resp.text))['data']
        download_music(ms,'F:\music\\')



def download_music(ms,path):
    """下载音乐"""
    if len(ms)>0:
        for m in ms:
            fm=path+m['title']+'-'+m['author']+'.mp3'
            response = req.get(m['url'])
            content = response.content
            with open(file=fm, mode="wb") as f:
                f.write(content)


""" type: post\get  """
def downSong(requType,songName,type,author,page,size,code):

    if 'post'.__eq__(requType):
        www = 'https://www.769sc.com/'
        data = {'input':songName,'filter':'name','type': type,'page': page}
        downSong1(www, data)

    elif 'get'.__eq__(requType):
        url1='''https://api.sounm.com/tencent/search?keyword=%s&type=%s&format=1&page=%s&pageSize=%s'''%(songName,type,page,size)
        header={'origin':'https://wsmusic.sounm.com',
                'ec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'unlockcode': code}
        resp = req.get(url1, headers=header)
        if len(resp.text)>0:
            data = (json.loads(resp.text))['data']

            ms=[]
            if len(data['list'])>0:
                for id in data['list']:

                    url2='https://api.sounm.com/tencent/song?id='+quote(id['id'],'utf-8')

                    sminfo= req.get(url2, headers=header)

                    if len(sminfo.text) <=0:
                        continue
                    else:
                        minfo = (json.loads(sminfo.text))['data']
                        url3='https://api.sounm.com/tencent/url?id='+quote(minfo['id'],'utf-8')+'&quality=flac&isRedirect=0'
                        sinfo= req.get(url3, headers=header)

                        if len(sinfo.text)>0:
                            surl=((json.loads(sinfo.text))['data'])[0]
                            info={'title':minfo['name'],'author':(minfo['singers'])[0],'url':surl}
                            ms.append(info)

                download_music(ms,'F:\music\wusun\\')


if __name__ == "__main__":

    # downSong('post','轻音乐','baidu','','1','','')
    downSong('get','热歌榜','song','','1','1','8943')


