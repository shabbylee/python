import urllib2

def download(url):
    print "Downloading...", url
    try:
        html = urllib2.urlopen(url).read()
        page = open('page.html', 'w')
        page.write(html)
        page.close()

    except urllib2.URLError as e:
        print "Downloading error:", e.reason
        html = None
    return html


if __name__ == "__main__":
    print ('This is main of module "download_page.py"')
    download('http://www.sohu.com')
