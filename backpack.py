from object import Object


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

    def __init__(self, backpack_contents, object_name):
        self.object_name = object_name
        self.backpack_contents = backpack_contents
        for self.object_name in self.backpack_contents:
            self.backpack_contents.append(self.object_name)

    def organise(self):
        self.backpack_contents.sort()

    def count(self):
        return self.backpack_contents.count()

    def list(self):
        print(self.backpack_contents)

    def add(self):
        if self.object_name is not None:
            self.backpack_contents.append(self.object_name)
            self.organise()

    def search_in_backpack(self):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :return: -1 | False | integer
        """
        return self.object_name

    def remove(self):
        if self.object_name is not None:
            self.backpack_contents.pop(self.object_name)
            self.organise()
