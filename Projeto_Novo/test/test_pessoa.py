import pytest
from Projeto_Novo.models.pessoa import Pessoa
from Projeto_Novo.models.enums.sexo import Sexo

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Marta", 22, Sexo.FEMININO)
    return pessoa

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Marta"

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 22