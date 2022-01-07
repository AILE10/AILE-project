from bilibili_api import video, sync
import  stylecloud
import  jieba
bvid=input("请输入BV号:")
data_=input("若获取历史弹幕请输入特定年.月.日：")
page=input("请输入分p号:")
v = video.Video(bvid=bvid)
dms = sync(v.get_danmakus(page_index=int(page)))
file = open('first.txt', 'w+',encoding='utf-8')
for dm in dms:
	file.write(str(dm)+'\n')
file.close()
def ciyun():
    with open('first.txt', 'r', encoding='utf-8') as f:
        word_list = jieba.cut(f.read())
        result = " ".join(word_list)  # 分词用空格隔开
    stopwords = open('D:\CODE\stopwords-master/hit_stopwords.txt', encoding='utf-8').read().split('\n')
    stylecloud.gen_stylecloud(
        text=result,
        size=512,
        font_path='msyh.ttc',
        palette='scientific.sequential.Davos_12',
        gradient='horizontal',
        icon_name='fas fa-fire',
        output_name='first.png',
        background_color="black",
        custom_stopwords=stopwords)
def main():
    ciyun()
if __name__ == '__main__':
    main()