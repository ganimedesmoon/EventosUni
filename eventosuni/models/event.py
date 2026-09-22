"""
Módulo do Evento (Model) - Paradigma Orientado a Objetos (OO)
-----------------------------------------------------------
Representa a entidade 'Evento' no sistema. Encapsula as informações
de identificação, capacidade e a lista de participantes inscritos.
"""

from dataclasses import dataclass, field
from typing import List
from models.participant import Participante


@dataclass
class Event:
    """
    PARADIGMA ORIENTADO A OBJETOS:
    Classe que molda os atributos e comportamentos de um evento acadêmico.
    """
    id: int
    day: str
    month: str
    date: str
    event_type: str
    title: str
    location: str
    capacity: int
    description: str
    inscritos: List[Participante] = field(default_factory=list)

    # --------------------------------------------------------------------------
    # MÉTODOS E PROPRIEDADES OO DE ENCAPSULAMENTO E COMPATIBILIDADE
    # --------------------------------------------------------------------------
    @property
    def registered(self) -> int:
        """
        Propriedade calculada que retorna a contagem atual de inscritos.
        Exigida pelos templates Jinja2 para exibir o progresso de lotação.
        """
        return len(self.inscritos)

    @property
    def vagas_totais(self) -> int:
        """Propriedade auxiliar para os cálculos do módulo de relatórios."""
        return self.capacity

    def __repr__(self) -> str:
        return f"Event(id={self.id}, title='{self.title}', capacity={self.capacity})"