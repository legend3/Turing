



from abc import ABC, abstractmethod

""" 具体中介者 """
class ConcreteMediator(ABC):
    # 维持对各个同时对象的引用
    