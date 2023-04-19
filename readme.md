### 这是本人在被毕设灌水降重折磨的时候给自己弄的工具，觉得挺好用的就发出来了。在此提醒：虽然有工具，但是还是不能完全依赖哦~
如果有问题可以提 issue 或者 qq 1719705266，但不一定会解决。
# 原理

原始的翻译大法+chatgpt 3.5 。 

中翻日 + 中翻英 + chatgpt提取要点 + 要点翻中 + chatgpt根据要点进行扩充写作。如果有钱买gpt4的话就不用这么大费周章了。

# 快速开始：

## 1.python 安装前置包

```
pip install flask
```
## 2.下载deeplx
下载 [deeplx](https://github.com/OwO-Network/DeepLX/releases/) 他们搞deepl逆向很幸苦的，不要忘了给他们一个星哦（但凡这deepl开个国内支付通道我都要花钱了）。Windows直接下载deeplx_windows_amd64.exe即可

## 3.配置config.ini

先复制你的openai apikey，如果有openai账号而且有额度的话，就可以使用自己的key了。姑且贴一个[链接](https://platform.openai.com/account/api-keys)
例子：
```
[chatgpt]
key=YOUR_API_KEY
```
## 4.打开梯子，deeplx，运行app文件
openai现在已经被墙，访问需要梯子，这个不用多说了。
直接运行前面下载的deeplx文件，并且打开app.py，就会在5000端口打开网页，可以直接运行了！
```
python app.py
```
