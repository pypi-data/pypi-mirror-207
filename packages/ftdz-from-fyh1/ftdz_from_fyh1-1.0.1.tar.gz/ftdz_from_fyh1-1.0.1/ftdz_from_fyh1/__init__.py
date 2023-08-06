import requests,time
head = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}# 设置请求头，模拟浏览器
#TODO 修改下方需要爬取的网址
url = "https://webfs.tx.kugou.com/202305061951/95e42cdba17ebddcdbeae00f3ffe4c26/v2/07b18d9a40bdc6684c2bf6958a259b55/part/0/960173/KGTX/CLTX001/clip_07b18d9a40bdc6684c2bf6958a259b55.mp3"
# 请求网页
try:
    with open("1.mp3","rb") as f:
        f.read()
except:
    print("正在下载文件")
    res = requests.get(url, headers=head)
        #TODO 取消下面代码的注释，可以保存内容到txt中
    with open("1.mp3", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url1 = "https://static0.xesimg.com/programme/python_assets/fe346bf7a40bf4cfc654afbf712319db.png"
    res = requests.get(url1, headers=head)
    with open("bg2(1).png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/f72664f6e5f9b4fb6116d110b327bc14.png"
    res = requests.get(url, headers=head)
    with open("bullet1.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/6bb8804f499a9ef9c8b3e608195b0aa1.png"
    res = requests.get(url, headers=head)
    with open("olp.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/3882df5166b5951c729c4edf14197958.png"
    res = requests.get(url, headers=head)
    with open("bullet.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/4b141a2446f48f34f6665c4ec8f8d483.png"
    res = requests.get(url, headers=head)
    with open("player.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/e2ee74a6e18b306d991b3cfec34b3ac7.png"
    res = requests.get(url, headers=head)
    with open("base2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/5716eb23b1df0f2ae3466b450b7b896b.png"
    res = requests.get(url, headers=head)
    with open("begin_game2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/102d2130af182b5348df51beed560f5a.png"
    res = requests.get(url, headers=head)
    with open("begin_game1.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/a638df7ae4b37b7f617ad12d9ebb38f1.png"
    res = requests.get(url, headers=head)
    with open("skills1.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/83f6e36c9dab410aab3dd099dd356f3a.png"
    res = requests.get(url, headers=head)
    with open("skills5.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/394822c497a8f6122c911e907ac9ffd9.png"
    res = requests.get(url, headers=head)
    with open("skills3.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/c14ef4eeeb3f48e0e37ba247e8e5525c.png"
    res = requests.get(url, headers=head)
    with open("skills4.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/dc2c4b4025905087c9f3f13273a58cfc.png"
    res = requests.get(url, headers=head)
    with open("skills2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/89acbe63ce741f7405af4930a12bf9aa.png"
    res = requests.get(url, headers=head)
    with open("sn1.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/a07160045b256de82c31cfc9752fb6b9.png"
    res = requests.get(url, headers=head)
    with open("box1.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/c4f9aa645860f9d09d05a29c93c42bf6.png"
    res = requests.get(url, headers=head)
    with open("box2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/e0630b71ab9f3a1b393e362ba20bd826.png"
    res = requests.get(url, headers=head)
    with open("box2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/e0630b71ab9f3a1b393e362ba20bd826.png"
    res = requests.get(url, headers=head)
    with open("box3.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/ce3911ac8b93125af44768d3002c38de.png"
    res = requests.get(url, headers=head)
    with open("sn.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/9b88147cead1214a1f64414576d43cfe.png"
    res = requests.get(url, headers=head)
    with open("skills6.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/9656ef6d4782d6c72a782eaebf69ad81.png"
    res = requests.get(url, headers=head)
    with open("skills7.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/cbf0b1d3617d7137b5db5cb3227b3593.png"
    res = requests.get(url, headers=head)
    with open("skills0.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/ad23089336bdef5124e7a8b94d0a3c5c.png"
    res = requests.get(url, headers=head)
    with open("life.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/776d41fba3921fa6367f776c00ac6058.jpg"
    res = requests.get(url, headers=head)
    with open("19.jpg", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/7267f2f9f10064a5c0466cd07bcb3f83.jpg"
    res = requests.get(url, headers=head)
    with open("h_0.jpg", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/4dd920af5585ace30759030993c73224.jpg"
    res = requests.get(url, headers=head)
    with open("h_1.jpg", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/17ead881718482c93a614205ca056d47.png"
    res = requests.get(url, headers=head)
    with open("help1.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/3a8e530d61a6993198156db982fb16e5.png"
    res = requests.get(url, headers=head)
    with open("help2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/3a8e530d61a6993198156db982fb16e5.png"
    res = requests.get(url, headers=head)
    with open("help2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/a0642e8c138033f7fdc2acc09d704547.jpg"
    res = requests.get(url, headers=head)
    with open("90.jpg", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/39de52c14ded960afd72e19472dffd8f.png"
    res = requests.get(url, headers=head)
    with open("c2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/330918d30463d40ce0a07a31ff4ae9ca.png"
    res = requests.get(url, headers=head)
    with open("bullet2.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/3a5e025bfa957ce409ba0b18a4dccc76.png"
    res = requests.get(url, headers=head)
    with open("7801.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/7bd84268122bdd2be46f52753312e307.png"
    res = requests.get(url, headers=head)
    with open("开.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    url = "https://static0.xesimg.com/programme/python_assets/35c0ba350034dacd5dd738c54d6ca932.png"
    res = requests.get(url, headers=head)
    with open("关.png", "wb") as file:
    #TODO 修改要写入的内容
        file.write(res.content)
    print("下载完毕")
    time.sleep(3)
finally:
    import ftdz_from_fyh1.main