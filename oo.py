import abc


class Test(object):

    def __init__(self):
        self.value = 0

    def set_name(self, val):
        self.value = val

    def get_val(self):
        return self.value


class Animal(object):

    inst_count = 0

    @classmethod
    def get_instance_count(cls):
        return cls.inst_count

    # Use as utility method
    @staticmethod
    def check_path(value):
        if len(value) == 0:
            return True
        else:
            return False

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Dog(Animal):
    def __init__(self, sound, name):
        self.sound = sound
        super(Dog, self).__init__(name)

    def get_sound(self):
        return self.sound


class Cat(Animal):
    def __init__(self, sound, name):
        self.sound = sound
        super(Cat, self).__init__(name)

    def get_sound(self):
        return self.sound


# Abstract classes
class GetterSetter(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_value(self, value):
        return

    @abc.abstractmethod
    def get_value(self):
        return


class MyGetterSetter(GetterSetter):
    def __init__(self):
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

