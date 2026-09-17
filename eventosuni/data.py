"""Camada responsável por consultar e alterar os dados simulados.

As rotas não acessam diretamente as listas do ``mock_db``. Elas usam o
``DataManager``, concentrando neste arquivo as regras de acesso aos eventos e
participantes. Em uma versão futura, esta classe poderia ser substituída por
uma implementação que conversa com um banco de dados real.
"""

from mock_db import EVENTS, MAP_EVENT_PARTICIPANT
from models.event import Event
from models.participant import Participant


class DataManager():
    """Oferece operações simples sobre o banco de dados mantido em memória.

    ORIENTAÇÃO A OBJETOS:
    A classe agrupa operações relacionadas aos dados. Seus métodos são
    estáticos porque não dependem de um objeto DataManager específico.
    """

    @staticmethod
    def get_events():
        """Retorna a lista de eventos que está disponível no mock database."""

        return EVENTS

    @staticmethod
    def get_event_by_id(event_id):
        """Procura um evento pelo ID e retorna ``None`` quando não o encontra.

        A expressão geradora examina os eventos um de cada vez. ``next`` para
        assim que encontra o primeiro evento cujo ID corresponde ao solicitado.
        """

        # PROGRAMAÇÃO FUNCIONAL:
        # A expressão geradora descreve o filtro desejado sem criar uma lista
        # intermediária. ``next`` devolve somente o primeiro resultado.
        return next(
            (event for event in EVENTS if event.id == event_id),
            None
        )

    @staticmethod
    def get_participants_of_event(event_id):
        """Retorna os participantes de um evento ou uma lista vazia."""

        return MAP_EVENT_PARTICIPANT.get(event_id, [])

    @staticmethod
    def add_participant(event_id, name, registry, major):
        """Inscreve uma pessoa se o evento existe e ainda possui vaga.

        O retorno booleano simplifica o uso na rota: ``True`` significa que a
        inscrição ocorreu; ``False`` significa que ela precisou ser recusada.
        """

        # ORIENTAÇÃO A OBJETOS:
        # Chamamos um método da classe e, mais abaixo, construímos um objeto da
        # classe Participant para representar a pessoa inscrita.
        event = DataManager.get_event_by_id(event_id)
        participants = MAP_EVENT_PARTICIPANT.get(event_id)

        # Um evento válido deve ter uma lista no mapa e uma vaga disponível.
        if event is None or participants is None or event.registered >= event.capacity:
            return False

        # Os dois valores são atualizados juntos para a lista e o contador
        # continuarem representando a mesma quantidade de inscritos.
        # PROGRAMAÇÃO IMPERATIVA:
        # append e += alteram estruturas já existentes. O estado depois dessas
        # instruções é diferente do estado anterior.
        participants.append(Participant(name=name, registry=registry, major=major))
        event.registered += 1
        return True

    @staticmethod
    def add_event(day, month, date, event_type, title, location, capacity, description):
        """Cria um evento e prepara uma lista vazia para seus participantes."""

        # O maior ID atual recebe mais um. ``default=0`` também permite cadastrar
        # corretamente o primeiro evento caso a lista comece vazia.
        # PROGRAMAÇÃO FUNCIONAL:
        # A expressão geradora transforma cada evento em seu ID, e max reduz
        # esses valores ao maior deles sem um laço manual com variável auxiliar.
        event_id = max((event.id for event in EVENTS), default=0) + 1

        # ORIENTAÇÃO A OBJETOS:
        # Event(...) chama o construtor da classe e produz um novo objeto.
        event = Event(
            id=event_id,
            day=day,
            month=month,
            date=date,
            type=event_type,
            title=title,
            location=location,
            registered=0,
            capacity=capacity,
            description=description,
        )

        # O evento entra na lista geral e ganha sua própria entrada no mapa.
        # PROGRAMAÇÃO IMPERATIVA:
        # As duas instruções abaixo alteram as coleções globais em memória.
        EVENTS.append(event)
        MAP_EVENT_PARTICIPANT[event_id] = []
        return event
