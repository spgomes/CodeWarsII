
from src.services.holeriteServices import HoleriteServices


class Holerite():
    def __init__(self, holeriteServices: HoleriteServices) -> None:
        self.holeriteServices = holeriteServices
        self.__matricula = self.__matricula
        self.__data_admissao = self.__data_admissao
        self.__cargo = self.__cargo
        self.__comissao = self.__comissao

    @property
    def __matricula(self) -> int:
        return self.__matricula
    
    @property
    def __data_admissao(self) -> str:
        return self.__data_admissao
    
    @property
    def __cargo(self) -> str:
        return self.__cargo
    
    @property
    def __comissao(self) -> int:
        return self.__comissao