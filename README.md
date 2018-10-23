注：非原创 ，原作者地址github https://github.com/megachweng/Dict2Anki/releases/tag/v2.0)中下载，
只是对他进行了按自己的需求进行了细微修改

**从v3.0版本开始需要登录有道词典或欧路词典完成同步**  
**Require Login first from verstion v3.0**
# Dict2Anki
##### **只支持 Anki 2.0.x.**  
**Only supports Anki 2.0.x.**    
**Dict2Anki** 是一款方便[有道词典](http://cidian.youdao.com/multi.html)、[欧陆词典](https://www.eudic.net/)用户同步生成本地单词本卡片至[Anki](https://apps.ankiweb.net/#download)的插件  
**Dict2Anki** is a Anki addon makes it easy for [Youdao](http://cidian.youdao.com/multi.html) and [Eudict](https://www.eudic.net/) user to sync their wordBook card to [Anki](https://apps.ankiweb.net/#download)

## 特点介绍 Feature
- 支持导入有道词典、欧陆词典生词本  
  Support Youdao and Eudict 

- 支持Mac、Windows平台  
  Support Mac and Windows operating system

- 检测词典软件的生词变化,并在Anki中相应的添加删除卡片  
  Detect the change of the wordlist and do the corresponding process  

- 支持获取图片和发音  
  Support pronunciation and image 

## 预览 Preview
- ### 界面 GUI
  <img src = "https://raw.githubusercontent.com/megachweng/Dict2Anki/master/screenshots/GUI.PNG" width=400>

- ### 卡片 Cards
  <span><img src = "https://raw.githubusercontent.com/megachweng/Dict2Anki/master/screenshots/card-front.png" width=400></span>
  <span><img src = "https://raw.githubusercontent.com/megachweng/Dict2Anki/master/screenshots/card-back.png" width=400></span>
## 如何安装 How to Install
- ### 从源码安装（推荐）Install from source(highly suggest)
    - 在[Release](https://github.com/megachweng/Dict2Anki/releases/tag/v2.0)中下载最新版本  
      Download lastest version from [Release](https://github.com/megachweng/Dict2Anki/releases/tag/v2.0)  

    - 解压`Zip`    
      Unzip

    - 把`PluginEntry.py 和 Dict2Anki目录` 放入Anki的`Addons`目录  
      Move `Dict2Anki.py and Dict2Anki directory` to `Addons` directary

    - 重启Anki  
      Restart Anki 

- ### 从AnkiWeb安装 Install from AnkiWeb
    - 打开 `工具` -> `插件` -> `浏览&安装`  
    Click `Tools` -> `Add-ons` -> `Browse&Install` 

    - `代码` : `480644339`  
    `Code`: `480644339`

    - 重启Anki  
    Restart Anki 
## 如何使用 How to Use
<span><img src = "https://raw.githubusercontent.com/megachweng/Dict2Anki/master/screenshots/firstsync.gif" ></span>
<span><img src = "https://raw.githubusercontent.com/megachweng/Dict2Anki/master/screenshots/secondsync.gif" ></span>

2018-10-17
addon 文件夹为 源码 未做修改

Dict2Anki 文件夹 加入了单词释义的导入

python2 文件夹 为对源码修改后的Python2的版本

python3 文件夹 为对源码修改后的Python3的版本（本级只有python3 环境， 而Dict2Anki 为python2 编写；所以python2先转化出python3代码修改测试后 转为 python2代码（可以使用3to2工具)
	Dict2AnkiEditV2 加入 输出日志到本地文件件 方便查找问题