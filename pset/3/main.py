'''
Factory Design Pattern
Andrés Martínez - A00227463

Sodafactory, it creates CocaColaFactory and PepsiFactory
'''

from pepsi import PepsiFactory
from cocacola import CocaColaFactory
        
pepsi_factory = PepsiFactory()
cocacola_factory = CocaColaFactory()

pepsi_factory.factory_method()
cocacola_factory.factory_method()
