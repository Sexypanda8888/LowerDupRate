import requests,json
from requests.adapters import HTTPAdapter
request = requests.Session()
request.mount('http://', HTTPAdapter(max_retries=3))
request.mount('https://', HTTPAdapter(max_retries=3))
import configparser


def getConfig(section,key=None):
    config = configparser.ConfigParser()
    file_path = "./config.ini"
    config.read(file_path,encoding='utf-8')
    if key!=None:
        return config.get(section,key) 
    else:
        return config.items(section)


class TranslateException(Exception):
    def __init__(self, message) -> None:
        self.message = message

class GPTException(Exception):
    def __init__(self, message) -> None:
        self.message = message


#翻日，翻英   gpt提取要点  翻中 gpt输出
# EN JA ZH

Authorization = "Bearer " + getConfig("chatgpt","key")

def translate(lang_from,lang_to,text):
    deeplx_api = "http://127.0.0.1:1188/translate"
    data = {
        "text": text,
        "source_lang": lang_from,
        "target_lang": lang_to
    }
    post_data = json.dumps(data)
    r = request.post(url = deeplx_api, data = post_data)
    r = json.loads(r.text)
    if r["code"] == 200:
        return r["data"]
    else:
        raise Exception("翻译错误")

def gpt_extract(text):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": Authorization,
        "Content-Type": "application/json"
    }
    message = "Please extract important information from the following sentences:\"{}\"".format(text)
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }
    try:
        r = request.post(url,headers=headers,data=json.dumps(data))
        r = json.loads(r.text)
        res = r["choices"][0]["message"]["content"]
    except:
        with open("DEBUG.txt",'a') as f:
            f.write(r.text)
        raise Exception("提取要点时发生错误，已经记录错误包信息")
    return res
    

def gpt_expand(text,length = -1):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    if length == -1:
        message = "根据下面关键信息，用中文写出论文中的一段：\"{}\"".format(text)
    else:
        message = "根据下面关键信息，用中文写出论文中的一段，字数不少于{}token：\"{}\"".format(length,text)
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }
    try:
        r = request.post(url,headers=headers,data=json.dumps(data))
        r = json.loads(r.text)
        res = r["choices"][0]["message"]["content"]
    except:
        with open("DEBUG.txt",'a') as f:
            f.write(r.text)
        raise Exception("扩写时发生错误，已经记录错误包信息")
    return res

def lowerDup(text,legnth = -1):
    try:
        text_1 = translate("ZH","JA",text)
        # print(text_1)
        text_2 = translate("JA","EN",text_1)
        # print(text_2)
        text_extracted = gpt_extract(text_2)
        # print(text_extracted)
        text_3 = translate("EN","ZH",text_extracted)
        # print(text_3)
        result = gpt_expand(text_3,length=legnth)
        return (result,True)
    except Exception as e:
        print(e)
        return (str(e),False)
    
        
if __name__ == "__main__":
    text = "对不良图片的检测最简单快捷的方式就是人工审核, 因为图片信息比较直观，人可以直接判断，但是网络上的图片数以万计，如果通过人工方式进行审核，以现在网络上的图片数量需要耗费的人工成本，是难以想象的。"
    try:
        text_1 = translate("ZH","JA",text)
        # print(text_1)
        text_2 = translate("JA","EN",text_1)
        # print(text_2)
        text_extracted = gpt_extract(text_2)
        # print(text_extracted)
        text_3 = translate("EN","ZH",text_extracted)
        # print(text_3)
        result = gpt_expand(text_3)
    except Exception as e:
        print(e)
        