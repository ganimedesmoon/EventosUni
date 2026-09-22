"""
Módulo de Regras de Elegibilidade - Paradigma Lógico (PL)
-------------------------------------------------------
Implementa validações declarativas baseadas em predicados e regras de inferência 
para verificar a elegibilidade de participantes, requisitos de idade e 
situação cadastral na base oficial da instituição.
"""

from models.participant import Participante
from mock_db import BASE_PESSOAS


# ------------------------------------------------------------------------------
# PREDICADOS LÓGICOS DE CONSULTA E VALIDAÇÃO DE MATRÍCULA
# ------------------------------------------------------------------------------

def buscar_cadastro_por_matricula(matricula: str):
    """
    PREDICADO LÓGICO DE CONSULTA:
    Consulta se a matrícula existe na base de dados oficial da instituição.
    """
    if not matricula:
        return None
    return BASE_PESSOAS.get(str(matricula).strip())


def possui_matricula_valida_e_ativa(participante: Participante) -> bool:
    """
    PREDICADO LÓGICO DE VALIDAÇÃO:
    Avalia a conjunção lógica (AND) de duas condições:
    1. A matrícula informada deve constar na base oficial.
    2. A situação cadastral do participante deve ser ATIVA (matriculado == True).
    """
    if not participante.matricula:
        return False

    cadastro_oficial = buscar_cadastro_por_matricula(participante.matricula)
    
    # Se não existe cadastro oficial associado à matrícula, a verificação falha
    if cadastro_oficial is None:
        return False

    # Valida se a matrícula está ativa no sistema
    return cadastro_oficial.matriculado is True


def atende_requisito_idade(participante: Participante, idade_minima: int = 18) -> bool:
    """
    PREDICADO LÓGICO DE IDADE:
    Avalia se a idade do participante atende à restrição mínima do evento.
    """
    return participante.idade >= idade_minima


# ------------------------------------------------------------------------------
# REGRAS LÓGICAS DE ELEGIBILIDADE POR PAPEL (REGRAS DE DEDUÇÃO)
# ------------------------------------------------------------------------------

def regra_estudante_ou_professor_matriculado(participante: Participante) -> bool:
    """
    REGRA LÓGICA 1:
    Para membros vinculados (estudantes ou professores), exige que a matrícula
    seja válida e esteja com o status ativo.
    """
    if participante.vinculo in ["estudante", "professor"] or participante.matricula:
        return possui_matricula_valida_e_ativa(participante)
    return False


def regra_comunidade(participante: Participante) -> bool:
    """
    REGRA LÓGICA 2:
    Para a comunidade externa sem matrícula, a elegibilidade depende exclusivamente
    de atender à regra de idade mínima.
    """
    return participante.vinculo == "comunidade" and not participante.matricula


# ------------------------------------------------------------------------------
# PREDICADO PRINCIPAL DE ELEGIBILIDADE (DISJUNÇÃO E CONJUNÇÃO LÓGICA)
# ------------------------------------------------------------------------------

def eh_elegivel(participante: Participante, idade_minima: int = 18) -> bool:
    """
    PREDICADO LÓGICO PRINCIPAL:
    Combina regras lógicas por Conjunção (AND) e Disjunção (OR):
    - Conjunção: Precisa satisfazer a idade mínima AND
    - Disjunção: Satisfazer ao menos uma das regras de elegibilidade por vínculo.
    """
    # Conjunção Lógica: Verificação de idade mínima
    if not atende_requisito_idade(participante, idade_minima):
        return False

    # Disjunção Lógica (OR): Aplicação da lista de regras declarativas
    regras = [
        regra_estudante_ou_professor_matriculado,
        regra_comunidade
    ]

    return any(regra(participante) for regra in regras)