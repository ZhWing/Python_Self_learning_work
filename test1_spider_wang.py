import requests
import os
import re

dow_path = ''
List = []


def Find(url):
    global List
    print('正在搜索, 请稍候......')
    t = 0
    i = 1
    s = 0
    while t < 1000:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=7)
        except:
            t = t + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                t += 60
    return s


def downloadPicture(url, message):
    if not os.path.exists(dow_path):
        os.mkdir(dow_path)

    try:
        pic = requests.get(url, timeout=5)
        file_path = dow_path + message + '.jpg'
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(pic.content)
            print(file_path, '下载成功!')
        else:
            i = 1
            while True:
                file_path = dow_path + message + '_{}.jpg'.format(i)
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(pic.content)
                    print(file_path, '下载成功!')
                    break
                i += 1
    except:
        print('{}下载失败'.format(url))


def downloadPictures(num, message):
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + message + '&pn='
    for page_i in range(num):
        url_i = url + str(page_i * 60)
        try:
            html = requests.get(url_i, timeout=10).text
            picture_urls = re.findall(r'"objURL":"(.*?)",', html)
            print("正在下载第{}张照片......".format(page_i + 1))
            downloadPicture(picture_urls[10], message)
        except:
            print('{}访问失败!'.format(url_i))


def main():
    message = input("请输入关键词:")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + message + '&pn='
    num_message = Find(url)
    print('经过检测{}类图片共有{}张'.format(message, num_message))
    num_Down = int(input("请输入需要下载的数量:"))
    global dow_path
    dow_path = './' + message + '/'
    downloadPictures(num_Down, message)


if __name__ == '__main__':
    main()
