"""
Módulo Mock Database (Base de Dados em Memória)
----------------------------------------------
Simula a camada de persistência da aplicação EventosUni.
Contém os dados iniciais de eventos, inscritos e a base oficial de
pessoas cadastradas na instituição para as validações do Paradigma Lógico.
"""

from models.event import Event
from models.participant import Participante


# ------------------------------------------------------------------------------
# 1. EVENTOS INICIAIS (ORIENTAÇÃO A OBJETOS)
# ------------------------------------------------------------------------------
EVENTS = [
    Event(
        id=1,
        day="15",
        month="SET",
        date="15/09/2026",
        event_type="WORKSHOP",
        title="Workshop de Python",
        location="Laboratório 2",
        capacity=30,
        description="Aprenda os fundamentos da linguagem Python e desenvolva os seus primeiros programas."
    ),
    Event(
        id=2,
        day="20",
        month="SET",
        date="20/09/2026",
        event_type="PALESTRA",
        title="Inteligência Artificial na Atualidade",
        location="Auditório A",
        capacity=60,
        description="Aprenda os fundamentos de IA e aprenda a treinar modelos!"
    )
]


# ------------------------------------------------------------------------------
# 2. LISTAS DE PARTICIPANTES INICIAIS
# ------------------------------------------------------------------------------
PARTICIPANTS_EVENT_1 = [
    Participante(nome='Ana Beatriz Lima', idade=20, vinculo='estudante', matricula='20261047', matriculado=True),
    Participante(nome='Bruno Henrique Alves', idade=21, vinculo='estudante', matricula='20262781', matriculado=True),
    Participante(nome='Camila Rodrigues', idade=19, vinculo='estudante', matricula='20264429', matriculado=True),
    Participante(nome='Diego Martins', idade=22, vinculo='comunidade', matricula='20264428', matriculado=True),
    Participante(nome='Elisa Fernandes', idade=20, vinculo='estudante', matricula='20267218', matriculado=True),
    Participante(nome='Felipe Santos', idade=21, vinculo='estudante', matricula='20268654', matriculado=True),
    Participante(nome='Gabriela Costa', idade=19, vinculo='estudante', matricula='20270136', matriculado=True),
    Participante(nome='Hugo Nascimento', idade=23, vinculo='comunidade', matricula='20270132', matriculado=True),
    Participante(nome='Isabela Moura', idade=20, vinculo='estudante', matricula='20273397', matriculado=True),
    Participante(nome='João Victor Rocha', idade=22, vinculo='estudante', matricula='20274620', matriculado=True),
    Participante(nome='Karina Oliveira', idade=19, vinculo='estudante', matricula='20276185', matriculado=True),
    Participante(nome='Lucas Pereira', idade=24, vinculo='comunidade', matricula='202323397', matriculado=True),
    Participante(nome='Mariana Souza', idade=20, vinculo='estudante', matricula='20279261', matriculado=True),
    Participante(nome='Nicolas Ribeiro', idade=21, vinculo='estudante', matricula='20280573', matriculado=True),
    Participante(nome='Olivia Barros', idade=19, vinculo='estudante', matricula='20282149', matriculado=True),
    Participante(nome='Pedro Azevedo', idade=25, vinculo='comunidade', matricula='20227897', matriculado=True),
    Participante(nome='Rafaela Teixeira', idade=20, vinculo='estudante', matricula='20285432', matriculado=True),
    Participante(nome='Samuel Cardoso', idade=21, vinculo='estudante', matricula='20286895', matriculado=True),
    Participante(nome='Tatiana Freire', idade=19, vinculo='estudante', matricula='20288317', matriculado=True),
    Participante(nome='Vinicius Melo', idade=26, vinculo='comunidade', matricula='20273876', matriculado=True),
]

