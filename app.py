from json import dumps, loads
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

alunos = []
relatorios = []


class AlunoSchema(Schema):
    idade = fields.Integer(required=True)
    disciplina = fields.String(required=True)


class RelatorioSchema(Schema):
    titulo = fields.Str()
    criacao = fields.Date()
    aluno = fields.Nested(AlunoSchema())


def cadastrarAluno(json_str: str):
    aluno = loads(json_str)
    alunos.append(aluno)
    return aluno


def cadastrarRelatorio(json_str: str):
    relatorio = loads(json_str)
    relatorios.append(relatorio)
    return relatorio


app = Flask(__name__)


@app.post('/aluno')
def aluno_post():

    request_data = request.json

    schema = AlunoSchema()
    try:
        result = schema.load(request_data)

        data_now_json_str = dumps(result)

        response_data = cadastrarAluno(data_now_json_str)

    except ValidationError as err:
        return jsonify(err.messages), 400

    return jsonify(response_data), 200


@app.post('/relatorio')
def relatorio_post():

    request_data = request.json

    schema = RelatorioSchema()
    try:
        result = schema.load(request_data)

        data_now_json_str = dumps(result)

        response_data = cadastrarRelatorio(data_now_json_str)

    except ValidationError as err:
        return jsonify(err.messages), 400

    return jsonify(response_data), 200
