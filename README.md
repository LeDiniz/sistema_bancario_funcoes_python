# 💰 Sistema bancário simples em python

Este é um projeto de terminal que simula um sistema bancário básico, aprimorado com funcionalidades adicionais. O usuário pode realizar depósitos, saques, consultar extrato, cadastrar novos usuários, criar novas contas e listar as contas existentes.

## 📋 Funcionalidades

- **Depósito:** permite adicionar valores ao saldo da conta.
- **Saque:** permite retirar valores da conta, respeitando:
  - Um **limite por saque** (R$500.00).
  - Um **limite diário de saques** (3 por dia).
  - A condição de saldo suficiente.
- **Extrato:** exibe todas as movimentações realizadas (depósitos e saques) e o saldo atual.
- **Novo usuário** : permite cadastrar um novo usuário no sistema.
- **Nova conta** : permite criar uma nova conta bancária vinculada a um usuário existente.
- **Listar contas** : exibe todas as contas cadastradas, com informações sobre o titular, agência e número da conta.
- **Sair** : finaliza a aplicação.

## 🚀 Como usar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone o repositório ou copie o código.
3. Execute o script:

```bash
python banco.py
```

4. Use o menu interativo para navegar pelas opções:

```
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Nova conta
[lc] Listar contas
[q] Sair
```

## 🧠 Exemplo de uso
### 1. Crie um novo usuário:

```text
=> u  
Digite seu CPF (somente números): 12345678901  
Digite o seu nome: João Silva  
Digite a sua data de nascimento (dd-mm-aaaa): 15-05-1985  
Digite o seu endereço (endereço, número - bairro - cidade/sigla do estado): Rua A, 123 - Centro - São Paulo/SP  
Usuário cadastrado com sucesso.
```

###2. Crie uma nova conta para o usuário:

```text
=> c  
Digite seu CPF (somente números): 12345678901  
Conta criada com sucesso!
```

###3. Listar as contas cadastradas:

```
=> lc  
-------------------- Contas --------------------  

Titular:João Silva     |  Agência:0001  |  Número da conta:1
```

###4. Realizar um depósito:

```text
=> d  
Digite o valor do depósito: 200  
Depósito realizado com sucesso!
```

###5. Realizar um saque:

```text
=> s  
Digite o valor do saque: 100  
Saque realizado com sucesso!
```

###6. Consulte o extrato:

```text
=> e  
------------EXTRATO------------  
DEPÓSITO - R$200.00  
SAQUE - R$100.00  
SALDO - R$100.00  
-------------------------------
```

## 📌 Regras de negócio

- Não é permitido realizar saques que excedam o saldo disponível.
- Não é permitido sacar mais do que R$500.00 por operação.
- O número de saques é limitado a 3 por execução.
- Depósitos com valor inválido (zero ou negativo) não são permitidos.
- Para criar uma conta, é necessário um CPF válido de um usuário já cadastrado.

