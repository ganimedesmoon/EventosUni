"""Estrutura que representa um evento acadêmico no sistema."""

from dataclasses import dataclass


# ORIENTAÇÃO A OBJETOS:
# Event é uma classe: ela define um modelo comum para criar objetos que possuem
# dados de um evento. Cada evento criado é uma instância independente da classe.
@dataclass
class Event:
    """Reúne todos os dados necessários para exibir e controlar um evento.

    O decorador ``@dataclass`` cria automaticamente tarefas repetitivas, como
    o método construtor. Assim, basta declarar abaixo os campos que todo evento
    deve possuir.

    ``day``, ``month`` e ``date`` guardam formatos diferentes da mesma data
    porque as telas exibem essa informação de maneiras diferentes. Já
    ``registered`` e ``capacity`` permitem calcular quantas vagas ainda restam.
    """

    id: int
    day: str
    month: str
    date: str
    type: str
    title: str
    location: str
    registered: int
    capacity: int
    description: str


# IMPERATIVA:
# Não há comandos que alterem dados neste arquivo. Entretanto, Event não usa
# ``frozen=True`` e, por isso, seus objetos são mutáveis. A alteração imperativa
# de ``event.registered`` ocorre mais tarde, dentro de data.py.

# FUNCIONAL:
# Este arquivo não implementa funções puras ou transformações de coleções. Ele
# serve principalmente como exemplo de modelagem orientada a objetos.
