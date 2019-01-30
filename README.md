# zi5book
要不要先star一波，book.zi5.me全站kindle电子书籍爬取，按照作者书籍名分类，每本书有mobi和equb两种格式，采用分布式进行全站爬取
# tips
需要安装pillow，pillow有相关依赖库，需要翻***墙访问，20190130可以正常使用
> sudo apt-get install libjpeg-dev

> pip3 install pillow




#最新安装操作

# 没有python3环境

下载anaconda3 https://www.anaconda.com/download/#linux

https://repo.anaconda.com/archive/



wget https://repo.anaconda.com/archive/Anaconda3-5.0.1-Linux-x86_64.sh

chmod +x Anaconda3-5.0.1-Linux-x86_64.sh

./Anaconda3-5.0.1-Linux-x86_64.sh



一路yes即可，除了最后的安装vscode



# 安装依赖包

conda install scrapy(也可以pip install scrapy，有时候容易安装错误) 

pip install scrapy_redis

pip install pymongo



# 安装redis和mongodb

sudo apt-get install redis-server

sudo apt-get install mongodb





# 运行

git clone https://github.com/guapier/zi5book.git

cd zi5book

python3 main.py即可



# 可能出现的错误的解决方案

```ba's
UnicodeEncodeError: 'ascii' codec can't encode characters in position 25-31: ordinal not in range(128)

sudo apt-get install language-pack-zh-hans

    
    
首先要从Ubuntu语言设置那里，把中文语言包安装上

打开/etc/environment
在下面添加如下两行
LANG=zh_CN.UTF-8
LANGUAGE=zh_CN:zh:en_US:en

打开 /var/lib/locales/supported.d/local
添加zh_CN.GB2312字符集，如下：
en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
zh_CN.GBK GBK
zh_CN GB2312
保存后，执行命令：
sudo locale-gen

打开/etc/default/locale
修改为：
LANG=”zh_CN.UTF-8″
LANGUAGE=”zh_CN:zh:en_US:en”
```






