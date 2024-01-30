from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        raise NotImplementedError()


    def bar(self):
        raise NotImplementedError()


class Concrete(Base):
    def foo(self):
        return 'foo() called'



assert issubclass(Concrete, Base)


