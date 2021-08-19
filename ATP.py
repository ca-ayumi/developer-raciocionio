
def obter_limite():

    print ("Seja bem vindo à nossa loja virtual Peça+, a loja especializada em peças automotivas. Aqui quem fala é a Camila Ayumi Penteado.  " )
    print ("Antes de começar às compras, farei uma análise de crédito para que você possa comprar sem nenhuma preocupação.")
    cargo = input ("Para iniciar, preciso que você informe o seu cargo na empresa em que trabalha atualmente: ")
    salario = int (input ("Agora informe o seu salário sem contabilizar os centavos: R$"))
    ano_nascimento = int(input ("E por fim, seu ano de nascimento com os 4 dígitos: "))

    print ("Validando o cargo: %s, o salário: R$%s, e o ano de nascimento: %s"%(cargo, salario , ano_nascimento))

    ano_atual = 2021
    idade =  (ano_atual - ano_nascimento)
    idade = int(idade)

    print ('A análise de crédito é baseada na sua idade que é aproximada em ' + str(idade) + ' anos.')

    limite_gasto = ((salario*((idade)/1000))+100)
    print('De acordo com a sua idade, o seu limite de gasto na loja Peca+ R$' + str(limite_gasto) + '.')

    return limite_gasto, idade

def verificar_produto(limite):

    nome_produto = input('Por favor, informe o nome do produto desejado: ')
    preco_produto = float (input ('Agora informe o preço do produto desejado: R$'))

    primeiro_nome = 6
    nome_completo = 21

    if preco_produto <= (0.6*limite):
        print('Liberado!')

    elif (preco_produto > (0.6*limite)) and (preco_produto <= (0.9*limite)):
        print('Liberado ao parcelar em até 2 vezes')

    elif (preco_produto > (0.9*limite)) and (preco_produto <= (limite)):
        print('“Liberado ao parcelar em 3 ou mais vezes”')

    else:
        print('Bloqueado')

    if ((preco_produto <= nome_completo) and (preco_produto >= idade)) or ((preco_produto >= nome_completo) and (preco_produto <= idade)):
        print('Você terá um desconto de R$',primeiro_nome,)
        print('O valor do produto com desconto é: R$',(preco_produto - primeiro_nome),)
        limite-=(preco_produto-primeiro_nome)

    else:
        print('Não há desconto')
        limite-=preco_produto
    return (limite)

limite,idade = obter_limite()
quantidade_produtos = int(input('Quantos produtos você deseja cadastrar? '))

i=1
while i<= quantidade_produtos:
    limite = verificar_produto(limite)
    print('Seu limite atualizado é de: R$',limite,)
    i+=1


