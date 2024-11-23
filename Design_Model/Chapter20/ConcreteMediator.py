



from abc import ABC, abstractmethod
from Design_Model.Chapter20 import Button, Component, Mediator, TextBox


""" 具体终结者 """
class ConcreteMediator(ABC, Mediator):
    # 维持对各个同事对象的引用
    button:Button
    list:list
    userNameTextBox:TextBox
    