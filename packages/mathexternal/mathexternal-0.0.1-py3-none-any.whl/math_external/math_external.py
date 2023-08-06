# coding=utf-8


class MathExternal(int):
    def __init__(self, elem):
        self.elem = elem
        super().__init__()

    def __len__(self):
        return self.elem
