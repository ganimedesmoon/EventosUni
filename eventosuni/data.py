"""
Módulo DataManager (Gestão de Dados)
------------------------------------
Responsável por intermédiar o acesso e a manipulação dos dados armazenados 
no banco em memória (mock_db).

- Paradigma Imperativo: Controle de fluxo e modificações no estado em memória.
- Paradigma OO: Manipulação de instâncias das classes Event e Participante.
"""

from typing import List, Optional
from models.event import Event
from models.participant import Participante
import mock_db


class DataManager:
    """
    Classe de serviços estáticos para consulta e persistência temporária 
    dos eventos e inscritos.
    """

    @staticmethod
    def get_events() -> List[Event]:
        """Retorna a lista completa de eventos cadastrados."""
        return mock_db.EVENTS

    @staticmethod
    def get_event_by_id(event_id: int) -> Optional[Event]:
        """
        Busca um evento pelo seu identificador único.
        Retorna o objeto Event se encontrado ou None caso contrário.
        """
        for event in mock_db.EVENTS:
            if event.id == event_id:
                return event
        return None

    @staticmethod
    def get_participants_of_event(event_id: int) -> List[Participante]:
        """Retorna a lista de participantes inscritos no evento informado."""
        event = DataManager.get_event_by_id(event_id)
        if event:
            return event.inscritos
        return []

    @staticmethod
    def add_event(day: str, month: str, date: str, event_type: str, 
                  title: str, location: str, capacity: int, description: str) -> Event:
        """
        PROGRAMAÇÃO IMPERATIVA & OO:
        Cria um novo evento com ID incremental e adiciona à coleção global.
        """
        new_id = max([e.id for e in mock_db.EVENTS], default=0) + 1
        
        new_event = Event(
            id=new_id,
            day=day,
            month=month,
            date=date,
            event_type=event_type,
            title=title,
            location=location,
            capacity=capacity,
            description=description,
            inscritos=[]
        )
        
        mock_db.EVENTS.append(new_event)
        mock_db.MAP_EVENT_PARTICIPANT[new_id] = new_event.inscritos
        return new_event

    @staticmethod
    def add_participant(event_id: int, participant: Participante) -> bool:
        """
        PROGRAMAÇÃO IMPERATIVA:
        Verifica o limite de vagas disponíveis antes de alterar o estado.
        Adiciona o participante e retorna True se a inscrição for realizada.
        """
        event = DataManager.get_event_by_id(event_id)
        
        if event and len(event.inscritos) < event.capacity:
            event.inscritos.append(participant)
            return True
            
        return False