import generateallurl
import opt
import time
import sys
import threading
import Queue
import datetime
import generateallurl
import opt
import time
import sys

#import kick

queue = Queue.Queue()
file = open ('category2.txt' , 'w')
urls = generateallurl.seekurl(1,54,200)#oringal(1,54,200)11-54
#file.write(urls[i]+'\n')
#file = open('url.txt'.'r')

for i in xrange(0, len(urls)):
    file.write(urls[i]+'\n')
#class ThreadClass(threading.Thread):
#    def __init__(self, queue):
#        threading.Thread.__init__(self)
#        self.queue = queue
#    def run(self):
#        while 1:
#            target = self.queue.get()
#            item = kick.webscraper(target)

#            self.queue.task_done()


#def main():

#    for j in xrange(4):
#        t = ThreadClass(queue)
#        t.setDaemon(True)
#        t.start()
#        for url in urls:
#            queue.put(url)
#    queue.join()
#main()
