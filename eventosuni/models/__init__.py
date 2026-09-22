"""
Pacote Models
-------------
Módulo de inicialização da camada de modelos.
Disponibiliza as entidades principais (Event e Participante) para facilitar 
a importação direta a partir do pacote 'models'.
"""

from models.event import Event
from models.participant import Participante

__all__ = ["Event", "Participante"]