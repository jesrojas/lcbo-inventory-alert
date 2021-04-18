class Repository(object):
    def __init__(self, adapter=None):
        self.client = adapter()

    def find_all(self, selector):
        return self.client.find_all(selector)

    def find(self, selector):
        return self.client.find(selector)

    def create(self, item):
        return self.client.create(item)

    def update(self, selector, item):
        return self.client.update(selector, item)

    def delete(self, selector):
        return self.client.delete(selector)
