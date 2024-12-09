# Documentação.

1- 
  As dependências do Flask e marshmallow
  
2- 
  '/aluno' - Na aplicação, esse endpoint será utilizado para cadastrar um aluno utilizando o request.json que receberá a requisição. Logo será atribuido a variável request_data para a manipulação.
  
  '/relatorio' - Na aplicação, esse endpoint será utilizado para cadastrar um relatório o request.json que receberá a requisição. Logo será atribuido a variável request_data para a manipulação.
  
3-
  Os dados são persistidos em listas (alunos e relatorios). Uma forma mais eficiente para se utilizar na aplicação é a utilização de um banco de dados (SQLite3, MySQL, PostgreSQL, etc.).

4-
  Na aplicação, o marshmallow é utilizado nas seguintes classes:
  
  class AlunoSchema(Schema):
  idade = fields.Integer(required=True) #Nessa parte, o método fields do marshmallow declara que o tipo do dado deve ser Integer e obrigatório
      
  disciplina = fields.String(required=True) #Nessa parte, o método fields do marshmallow declara que o tipo do dado deve ser String e obrigatório
  
  class RelatorioSchema(Schema):
  
  titulo = fields.Str()  #Nessa parte, o método fields do marshmallow declara que o tipo do dado deve ser String e obrigatório
  
  criacao = fields.Date()  #Nessa parte, o método fields do marshmallow declara que o tipo do dado deve ser Date e obrigatório
  
  aluno = fields.Nested(AlunoSchema()) #Nessa parte, é criado um relacionamento com AlunosSchema
  
  Ela também é utlizada no tratamento de exceções com "ValidationError"

  Com isso, nos endpoints para cadastramento de alunos e relatórios, os dados serão analisados e, caso não aja erros, serão persistidos, caso contrário, a exceção do marshmallow "ValidationError" será lançada.

5-
  O JSON em "alunos" tem os campos de "idade" e "disciplina", isso é visto na classe AlunoSchema(Schema), onde os atributos são esses respectivamente. No endpoint "/aluno", onde será persistido, essa classe é atribuída a variável schema, que logo em seguida carregará o JSON adicionado e contido em "request_data".

  O JSON em "relatorio" tem os campos de "titulo", "criacao" e "alunos (aluno sendo referenciado pela classe AlunoSchema) isso é visto na classe RelatorioSchema(Schema), onde os atributos são esses respectivamente. No endpoint "/relatorio", onde será persistido, essa classe é atribuída a variável schema, que logo em seguida carregará o JSON adicionado e contido em "request_data".
