# Projeto 1 POO
# TEMA 8 – SISTEMA DE RESERVAS DE HOTEL

# Integrantes 
GUSTAVO DE SOUZA LOBO - 2025013399 - Modelagem das Classes (POO)
EMANUEL GONÇALVES DOS SANTOS - 2023011930 - Gerenciamento do Hotel (Regras de Negócio)
IAGO RONAN ALMINO OLIVEIRA - 2025012453 - Documentação e Qualidade
DAVI LUCAS SILVA SAMPAIO - 2025012417 - Persistência de Dados
ARTHUR FIALHO LEITE - 2025013370 - Interface de Linha de Comando (CLI)

# Principais classes do projeto (UML Textual)
Class: Quarto
Atributos: numero, tipo, capacidade, tarifa
Metodos: cadastrar, exibir, disponivel

Class: Hospede
Atributos: nome, documento, email
Metodos: cadastrar, exibir

Class: Reserva
Atributos: hospede, quarto, entrada, saida, valor
Metodos: reseva, dispnibilidade, resumo, cancelar.

