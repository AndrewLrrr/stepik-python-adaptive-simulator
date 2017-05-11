from unittest import TestCase
from modify_list import modify_list


class TestModifyList(TestCase):
    def test1(self):
        lst = [1, 2, 3, 4, 5, 6]
        modify_list(lst)
        self.assertEquals([1, 2, 3], lst)
        modify_list(lst)
        self.assertEquals([1], lst)

    def test2(self):
        lst = [10, 5, 8, 3]
        modify_list(lst)
        self.assertEquals([5, 4], lst)
        modify_list(lst)
        self.assertEquals([2], lst)
        modify_list(lst)
        self.assertEquals([1], lst)
        modify_list(lst)
        self.assertEquals([], lst)

    def test3(self):
        lst = [2, 2, 2, 2, 2, 4]
        modify_list(lst)
        self.assertEquals([1, 1, 1, 1, 1, 2], lst)
        modify_list(lst)
        self.assertEquals([1], lst)


