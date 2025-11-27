# Gerenciador de Tarefas — Projeto Django

Este é um Gerenciador de Tarefas desenvolvido em Python + Django, criado para organizar atividades do dia a dia de forma simples, eficiente e escalável.
O projeto utiliza boas práticas de desenvolvimento, ambiente virtual e arquitetura limpa.

Tecnologias Utilizadas

Python 3.10+

Django 4+

Virtualenv

SQLite (padrão, mas pode ser alterado)

HTML / CSS / Bootstrap (ou conforme o projeto)

Git e GitHub

Como Instalar e Rodar o Projeto

Siga o passo a passo abaixo para rodar o projeto localmente.

1. Clonar o repositório
git clone https://github.com/gabrielslsz/gerenciadordetarefas.git
cd seu-repositorio

2. Criar o ambiente virtual (virtualenv)

Se ainda não tiver o virtualenv instalado:

pip install virtualenv


Criar o ambiente:

virtualenv venv

3. Ativar o ambiente virtual
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

4. Instalar as dependências
pip install -r requirements.txt


Se ainda não tiver o arquivo requirements.txt, pode gerar com:

pip freeze > requirements.txt

5. Configurar o Django
Criar as migrações:
python manage.py makemigrations

Aplicar as migrações:
python manage.py migrate

6. Criar um superusuário (opcional)
python manage.py createsuperuser

7. Rodar o servidor
python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000/

Estrutura do Projeto (exemplo)
meu_projeto/
│── manage.py
│── requirements.txt
│── README.md
│── app_tarefas/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│── meu_projeto/
    ├── settings.py
    ├── urls.py
    └── wsgi.py

Funcionalidades

Criar tarefas

Editar tarefas

Marcar como concluída

Excluir tarefas

Interface simples e objetiva

Autenticação (se implementada)

Contribuições

Sinta-se à vontade para contribuir, sugerir melhorias ou enviar pull requests.

Licença

Este projeto está sob a licença MIT.