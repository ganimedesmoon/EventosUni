"""
Aplicação Principal EventosUni (Rotas Flask)
--------------------------------------------
Este módulo atua como o controlador principal da aplicação web.
Integra as requisições HTTP às regras de negócio, manipulando os dados através
do DataManager e aplicando as validações dos diferentes paradigmas.

Paradigmas integrados:
- OO: Flask, instâncias de Event e Participante.
- Lógico: Invocação de 'possui_matricula_valida_e_ativa' e 'eh_elegivel'.
- Funcional: Invocação de 'gerar_relatorio_geral_funcional'.
- Imperativo: Controle de fluxo das rotas e requisições HTTP.
"""

from datetime import datetime
from flask import Flask, render_template, abort, redirect, request, url_for

from data import DataManager
from models.participant import Participante
from rules import eh_elegivel
from reports import gerar_relatorio_geral_funcional


app = Flask(__name__)


# ------------------------------------------------------------------------------
# ROTA 1: PÁGINA INICIAL (INDEX)
# ------------------------------------------------------------------------------
@app.route('/')
def index():
    """Exibe a lista de eventos cadastrados no sistema."""
    return render_template('index.html', events=DataManager.get_events())


# ------------------------------------------------------------------------------
# ROTA 2: CADASTRO DE EVENTOS
# ------------------------------------------------------------------------------
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    """
    Mostra o formulário (GET) e processa a criação de um novo evento (POST).
    """
    if request.method == 'POST':
        title = request.form.get('nome', '').strip()
        date_value = request.form.get('data', '').strip()
        event_type = request.form.get('tipo', '').strip()
        location = request.form.get('local', '').strip()
        capacity_value = request.form.get('vagas', '').strip()
        description = request.form.get('descricao', '').strip()

        try:
            event_date = datetime.strptime(date_value, '%Y-%m-%d')
            capacity = int(capacity_value)
        except ValueError:
            return render_template('cadastro_evento.html', error="Data ou número de vagas inválido."), 400

        if not title or not event_type or not location or not description or capacity < 1:
            return render_template('cadastro_evento.html', error="Preencha todos os campos obrigatórios."), 400

        # Mapeamento imutável dos meses (Paradigma Funcional)
        months = ('JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                  'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ')

        event = DataManager.add_event(
            day=event_date.strftime('%d'),
            month=months[event_date.month - 1],
            date=event_date.strftime('%d/%m/%Y'),
            event_type=event_type.upper(),
            title=title,
            location=location,
            capacity=capacity,
            description=description,
        )

        return redirect(url_for('evento', event_id=event.id))

    return render_template('cadastro_evento.html')


# ------------------------------------------------------------------------------
# ROTA 3: DETALHES DO EVENTO
# ------------------------------------------------------------------------------
@app.route('/evento/<int:event_id>', methods=['GET'])
def evento(event_id):
    """Exibe as informações do evento e os seus participantes inscritos."""
    event = DataManager.get_event_by_id(event_id)
    participants = DataManager.get_participants_of_event(event_id)

    if event is None:
        abort(404)

    return render_template('evento.html', event=event, participants=participants)


# ------------------------------------------------------------------------------
# ROTA 4: INSCRIÇÃO DE PARTICIPANTE
# ------------------------------------------------------------------------------
@app.route('/inscricao/<int:event_id>', methods=['GET', 'POST'])
def inscricao(event_id):
    """
    Mostra o formulário de inscrição (GET) e processa a validação e cadastro (POST).
    Aplica as regras do Paradigma Lógico para validar a matrícula e verificar elegibilidade.
    """
    event = DataManager.get_event_by_id(event_id)
    if event is None:
        abort(404)

    if request.method == 'POST':
        name = request.form.get('nome', '').strip()
        vinculo = request.form.get('vinculo', '').strip().lower()
        idade_value = request.form.get('idade', '').strip()
        registry = request.form.get('matricula', '').strip()
        curso = request.form.get('curso', '').strip()

        # Campos sempre obrigatórios: nome, vínculo e idade.
        # A matrícula só é obrigatória para estudantes e professores;
        # a comunidade externa se inscreve sem ela (Regra Lógica 2).
        if not name or not vinculo or not idade_value:
            return render_template('inscricao.html', event=event, error="Preencha todos os campos obrigatórios."), 400

        if vinculo in ("estudante", "professor") and not registry:
            return render_template('inscricao.html', event=event, error="Informe a matrícula para se inscrever como estudante ou professor."), 400

        try:
            idade = int(idade_value)
        except ValueError:
            return render_template('inscricao.html', event=event, error="Informe uma idade válida."), 400

        # Instanciação do objeto Participante (Orientação a Objetos)
        # Observação: o model Participante não possui campo de curso — o
        # vínculo (estudante/professor/comunidade) é o que alimenta as regras
        # lógicas de elegibilidade; "curso" é apenas informativo no formulário.
        participante = Participante(
            nome=name,
            idade=idade,
            vinculo=vinculo,
            matricula=registry or None,
        )

        # PARADIGMA LÓGICO: Elegibilidade combina idade mínima com a regra do
        # vínculo (matrícula ativa para estudante/professor, ou comunidade sem matrícula).
        if not eh_elegivel(participante):
            if vinculo == "comunidade":
                mensagem_erro = "Inscrição não permitida: idade mínima de 18 anos não atendida."
            else:
                mensagem_erro = "Matrícula inválida ou inativa na base da instituição."
            return render_template('inscricao.html', event=event, error=mensagem_erro), 400

        # PARADIGMA IMPERATIVO: Adição do participante com controlo de lotação
        sucesso = DataManager.add_participant(event_id=event_id, participant=participante)

        if not sucesso:
            return render_template('inscricao.html', event=event, error="Inscrição não realizada: as vagas para este evento já se esgotaram."), 409

        return redirect(url_for('evento', event_id=event_id))

    return render_template('inscricao.html', event=event)


# ------------------------------------------------------------------------------
# ROTA 5: RELATÓRIOS ANALÍTICOS
# ------------------------------------------------------------------------------
@app.route('/relatorios', methods=['GET'])
def relatorios():
    """
    PARADIGMA FUNCIONAL:
    Gera o relatório de ocupação dos eventos usando transformações puras (map/filter).
    """
    eventos = DataManager.get_events()
    relatorio = gerar_relatorio_geral_funcional(eventos)
    return render_template('relatorios.html', relatorio=relatorio)


if __name__ == '__main__':
    app.run(debug=True)