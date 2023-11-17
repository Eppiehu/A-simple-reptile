import requests
from bs4 import BeautifulSoup
import sys

# 目标网站的 URL
# 检查是否有命令行参数
if len(sys.argv) > 1:
    # 第一个命令行参数作为 URL
    url = sys.argv[1]
#url = 'https://www.baidu.com'

# 发送 GET 请求 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url,headers=headers)

#response = requests.get(url)
# 检查响应状态码是否为 200 (成功)
if response.status_code == 200:
    print("成功获取网页内容")
else:
    print("获取网页内容失败，状态码：", response.status_code)


# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(response.content, 'html.parser')


# 提取不同类型的内容
titles = soup.find_all('title')
paragraphs = soup.find_all('p')
links = soup.find_all('a')
images = soup.find_all('img')

# 将提取的内容保存到文件中
with open('extracted_content.txt', 'w', encoding='utf-8') as file:
    # 写入标题
    file.write('提取的标题:\n')
    for title in titles:
        file.write(title.get_text() + '\n')
    file.write('\n')

    # 写入段落
    file.write('提取的段落:\n')
    for paragraph in paragraphs:
        file.write(paragraph.get_text() + '\n')
    file.write('\n')

    # 写入链接文本
    file.write('提取的链接:\n')
    for link in links:
        href = link.get('href', '无链接')
        text = link.get_text() or '无文本'
        file.write(f'{text}: {href}\n')
    file.write('\n')

    # 写入图像描述
    file.write('提取的图像描述:\n')
    for img in images:
        alt_text = img.get('alt', '无描述')
        file.write(alt_text + '\n')



# 提取所有的图片链接
images = soup.find_all('img')

base_url = url  # 如果需要，也可以使用 'http:'
i = 0
for img in images:
    img_url = img['src']
    # 如果 URL 以 "//" 开头，那么添加 'http:' 或 'https:'
    if img_url.startswith('//'):
        img_url = 'https:' + img_url
    elif img_url.startswith('/'):
        img_url = base_url + img_url
    # 如果 URL 不以 'http:' 或 'https:' 开头，那么添加基础 URL
    elif not (img_url.startswith('http:') or img_url.startswith('https:')):
        img_url = base_url + '/' + img_url
    
    print("图片 URL:", img_url)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    img_response = requests.get(img_url, headers=headers)

    if img_response.status_code == 200:

        with open(f'{i}.png', 'wb') as file:
            file.write(img_response.content)
            print(f"图片{i}已下载")
    i += 1

