"""Banco de dados simulado usado durante o desenvolvimento.

Os objetos abaixo ficam somente na memória do programa. Isso torna o projeto
simples para fins acadêmicos, mas significa que cadastros feitos pelo navegador
desaparecem quando o servidor é encerrado ou reiniciado.
"""

from models.event import Event
from models.participant import Participant


# ORIENTAÇÃO A OBJETOS:
# Cada chamada Event(...) ou Participant(...) abaixo cria um objeto a partir de
# uma classe. Os dados relacionados permanecem reunidos dentro desses objetos.

# PROGRAMAÇÃO IMPERATIVA:
# As atribuições constroem o estado inicial do banco simulado. Além disso, as
# listas e o dicionário são estruturas mutáveis que data.py altera em execução.

# PROGRAMAÇÃO FUNCIONAL:
# Não há processamento funcional de coleções neste arquivo. O aspecto funcional
# relacionado a estes dados está na imutabilidade dos objetos Participant,
# definida por ``frozen=True`` em models/participant.py.

# Eventos iniciais usados para que a aplicação já abra com conteúdo de exemplo.
# ``registered`` deve corresponder ao total existente na lista de participantes
# associada ao evento no final deste arquivo.
EVENTS = [
            Event(
                id=1, day='15', month='SET', date='15/09/2026',
                type='WORKSHOP', title='Workshop de Python',
                location='Laboratório 2', registered=20, capacity=30, description="Aprenda os fundamentos da linguagem Python e desenvolva seus primeiros programas."
            ),
            Event(
                id=2, day='20', month='SET', date='20/09/2026',
                type='PALESTRA', title='Inteligência Artificial na Atualidade',
                location='Auditório A', registered=50, capacity=60, description= "Aprenda os fundamentos de IA e aprenda a treinar modelos !"
            ),
    ]


# Participantes que começam associados ao evento de ID 1.
PARTICIPANTS_EVENT_1 = [
    Participant(name='Ana Beatriz Lima', registry=20261047, major='Sistemas de informação'),
    Participant(name='Bruno Henrique Alves', registry=20262781, major='Engenharia de Software'),
    Participant(name='Camila Rodrigues', registry=20264429, major='Ciencias da Computacao'),
    Participant(name='Diego Martins', registry=20265903, major='Outros'),
    Participant(name='Elisa Fernandes', registry=20267218, major='Sistemas de informação'),
    Participant(name='Felipe Santos', registry=20268654, major='Engenharia de Software'),
    Participant(name='Gabriela Costa', registry=20270136, major='Ciencias da Computacao'),
    Participant(name='Hugo Nascimento', registry=20271842, major='Outros'),
    Participant(name='Isabela Moura', registry=20273397, major='Sistemas de informação'),
    Participant(name='João Victor Rocha', registry=20274620, major='Engenharia de Software'),
    Participant(name='Karina Oliveira', registry=20276185, major='Ciencias da Computacao'),
    Participant(name='Lucas Pereira', registry=20277904, major='Outros'),
    Participant(name='Mariana Souza', registry=20279261, major='Sistemas de informação'),
    Participant(name='Nicolas Ribeiro', registry=20280573, major='Engenharia de Software'),
    Participant(name='Olivia Barros', registry=20282149, major='Ciencias da Computacao'),
    Participant(name='Pedro Azevedo', registry=20283706, major='Outros'),
    Participant(name='Rafaela Teixeira', registry=20285432, major='Sistemas de informação'),
    Participant(name='Samuel Cardoso', registry=20286895, major='Engenharia de Software'),
    Participant(name='Tatiana Freire', registry=20288317, major='Ciencias da Computacao'),
    Participant(name='Vinicius Melo', registry=20289964, major='Outros'),
]


