class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)


class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == 'Request 1':
            print("ConcreteHandler1 handles {}".format(request))
        else:
            super().handle_request(request)


class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == 'Request 2':
            print("ConcreteHandler2 handles {}".format(request))
        else:
            super().handle_request(request)


class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == 'Request 3':
            print("ConcreteHandler3 handles {}".format(request))
        else:
            super().handle_request(request)


# Client code
def main():
    handler3 = ConcreteHandler3()
    handler2 = ConcreteHandler2(handler3)
    handler1 = ConcreteHandler1(handler2)

    requests = ['Request 1', 'Request 2', 'Request 3', 'Request 4']

    for request in requests:
        handler1.handle_request(request)


if __name__ == "__main__":
    main()
