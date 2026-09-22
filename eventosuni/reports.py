"""
Módulo de Relatórios e Análises - Paradigma Funcional (PF)
---------------------------------------------------------
Aplica o paradigma funcional para processar, filtrar e agregar dados de eventos
e participantes sem alterar o estado original dos objetos (Imutabilidade).

Utiliza funções de alta ordem (map, filter), expressões lambda e transformações puras.
"""

from typing import List, Dict, Any
from models.event import Event


# ------------------------------------------------------------------------------
# FUNÇÕES PURAS E TRANSFORMAÇÕES FUNCIONAIS
# ------------------------------------------------------------------------------

def calcular_taxa_ocupacao(event: Event) -> float:
    """
    FUNÇÃO PURA:
    Calcula o percentual de ocupação de um evento sem alterar seus atributos.
    Fórmula: (Inscritos / Capacidade Total) * 100
    """
    if not event or event.capacity <= 0:
        return 0.0
    taxa = (len(event.inscritos) / event.capacity) * 100
    return round(taxa, 2)


def mapear_evento_para_resumo(event: Event) -> Dict[str, Any]:
    """
    FUNÇÃO PURA (TRANSFORMAÇÃO DE DADOS):
    Recebe um objeto Event e constrói um novo dicionário com os dados consolidados.
    Garante imutabilidade, pois gera uma nova estrutura sem modificar o objeto original.
    """
    taxa = calcular_taxa_ocupacao(event)
    status = "Lotado" if taxa >= 100.0 else ("Alta Procura" if taxa >= 70.0 else "Vagas Disponíveis")

    return {
        "id": event.id,
        "titulo": event.title,
        "tipo": event.event_type,
        "data": event.date,
        "capacidade": event.capacity,
        "inscritos": len(event.inscritos),
        "vagas_restantes": max(0, event.capacity - len(event.inscritos)),
        "taxa_ocupacao": taxa,
        "status": status
    }


# ------------------------------------------------------------------------------
# FUNÇÃO PRINCIPAL DE GERAÇÃO DE RELATÓRIO (PARADIGMA FUNCIONAL)
# ------------------------------------------------------------------------------

def gerar_relatorio_geral_funcional(eventos: List[Event]) -> Dict[str, Any]:
    """
    PARADIGMA FUNCIONAL:
    Mapeia e sintetiza a coleção de eventos aplicando transformações funcionais.

    Conceitos aplicados:
    - `map`: Transforma a lista de objetos Event em uma lista de dicionários de resumo.
    - `filter`: Isola subconjuntos específicos (ex: eventos lotados).
    - Expressões `lambda`: Definem transformações pontuais e puras.
    - Funções puras de agregação: `sum` e `len` para métricas consolidadas.
    """
    if not eventos:
        return {
            "resumos": [],
            "total_eventos": 0,
            "total_vagas": 0,
            "total_inscritos": 0,
            "media_ocupacao": 0.0,
            "eventos_lotados": 0
        }

    # 1. MAP: Transforma cada objeto Event em um dicionário estruturado (Imutabilidade)
    resumos = list(map(mapear_evento_para_resumo, eventos))

    # 2. FILTER: Filtra eventos com 100% ou mais de ocupação usando expressão lambda
    lotados = list(filter(lambda r: r["taxa_ocupacao"] >= 100.0, resumos))

    # 3. AGREGAÇÃO FUNCIONAL: Métricas puras a partir dos resumos gerados
    total_vagas = sum(map(lambda r: r["capacidade"], resumos))
    total_inscritos = sum(map(lambda r: r["inscritos"], resumos))
    media_ocupacao = round(sum(map(lambda r: r["taxa_ocupacao"], resumos)) / len(resumos), 2)

    return {
        "resumos": resumos,
        "total_eventos": len(eventos),
        "total_vagas": total_vagas,
        "total_inscritos": total_inscritos,
        "media_ocupacao": media_ocupacao,
        "eventos_lotados": len(lotados)
    }