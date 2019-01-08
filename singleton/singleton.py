# -*- coding:utf-8 -*-

class SingletonMetaclass(type):
    """
    通过元类实现单例模式

    pyton 2.x:
    class Sglclass:
        __metaclass__ = SingletonMetaclass
        pass

    pyton 3.x:
    class Sglclass(metaclass=SingletonMetaclass):
        pass
    """

    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = \
                super(SingletonMetaclass, cls).__call__(*args, **kwargs)
            print(cls._instances)
        return cls._instances[cls]


def Test():

    # metaclass
    class Foo:
        __metaclass__ = SingletonMetaclass
        pass

    fooa = Foo()
    foob = Foo()
    print(fooa, foob)

    class Bee:
        __metaclass__ = SingletonMetaclass
        pass

    beea = Bee()
    beeb = Bee()
    print(beea, beeb)

if __name__ == '__main__':
    Test()