from Projeto_Novo.models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def set_idade(self, idade):
        if _verificar_idade_negativa(idade):
            self._idade = idade
        else: 
            self._idade = idade

    def _verificar_idade_negativa(self, idade) -> int:
        if idade < 0:
            self._idade = 0
        return True

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
        )