class Event:
    def __init__(self):
        self.handlers = set()

    def handle(self, handler):
        self.handlers.add(handler)
        return self

    def un_handle(self, handler):
        try:
            self.handlers.remove(handler)
        except:
            raise ValueError("Handler is not handling this event, so cannot un handle it.")
        return self

    def fire(self, *args, **kargs):
        for handler in self.handlers:
            handler(*args, **kargs)

    def get_handler_count(self):
        return len(self.handlers)

    __iadd__ = handle
    __isub__ = un_handle
    __call__ = fire
    __len__ = get_handler_count
