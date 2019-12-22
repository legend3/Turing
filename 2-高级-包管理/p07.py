#直接导入一个包，可以使用__init__.py中的内容
import pkg01

pkg01.inInit()


#此种方法是默认对__init__.py内容的导入
import pkg01 as pp

pp.inInit()