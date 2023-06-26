## ProgMod-Trab1
Trabalho de programação modular - Grupo 8

# Aplicação Locadora

São lojas que permitem ao interessado alugar um jogo de tabuleiro durante o período de
uma semana, bem como reservar durante o período de um dia para jogar com os amigos
na própria loja.
A aplicação a ser desenvolvida consiste em um controle básico deste aluguel sendo
necessários os seguintes procedimentos:
• Manter cadastro das pessoas que alugam os jogos;
• Manter o controle de aluguel de jogos com base na disponibilidade da loja;
• Cada loja tem dois jogos de cada. Porém, se houver uma procura maior, a loja
deverá comprar dos fornecedores a quantidade necessária para atender a
demanda;
• Se uma pessoa quiser alugar um jogo e todos já tiverem sido alugados, a aplicação
informará que não tem o jogo disponível. Se três pessoas solicitarem o mesmo
jogo, a aplicação dispara para o fornecedor uma solicitação de compra e se o
fornecedor informar que o jogo não existe em seu cadastro, ela dispara uma
preferência deste novo jogo para que o fornecedor possa comprar. Este jogo
somente estará disponível para ser vendido para a loja na solicitação da próxima
pessoa que deseja alugá-lo. Aí, sim, já estará no estoque do fornecedor e a loja
comprará e disponibilizará para este usuário, caso tenha dinheiro suficiente para
realizar esta compra. Se não tiver, a aplicação continua informando que não há o
jogo disponível e somente libera quando o jogo for novamente requisitado e a loja
puder comprá-lo;
• Controlar o dinheiro recebido do aluguel e utilizado para a compra de novos jogos.
A transação é simples e puramente matemática, ou seja, recebe $3 em cada um
dos três alugueis, tem então $9. Com isso pode comprar um jogo de $9 mas não
um jogo de $11.
