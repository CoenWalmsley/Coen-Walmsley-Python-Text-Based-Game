import object


class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items (in main file)
    ToDo: [X] Count items
    ToDo: [X] in backpack
    ToDo: [X] Sort Items

    """

    def __init__(self, backpack_contents, object_name):
        """

        :param backpack_contents: List of the content's in the backpack (list of the object instances once collected)
        :param object_name:  The name of the objects in the backpack
        """
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
        :return: -1 | False | integer
        """

        def binary_search(arr, min, max, value):
            if max >= min:
                middle_value = (max + min) // 2
                if arr[middle_value] == value:
                    return middle_value
                elif arr[middle_value] > value:
                    return binary_search(arr, min, max - 1, value)
                else:
                    return binary_search(arr, middle_value + 1, max, value)

            else:
                return -1

        search_result = binary_search(self.backpack_contents, 0, len(self.backpack_contents) - 1, object.Object)
        if search_result != -1:
            print("Element is present at index", str(search_result))
        else:
            print("Element is not present in array")

        return self.object_name

    def remove(self):
        if self.object_name is not None:
            self.backpack_contents.pop(self.object_name)
            self.organise()