PARTICIPANTS_EVENT_2 = [
    Participante(nome='Adriana Ramos', idade=20, vinculo='estudante', matricula='20301021', matriculado=True),
    Participante(nome='Andre Carvalho', idade=22, vinculo='estudante', matricula='20302486', matriculado=True),
    Participante(nome='Bianca Moreira', idade=19, vinculo='estudante', matricula='20303947', matriculado=True),
    Participante(nome='Caio Farias', idade=23, vinculo='comunidade', matricula=None, matriculado=True),
    Participante(nome='Daniela Lopes', idade=20, vinculo='estudante', matricula='20306795', matriculado=True),
    Participante(nome='Eduardo Rezende', idade=21, vinculo='estudante', matricula='20308136', matriculado=True),
    Participante(nome='Fernanda Brito', idade=19, vinculo='estudante', matricula='20309608', matriculado=True),
    Participante(nome='Gustavo Neves', idade=24, vinculo='comunidade', matricula=None, matriculado=True),
    Participante(nome='Helena Castro', idade=20, vinculo='estudante', matricula='20312549', matriculado=True),
    Participante(nome='Igor Duarte', idade=22, vinculo='estudante', matricula='20313982', matriculado=True),
    Participante(nome='Juliana Paiva', idade=19, vinculo='estudante', matricula='20315460', matriculado=True),
    Participante(nome='Kleber Viana', idade=25, vinculo='comunidade', matricula=None, matriculado=True),
    Participante(nome='Larissa Cunha', idade=20, vinculo='estudante', matricula='20318314', matriculado=True),
    Participante(nome='Matheus Tavares', idade=21, vinculo='estudante', matricula='20319768', matriculado=True),
    Participante(nome='Natalia Gomes', idade=19, vinculo='estudante', matricula='20321243', matriculado=True),
    Participante(nome='Otavio Pires', idade=27, vinculo='comunidade', matricula=None, matriculado=True),
    Participante(nome='Patricia Mota', idade=20, vinculo='estudante', matricula='20324158', matriculado=True),
    Participante(nome='Renato Sales', idade=22, vinculo='estudante', matricula='20325506', matriculado=True),
    Participante(nome='Sofia Nunes', idade=19, vinculo='estudante', matricula='20327083', matriculado=True),
    Participante(nome='Tiago Lemos', idade=28, vinculo='comunidade', matricula=None, matriculado=True),
]


# ------------------------------------------------------------------------------
# 3. BASE OFICIAL DE CADASTROS DA INSTITUIÇÃO (SUPORTE AO PARADIGMA LÓGICO)
# ------------------------------------------------------------------------------
BASE_PESSOAS = {}

# Mapeia os alunos com matrícula da lista inicial
for p in PARTICIPANTS_EVENT_1 + PARTICIPANTS_EVENT_2:
    if p.matricula:
        BASE_PESSOAS[p.matricula.strip()] = p

# Adiciona os 6 casos de teste específicos (Professores, Alunos Ativos e Inativos):
# 2 Professores (Ativos)
BASE_PESSOAS["90001001"] = Participante(nome="Prof. Roberto Santos", idade=45, vinculo="professor", matricula="90001001", matriculado=True)
BASE_PESSOAS["90001002"] = Participante(nome="Profª. Helena Lima", idade=38, vinculo="professor", matricula="90001002", matriculado=True)

# 2 Alunos Matriculados (Ativos)
BASE_PESSOAS["10002001"] = Participante(nome="Gabriel Mendonça", idade=20, vinculo="estudante", matricula="10002001", matriculado=True)
BASE_PESSOAS["10002002"] = Participante(nome="Beatriz Cavalcante", idade=21, vinculo="estudante", matricula="10002002", matriculado=True)

# 2 Alunos NÃO Matriculados (Inativos / Trancados)
BASE_PESSOAS["10003001"] = Participante(nome="Lucas Andrade", idade=22, vinculo="estudante", matricula="10003001", matriculado=False)
BASE_PESSOAS["10003002"] = Participante(nome="Juliana Alencar", idade=19, vinculo="estudante", matricula="10003002", matriculado=False)


# ------------------------------------------------------------------------------
# 4. MAPEAMENTO E SINCRONIZAÇÃO DE INSCRIÇÕES
# ------------------------------------------------------------------------------
MAP_EVENT_PARTICIPANT = {
    EVENTS[0].id: PARTICIPANTS_EVENT_1,
    EVENTS[1].id: PARTICIPANTS_EVENT_2
}

EVENTS[0].inscritos = PARTICIPANTS_EVENT_1
EVENTS[1].inscritos = PARTICIPANTS_EVENT_2