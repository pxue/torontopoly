import rx
from rx import Observable, Observer

class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)
        
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("Sequence completed")

myob = MyObserver()

def do(x):
    print x

def complete():
    print "completed"

def has_error():
    print "er"

Observable.interval(1000).\
        take(5).\
        subscribe(lambda x: do(x), None, complete)

