class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items (in main file)
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items):
        self._backpack = []
        if items is None:
            items = []
        if type(items) != "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def sort(self):
        self._backpack.sort()

    def count(self):
        return self._backpack.count(self._backpack)

    def list(self):
        print(self._backpack)

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        return None

    def remove(self, item):
        if item is not None:
            self._backpack.pop(item)
            self.sort()
