"""Rotas web da aplicação EventosUni.

Este módulo liga o navegador às regras do sistema. Cada função decorada com
``@app.route`` responde a um endereço da aplicação, consulta ou altera os dados
por meio do ``DataManager`` e escolhe qual página HTML será apresentada.
"""

from datetime import datetime

from flask import Flask, render_template, abort, redirect, request, url_for
from data import DataManager


app = Flask(__name__)

# ORIENTAÇÃO A OBJETOS:
# ``app`` é um objeto criado a partir da classe Flask. As rotas também usam os
# métodos estáticos da classe DataManager e trabalham com objetos Event.


@app.route('/')
def index():
    """Exibe a página inicial com todos os eventos cadastrados."""

    return render_template('index.html', events=DataManager.get_events())


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    """Mostra o formulário e processa o cadastro de um novo evento.

    Uma requisição GET apenas abre a página. Uma requisição POST acontece
    quando o formulário é enviado e traz os valores digitados pelo usuário.
    """

    # PROGRAMAÇÃO IMPERATIVA:
    # A rota segue uma sequência de ações: lê os campos, converte valores,
    # verifica condições, altera os dados e decide qual resposta devolver.
    if request.method == 'POST':
        # ``get`` evita erro caso um campo não venha no formulário. ``strip``
        # remove espaços extras no início e no fim dos textos digitados.
        title = request.form.get('nome', '').strip()
        date_value = request.form.get('data', '').strip()
        event_type = request.form.get('tipo', '').strip()
        location = request.form.get('local', '').strip()
        capacity_value = request.form.get('vagas', '').strip()
        description = request.form.get('descricao', '').strip()

        # O navegador envia a data como AAAA-MM-DD e os números como texto.
        # A conversão confirma que esses dois campos possuem formatos válidos.
        try:
            event_date = datetime.strptime(date_value, '%Y-%m-%d')
            capacity = int(capacity_value)
        except ValueError:
            # O código HTTP 400 informa que os dados enviados são inválidos.
            return render_template('cadastro_evento.html'), 400

        # Além do formato, os campos obrigatórios precisam estar preenchidos e
        # a capacidade deve permitir pelo menos uma inscrição.
        if not title or not event_type or not location or not description or capacity < 1:
            return render_template('cadastro_evento.html'), 400

        # As abreviações em português são usadas nos cartões da página inicial.
        # PROGRAMAÇÃO FUNCIONAL:
        # A tupla é imutável e as chamadas strip, upper e strftime transformam
        # valores em novos valores sem modificar os textos originais. A rota
        # inteira, porém, não é pura, pois lê a requisição e cadastra um evento.
        months = ('JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                  'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ')

        # O DataManager centraliza a alteração do banco de dados simulado.
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

        # Após cadastrar, o navegador é enviado para os detalhes do novo evento.
        return redirect(url_for('evento', event_id=event.id))

    # Se a requisição não for POST, basta abrir o formulário vazio.
    return render_template('cadastro_evento.html')


@app.route('/evento/<int:event_id>', methods=['GET'])
def evento(event_id):
    """Exibe os detalhes de um evento e sua lista de participantes."""

    # IMPERATIVA + ORIENTAÇÃO A OBJETOS:
    # As chamadas acontecem em ordem e pedem que a classe DataManager consulte
    # os objetos necessários antes que a página possa ser montada.
    event = DataManager.get_event_by_id(event_id)
    participants = DataManager.get_participants_of_event(event_id)

    # Interrompe com "não encontrado" quando não existe evento com esse ID.
    if event is None:
        abort(404)

    return render_template('evento.html', event=event, participants=participants)


@app.route('/inscricao/<int:event_id>', methods=['GET', 'POST'])
def inscricao(event_id):
    """Mostra o formulário e registra um participante no evento escolhido."""

    event = DataManager.get_event_by_id(event_id)
    if event is None:
        abort(404)

    # PROGRAMAÇÃO IMPERATIVA:
    # O if controla o caminho executado, e add_participant produz uma alteração
    # no banco simulado quando os dados são válidos e existe vaga.
    if request.method == 'POST':
        # Coleta e limpa os três campos recebidos do formulário de inscrição.
        name = request.form.get('nome', '').strip()
        registry = request.form.get('matricula', '').strip()
        major = request.form.get('curso', '').strip()

        # A matrícula só é aceita quando contém exclusivamente números.
        if not name or not registry.isdigit() or not major:
            return render_template('inscricao.html', event=event), 400

        # O método também pode recusar a inscrição quando não há mais vagas.
        if not DataManager.add_participant(event_id, name, int(registry), major):
            # O código 409 indica conflito entre o pedido e o estado do evento.
            return render_template('inscricao.html', event=event), 409

        # Reabrir a página do evento permite ver o participante recém-inserido.
        return redirect(url_for('evento', event_id=event_id))

    return render_template('inscricao.html', event=event)


if __name__ == '__main__':
    # Este bloco só roda quando o arquivo é iniciado diretamente. O modo debug
    # reinicia o servidor após alterações e mostra erros durante o desenvolvimento.
    app.run(debug=True)
