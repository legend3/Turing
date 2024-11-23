



from abc import ABC, abstractmethod
from Design_Model.Chapter20 import Component


""" 抽象中介者 """
class Mediator(ABC):
    @abstractmethod
    def componentChanged(self, c:Component):
        pass