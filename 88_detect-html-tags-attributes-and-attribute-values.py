from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('->',attr[0],'>',attr[1])
    
parser = MyHtmlParser()
html = ''
for i in range(int(input())):
    html += input()
parser.feed(html)
