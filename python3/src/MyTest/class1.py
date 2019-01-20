from urllib.parse import urlencode
import requests
import re
from bs4 import BeautifulSoup
from itertools import chain
class Youdao(object):
    timeout = 10
    def __init__(self,username,password,cookie):
        super().__init__()
        self.username = username
        self.password = password
        self.cookie = cookie
    def __checkCookie(self):
        if self.cookie:
            rsp = requests.get('http://dict.youdao.com/wordbook/wordlist', cookies=self.cookie)
            if 'account.youdao.com/login' not in rsp.url:
                return True
        return False
    def __simplerequest(self):
        rsp = requests.get('http://dict.youdao.com/wordbook/wordlist')
        print(rsp.text);

    def getTotalPage(self):
        try:
            rsp = requests.get('http://dict.youdao.com/wordbook/wordlist', timeout=self.timeout, cookies=self.cookie)
            groups = re.search('<a href="wordlist.p=(.*).tags=" class="next-page">最后一页</a>', rsp.text, re.M | re.I)
            if groups:
                total = int(groups.group(1)) - 1
            else:
                total = 1
            return total
        except Exception as e:
            self.SIG.exceptionOccurred.emit(e)
            self.SIG.log.emit('网络异常')

    def getWordPerPage(self, pageNumber):
        words = []
        try:
            #self.SIG.log.emit(f'获取单词本第:{pageNumber + 1}页')
            rsp = requests.get(
                'http://dict.youdao.com/wordbook/wordlist',
                params={'p': pageNumber},
                cookies=self.cookie
            )
            soup = BeautifulSoup(rsp.text, features='html.parser')
            table = soup.find(id='wordlist').table.tbody
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                words.append(cols[1].div.a.text.strip())
        #except Exception as e:
        #    self.SIG.progress.emit()
        #    self.SIG.exceptionOccurred.emit(e)
        #    self.SIG.log.emit('网络异常')
        finally:
            return words
    def getWordDescPerPage(self, pageNumber):
        wordsDescDic = {}
        try:
            #self.SIG.log.emit(f'获取单词本注释第:{pageNumber + 1}页')
            rsp = requests.get(
                'http://dict.youdao.com/wordbook/wordlist',
                params={'p': pageNumber},
                cookies=self.cookie
            )
            soup = BeautifulSoup(rsp.text, features='html.parser')
            table = soup.find(id='wordlist').table.tbody
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                wordsDescDic[cols[1].div.a.text.strip()]=cols[3].div.text.strip()
        #    self.SIG.progress.emit()
        #except Exception as e:
        #    self.SIG.progress.emit()
        #    self.SIG.exceptionOccurred.emit(e)
        #    self.SIG.log.emit('网络异常')
        finally:
            return wordsDescDic
    def query(self,remoteWords,remoteWordsDescDic):
        print(self.YoudaoAPIquery(remoteWords[0]))
    def YoudaoAPIquery(self, word):
        timeout = 10
        s = requests.Session()
        url = 'https://dict.youdao.com/jsonapi'
        params = {"dicts": {"count": 99, "dicts": [["ec", "pic_dict"], ["web_trans"], ["fanyi"], ["blng_sents_part"]]}}
        rsp = s.get(
            url,
            params=urlencode(dict(params, **{'q': word}))
        )
        jsonResult = self.parser(rsp.json(), word).json
        return jsonResult
    def getAllWordPage(self):
        dic={}
        for n in range(self.getTotalPage()):
            wordsdescDic = self.getWordDescPerPage(n)
            dic = {**dic,**wordsdescDic}
        return dic    
    def run(self):
        dic=self.getAllWordPage()
        #print(dic)
        print(list(dic.keys()))
        #words = chain(*[self.getWordDescPerPage(n) for n in range(self.getTotalPage())])
        #words = list(words)
        #self.query(words,dic)
        #for  word in words:
        #    print(word)
cookie=dict(DICT_LOGIN='3||1543279876989',DICT_PERS='v2|urstoken||DICT||web||-1||1547954930121||122.224.233.66||junqiangsix@163.com||TuO46zh4k50eFnHgu0MkERQuRfPuRHkWRkfOMPuOfwuRTKOLkf6MQFRgBnMTB6LQyROWh4OlOMeu0PyOLqZhHU5R',DICT_SESS='v2|URSM|DICT||junqiangsix@163.com||urstoken||XagdhwfFFj4coPWQa7lRMuoiQsE.HVY8unmkGyHQ3up3KLq47KPqRQcc6VlGSQJp2XuI7d_z_Kc154w.w80KQeBg7fsmPB36eYLQe8.D5dH4OekwYDLqwVf0buO2cM5b9aDZ8VPJATT1NmLcn7sBR2IdxtsEliK15mgO8UOdxV4as_NpL9LVksM7ilPHfdc.p||604800000||pu6MlEhMpB0TyOMwKhHQFRzEPM6u6LTyRe4kfkl0LYfRzfnMq4nHeuRJShHgu0MpuRJKOMJynHPBRqykMQFOMgLR')
aa=Youdao('aa','bb',cookie)
#aa._Youdao__simplerequest()
print(aa._Youdao__checkCookie())
#for  word in aa.getWordPerPage(1):
#    print(word)
aa.run()
#aa._Youdao__printinfo()

