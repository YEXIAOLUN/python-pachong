import urllib.request
import json
import datetime
import re
import xlwt
'''
m_num = int(input('月份数量：'))
id = input('用户名称：')
file_name=input('请输入要生成的文件名:')
time_now = datetime.datetime.now()
m_year = m_num // 12
m_month = m_num - m_year* 12
proxy_addr="122.241.72.191:808"#代理地址，可以自己在西刺网里找可用的IP
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
##print(url)
'''

def month_sub(time_now, created_at):    
    try:
        now_str = time_now.strftime('%Y-%m-%d')
        new = [int(i) for i in now_str.split('-')]
        old = [int(i) for i in created_at.split('-')]
        new[0] = new[0] - m_year
        new[1] = new[1] - m_month
    except:
        return True
#    print(new, old)
    if(old[0]>new[0]):
        return True  
    elif(old[0] == new[0]):
        if(old[1] >= new[1]):
            return True
        else:
            return False
    else:
        return False

def get_message_page(uurl):#使用代理发送请求
    handler = urllib.request.ProxyHandler({'http':proxy_addr})
    req=urllib.request.Request(uurl)#固定方法
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)#使它全局化，之后不论是什么方法发送请求都将使用自定义代理
    # response = urllib.request.urlopen('https://weibo.com/p/1005055443276821/home?from=page_100505&mod=TAB&is_all=1#place')
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')#获取信息
    return data

def get_message(uurl):#获取基本信息包括昵称性别，主页地址，粉丝数，关注人数等
    data=get_message_page(uurl)
    message=json.loads(data).get('data')
    message=message.get('userInfo')
    name=message.get('screen_name')
    gender=message.get('gender')
    if(gender=='f'):
        gender='女'
    else:
        gender='男'
    profile_url=message.get('profile_url')
    profile_image_url=message.get('profile_image_url')
    verified=message.get('verified')
    if(verified=='True'):
        verified='是'
    else:
        verified='否'
    follow_count=message.get('follow_count')
    followers_count=message.get('followers_count')
    print('昵称:'+name+'\n'+'性别:'+gender+'\n'+'头像:'+profile_image_url+'\n'+'主页:'+profile_url+'\n'+'是否认证:'+verified+'\n'+'粉丝数:'+str(followers_count)+'\n'+'关注人数:'+str(follow_count)+'\n')

def get_containerid(uurl):#获取网页的containerid，观察得之后提取微博信息时网页链接上需要用这个信息
    data=get_message_page(uurl)
    message=json.loads(data).get('data')
    for data in message.get('tabsInfo').get('tabs'):
        if(data.get('tab_type')=='weibo'):
            containerid=data.get('containerid')
            # print(containerid)
            return containerid

def get_all_mes(url,file):#获取微博的信息并且保存至文件
    containerid=get_containerid(url)
    i=1#控制网页页码
    rows = [{'发布时间':'发布时间','微博内容':'微博内容','转发数':'转发数','评论数':'评论数','点赞数':'点赞数','微博地址':'微博地址'}]
    f = 0
    while True:
        main_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+containerid+'&page='+str(i)
        data=get_message_page(main_url)
        weibo=json.loads(data).get('data')
        cards=weibo.get('cards')
        
        if (len(cards) > 0):
            for j in range(len(cards)):
                card_type = cards[j].get('card_type')
                if (card_type == 9):#观察得包含所需微博信息的这个值都是9
                    
                    mblog = cards[j].get('mblog')
                    attitudes_count = mblog.get('attitudes_count')
                    comments_count = mblog.get('comments_count')
                    created_at = mblog.get('created_at')
                    reposts_count = mblog.get('reposts_count')
                    scheme = cards[j].get('scheme')
                    text = mblog.get('text')
                    
                    re_h = re.compile('</?\w+[^>]*>')##正则替换HTML标签
                    text=re_h.sub('', text)

                    if(len(created_at) < 10):
                        created_at =str(time_now.year) + '-' + created_at
                    try:
                        if(j == 0):
                            if(month_sub(time_now, created_at)):
                                rows.append({'发布时间':str(created_at),'微博内容':text,'点赞数':str(attitudes_count),'评论数':str(comments_count),'转发数':str(reposts_count),'微博地址':str(scheme)})
                                with open(file, 'a', encoding='utf-8') as f:
                                    f.write("----第" + str(i) + "页，第" + str(j) + "条微博----" + "\n")
                                    f.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count) + "\n")
                        elif(month_sub(time_now, created_at)):
                            rows.append({'发布时间':str(created_at),'微博内容':text,'点赞数':str(attitudes_count),'评论数':str(comments_count),'转发数':str(reposts_count),'微博地址':str(scheme)})
                            with open(file, 'a', encoding='utf-8') as f:
                                f.write("----第" + str(i) + "页，第" + str(j) + "条微博----" + "\n")
                                f.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count) + "\n")
                        else:
                            f = 1
                            break
                    except:
                        with open(file, 'a', encoding='utf-8') as f:
                                f.write("----第" + str(i) + "页，第" + str(j) + "条微博----" + "\n")
                                f.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count) + "\n")
            i += 1
            if(f == 1):
                break
            
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet(id)
    i = 0; j = 0        
    for temp in rows:
        worksheet.write(i, j, temp['发布时间'])
        j = j + 1
        worksheet.write(i, j, temp['微博内容'])
        j = j + 1
        worksheet.write(i, j, temp['转发数'])
        j = j + 1
        worksheet.write(i, j, temp['评论数'])
        j = j + 1
        worksheet.write(i, j, temp['点赞数'])
        j = j + 1
        worksheet.write(i, j, temp['微博地址'])                                                
        j = 0
        i = i + 1
    workbook.save(file_name + '.xls')
'''
def main():
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
    get_message(url)
    file=id+'.txt'
    get_all_mes(url,file)

main()
'''