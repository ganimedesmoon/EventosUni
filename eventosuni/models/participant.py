"""Estrutura que representa uma pessoa inscrita em um evento."""

from dataclasses import dataclass


# ORIENTAÇÃO A OBJETOS:
# Participant é uma classe usada como molde para todos os participantes. Cada
# pessoa inscrita é representada por um objeto criado a partir deste molde.
@dataclass(frozen=True)
class Participant:
    """Guarda os dados acadêmicos básicos de um participante.

    ``frozen=True`` torna o objeto imutável: depois que um participante é
    criado, nome, matrícula e curso não podem ser trocados por acidente. Para
    corrigir alguma informação seria necessário criar um novo participante.
    """

    name: str
    registry: int
    major: str


# FUNCIONAL:
# ``frozen=True`` aplica a ideia de imutabilidade, muito valorizada na
# programação funcional. Um objeto Participant não muda depois de criado,
# reduzindo alterações inesperadas no estado do programa.

# IMPERATIVA:
# Não existem instruções sequenciais que alterem estado neste arquivo. A lista
# que guarda estes objetos é modificada de forma imperativa em data.py.
