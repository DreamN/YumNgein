import re


class regFnDetector():

    def __init__(self):
        self.fnDicts = {}

    def route(self, str_route):
        def decorator(f):
            self.fnDicts[str_route] = f
            return f
        return decorator

    def serve(self, str_path, sender):
        # fn = self.fnDicts.get(str_path)

        for p in self.fnDicts:
            x = re.compile(p).match(str_path)
            # print("Compare {} with {}".format(p[0], str_path))
            if x:
                kwargs = x.groupdict() #Got Param
                kwargs['sender'] = sender
                return self.fnDicts[p](**kwargs)

        return "Unknown Command! :("
