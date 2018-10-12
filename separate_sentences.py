import sys
import os


def separate_by_dot(news_dir):
    news = os.listdir(news_dir)
    print("Separating sentences by dots...")
    for s in news:
        whole_article=""
        with open(os.path.join(news_dir, s), "r") as fr:
            whole_article = fr.read()
        with open(os.path.join(news_dir, s), "w") as fw:
            whole_article = whole_article.replace(".", ". \n \n")
            fw.write(whole_article)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        news_dir = sys.argv[1]
        separate_by_dot(sys.argv[1])

    else:
        print("USAGE: python separate_sentences.py <your_news_dir>")
        sys.exit()