# 简单的爬虫

这是一个简单的爬虫实现，利用requests库和beautifulsoup库实现网页爬取，基本的网站都可以（特别是各大学校网站官网清华，北大等）。

## 项目描述

用的是python和c++写出来的，核心是python代码，也就是test.py文件。用qt写了一个非常简单的界面，套了一下。该项目仅供学习交流使用，是很简单的实现，我们可以一起学习进步。

## 使用

如果想要仅仅使用体验，直接下载exe文件夹就可以，将两个exe放在同一个目录下，运行界面.exe。
输入网址点击确定即可，爬取的数据将会在当前目录下。
注意：网址不要添加最后的“/”。如“https://www.baidu.com”就是可以的，而最好不要“https://www.baidu.com/”

## 安装

如果想不仅仅去使用，而是深究代码，可以像下面这样配置。项目依赖于 Python 。确保您的系统中安装了 Python，并且可以通过以下命令安装所需要的依赖库：

```bash
pip install numpy
pip install BeautifulSoup
pip install sys



