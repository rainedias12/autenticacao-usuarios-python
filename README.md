# Sistema de Autenticação e Persistência em TXT

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Este projeto consiste em um sistema funcional de simulação de banco de dados para gerenciamento e autenticação de usuários, utilizando persistência de dados em arquivos de texto simples (`.txt`).

O objetivo principal é demonstrar o domínio de conceitos fundamentais do Python voltados à manipulação de arquivos e estruturação de dados em memória.

##  Funcionalidades Cadastradas
* **Persistência Local:** Criação e leitura automatizada de arquivos de texto para salvar dados de usuários no formato `email;senha;nome;data`.
* **Validação de Login:** Lógica de criptografia lógica/comparações para validar credenciais (e-mail e senha) cadastradas.
* **Segurança de Duplicidade:** Verificação em tempo de execução para impedir o cadastro de e-mails duplicados.

##  Conceitos Python Aplicados
* **Orientação a Objetos (POO):** Estruturação do código em classes e métodos reutilizáveis.
* **Manipulação de Arquivos (I/O):** Uso de blocos `with open()` para leitura e escrita segura de dados.
* **Estruturas de Dados:** Uso de dicionários para busca rápida de informações em memória de forma eficiente.
* **Tratamento de Erros:** Estrutura `try/except` para lidar com a ausência inicial do arquivo de registros.

##  Como Rodar o Projeto
Este script roda diretamente no terminal, sem a necessidade de instalar bibliotecas externas.

1. Salve o código em um arquivo chamado `database.py`.
2. Execute o script pelo terminal:
```bash
   python database.py
