Feature: Buscar usuário pela API

  Scenario: Buscar um usuário existente
    Given que tenho o endpoint de usuários
    When eu faço uma requisição pelo ID 1
    Then o retorno deve conter o nome "Leanne Graham"
