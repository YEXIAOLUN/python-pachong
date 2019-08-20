import requests
def main():
    page=1
    for i in range(1,244):
        url='http://www.dlsstax.com/dianzishu/sheshuipanli/files/mobile/'+str(page)+'.jpg'
        res=requests.get(url)
        with open(r'C:\Users\yexiaolun\Desktop\pictures\\'+str(page)+'.jpg','wb') as f:
            f.write(res.content)
        page+=1
if __name__=="__main__":
    main()
