class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def get_class_name(cls):
        return cls.__name__

print(MathUtils.add(5, 7))
print(MathUtils.get_class_name())