# Participantes que começam associados ao evento de ID 2.
PARTICIPANTS_EVENT_2 = [
    Participant(name='Adriana Ramos', registry=20301021, major='Sistemas de informação'),
    Participant(name='Andre Carvalho', registry=20302486, major='Engenharia de Software'),
    Participant(name='Bianca Moreira', registry=20303947, major='Ciencias da Computacao'),
    Participant(name='Caio Farias', registry=20305312, major='Outros'),
    Participant(name='Daniela Lopes', registry=20306795, major='Sistemas de informação'),
    Participant(name='Eduardo Rezende', registry=20308136, major='Engenharia de Software'),
    Participant(name='Fernanda Brito', registry=20309608, major='Ciencias da Computacao'),
    Participant(name='Gustavo Neves', registry=20311074, major='Outros'),
    Participant(name='Helena Castro', registry=20312549, major='Sistemas de informação'),
    Participant(name='Igor Duarte', registry=20313982, major='Engenharia de Software'),
    Participant(name='Juliana Paiva', registry=20315460, major='Ciencias da Computacao'),
    Participant(name='Kleber Viana', registry=20316827, major='Outros'),
    Participant(name='Larissa Cunha', registry=20318314, major='Sistemas de informação'),
    Participant(name='Matheus Tavares', registry=20319768, major='Engenharia de Software'),
    Participant(name='Natalia Gomes', registry=20321243, major='Ciencias da Computacao'),
    Participant(name='Otavio Pires', registry=20322691, major='Outros'),
    Participant(name='Patricia Mota', registry=20324158, major='Sistemas de informação'),
    Participant(name='Renato Sales', registry=20325506, major='Engenharia de Software'),
    Participant(name='Sofia Nunes', registry=20327083, major='Ciencias da Computacao'),
    Participant(name='Tiago Lemos', registry=20328419, major='Outros'),
    Participant(name='Aline Peixoto', registry=20329965, major='Sistemas de informação'),
    Participant(name='Bernardo Leal', registry=20331428, major='Engenharia de Software'),
    Participant(name='Clara Aguiar', registry=20332870, major='Ciencias da Computacao'),
    Participant(name='Davi Queiroz', registry=20334356, major='Outros'),
    Participant(name='Evelyn Siqueira', registry=20335804, major='Sistemas de informação'),
    Participant(name='Fabio Motta', registry=20337269, major='Engenharia de Software'),
    Participant(name='Giovana Reis', registry=20338715, major='Ciencias da Computacao'),
    Participant(name='Heitor Melo', registry=20340192, major='Outros'),
    Participant(name='Ingrid Valente', registry=20341638, major='Sistemas de informação'),
    Participant(name='Jonas Braga', registry=20343107, major='Engenharia de Software'),
    Participant(name='Kelly Araujo', registry=20344581, major='Ciencias da Computacao'),
    Participant(name='Leandro Antunes', registry=20346024, major='Outros'),
    Participant(name='Monica Pinheiro', registry=20347496, major='Sistemas de informação'),
    Participant(name='Natan Coelho', registry=20348953, major='Engenharia de Software'),
    Participant(name='Priscila Bastos', registry=20350418, major='Ciencias da Computacao'),
    Participant(name='Rafael Xavier', registry=20351872, major='Outros'),
    Participant(name='Sara Mendonca', registry=20353340, major='Sistemas de informação'),
    Participant(name='Theo Macedo', registry=20354806, major='Engenharia de Software'),
    Participant(name='Valeria Monteiro', registry=20356289, major='Ciencias da Computacao'),
    Participant(name='Wagner Falcao', registry=20357731, major='Outros'),
    Participant(name='Yasmin Lacerda', registry=20359194, major='Sistemas de informação'),
    Participant(name='Alex Rocha', registry=20360658, major='Engenharia de Software'),
    Participant(name='Brenda Moraes', registry=20362105, major='Ciencias da Computacao'),
    Participant(name='Cesar Aquino', registry=20363579, major='Outros'),
    Participant(name='Debora Freitas', registry=20365042, major='Sistemas de informação'),
    Participant(name='Enzo Matos', registry=20366497, major='Engenharia de Software'),
    Participant(name='Flavia Barreto', registry=20367926, major='Ciencias da Computacao'),
    Participant(name='George Correia', registry=20369480, major='Outros'),
    Participant(name='Iara Fonseca', registry=20370853, major='Sistemas de informação'),
    Participant(name='Murilo Assis', registry=20372316, major='Engenharia de Software'),
]


# Este dicionário relaciona cada ID de evento à sua própria lista de inscritos.
# A estrutura permite localizar os participantes sem percorrer todas as listas.
MAP_EVENT_PARTICIPANT = {
    EVENTS[0].id : PARTICIPANTS_EVENT_1,
    EVENTS[1].id : PARTICIPANTS_EVENT_2
    }
