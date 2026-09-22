"""
Módulo do Participante (Model) - Paradigma Orientado a Objetos (OO)
------------------------------------------------------------------
Representa a pessoa inscrita em um evento acadêmico.
- OO: Estrutura base de dados com métodos e propriedades para encapsulamento.
- Imutabilidade (Funcional): O parâmetro frozen=True garante imutabilidade
  dos dados cadastrais após a instância ser criada.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Participante:
    """
    PARADIGMA ORIENTADO A OBJETOS:
    Classe imutável que representa um participante no sistema.
    """
    nome: str
    idade: int
    vinculo: str               # "estudante", "professor" ou "comunidade"
    matricula: str = None      # Matrícula institucional (ex: "10002001")
    matriculado: bool = True   # Status do vínculo: True (Ativo) ou False (Inativo/Trancado)

    def __post_init__(self):
        """Padroniza o vínculo para minúsculas sem violar a imutabilidade do frozen dataclass."""
        if self.vinculo:
            object.__setattr__(self, "vinculo", self.vinculo.lower().strip())

    # --------------------------------------------------------------------------
    # PROPRIEDADES DE ENCAPSULAMENTO / COMPATIBILIDADE COM OS TEMPLATES HTML
    # --------------------------------------------------------------------------
    @property
    def name(self) -> str:
        """Retorna o nome completo para renderização no template evento.html."""
        return self.nome

    @property
    def registry(self) -> str:
        """Retorna a matrícula formatada para o template evento.html."""
        return self.matricula if self.matricula else "Sem Matrícula"

    @property
    def major(self) -> str:
        """Retorna o curso/vínculo formatado com a primeira letra maiúscula."""
        return self.vinculo.capitalize() if self.vinculo else "Geral"

    def __repr__(self) -> str:
        return f"Participante({self.nome}, vinculo='{self.vinculo}', matricula='{self.matricula}')"