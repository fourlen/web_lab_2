import time
import webbrowser

def show_webpages(webpages, interval):
    for webpage in webpages:
        webbrowser.open(webpage)
        time.sleep(interval)

if __name__ == "__main__":
    webpages = [
        "file:///Users/fourlen/web/lab1/Sample01.html",
        "file:///Users/fourlen/web/lab1/Sample02.html",
        "file:///Users/fourlen/web/lab1/Sample03.html"
    ]
    interval = 5  # задаем интервал показа в секундах
    
    show_webpages(webpages, interval)


