import jieba
news = open("news.txt",encoding='UTF-8')
news_read = news.readlines()
while "\n" in news_read:
	news_read.remove("\n")
news1 = (" ".join(news_read))
news1 = news1.replace("\n",'')
for ch in '。，：；？！@‘“’”、（）《》':
	news1 = news1.replace(ch," ")
news1 = news1.replace(" ","")
#news2 = jieba.cut(news1, cut_all=True)

#while " " in news3:
#	news3.remove(" ")

print(news1)
input()