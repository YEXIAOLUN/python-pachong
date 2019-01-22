import bs4
f=open('d://abc//火车票.txt','r',encoding='utf8')
text=f.read()
bs=bs4.BeautifulSoup(text,'lxml')
ticket=bs.find(id='queryLeftTable')
tickets=ticket.find_all(name='tr')
for i in tickets:
    try:
        print(i.find(class_='number').text)
    except:
        print()
