import panel as pn
import pandas as pd
import numpy as np

Nome_Do_Usuario = pn.widgets.TextInput(name='Vamos começar, qualo seu nome?')
Cidade = pn.widgets.TextInput(name='Qual a cidade do empreendimento?')
Nome_Empresa = pn.widgets.TextInput(name='E para finalizar essa etapa, qual o nome do empreendimento ou da sua empresa?')
Parcelas_Entrada  =  pn.widgets.IntInput(name="Quantas vezes parcela a entrada?",  start=1, step=1)
Entrada_A_Vista  =  pn.widgets.FloatInput(name="Qual o valor da entrada à vista?", step=0.01)
Entrada_A_Prazo_1  =  pn.widgets.FloatInput(name="Qual o valor da primeira parcela da entrada a prazo?",  step=0.01)
Entrada_A_Prazo_2  =  pn.widgets.FloatInput(name="Qual o valor da segunda parcela da entrada a prazo?", step=0.01)
Saldo_Parcelado  =  pn.widgets.FloatInput(name="Qual o saldo a ser parcelado?",step=0.01)
Parcelas  =  pn.widgets.IntInput(name="Em quantas parcelas será dividido o saldo restante?",  start=1, step=1)
Juros  =  pn.widgets.FloatInput(name="Qual é a taxa de juros anual (%)?", value=0.08, step=0.0001)
Juros_Mensal  =  pn.widgets.FloatInput(name="Qual é a taxa de juros mensal (%)?", value=0.006434, step=0.0001)
Valor_Do_Lote  =  pn.widgets.FloatInput(name="Qual o valor total do lote?", value=109227.4, step=0.01)
Valor_Parcela  =  pn.widgets.IntInput(name="Qual o tamanho (número de parcelas) do financiamento?", value=240, start=1, step=1)
Tamanho  =  pn.widgets.FloatInput(name="Qual é o tamanho médio do lote?",  step=0.01)
Percentual_empreendedor  =  pn.widgets.FloatInput(name="Qual é o percentual do empreendedor?", value=0.7, step=0.01)
Comissao_Total  =  pn.widgets.FloatInput(name="Qual o valor total da comissão (%)?", value=0.03, step=0.01)
Parcelamento_Comissao  =  pn.widgets.IntInput(name="Em quantas parcelas será dividido o pagamento da comissão?", value=3, start=1, step=1)
Imposto  =  pn.widgets.FloatInput(name="Qual o percentual de imposto (%)?", value=0.0673, step=0.0001)
Taxa_Adm  =  pn.widgets.FloatInput(name="Qual a taxa administrativa (%)?", value=0.1, step=0.01)
Meses_Para_Vender  =  pn.widgets.IntInput(name="Quantos meses são necessários para vender todos os lotes?", value=15, start=1, step=1)
Media_De_Venda  =  pn.widgets.FloatInput(name="Qual é a média de vendas por mês?", value=2, step=0.01)
Std_De_Venda  =  pn.widgets.FloatInput(name="Qual é o desvio padrão das vendas por mês?", value=5, step=0.01)
Numero_De_Lotes  =  pn.widgets.IntInput(name="Quantos lotes estão disponíveis para venda?", value=500, start=1, step=1)
Valores_Entrada  =  pn.widgets.LiteralInput(name="Quais são os valores da entrada?", value=np.array([3276.82, 1092.27, 1092.27]), type=np.ndarray)
Obra  =  pn.widgets.IntInput(name="Qual é a duração da obra em meses?", value=140, start=1, step=1)
Total_Obra  =  pn.widgets.FloatInput(name="Qual é o valor total da obra?", value=15800000, step=1000)
Obra_Pre_Lancamento  =  pn.widgets.FloatInput(name="Qual é o valor da obra no pré-lançamento?", value=1000000, step=1000)
Aprovacao  =  pn.widgets.FloatInput(name="Qual é o valor da aprovação?", value=1000000, step=1000)
Valor_pre_Lancamento  =  pn.widgets.FloatInput(name="Qual é o valor do pré-lançamento?", value=1000000 + 1000000, step=1000)
Meses_Pre_Lancamento  =  pn.widgets.IntInput(name="Quantos meses dura o pré-lançamento?", value=28, start=1, step=1)
Media_Pre_Lancamento  =  pn.widgets.FloatInput(name="Qual é a média de duração do pré-lançamento em meses?", value=26, step=0.01)
Std_Dev_Pre_Lancamento  =  pn.widgets.FloatInput(name="Qual é o desvio padrão da duração do pré-lançamento em meses?", value=15, step=0.01)
Valor_Pos_Lancamento  =  pn.widgets.FloatInput(name="Qual é o valor da obra no pós-lançamento?", value=15800000 - 1000000, step=1000)
Meses_Pos_Lancamento  =  pn.widgets.IntInput(name="Quantos meses dura o pós-lançamento?", value=20, start=1, step=1)
Media_Pos_Lancamento  =  pn.widgets.FloatInput(name="Qual é a média de duração do pós-lançamento em meses?", value=12, step=0.01)
Std_Dev_Pos_Lancamento  =  pn.widgets.FloatInput(name="Qual é o desvio padrão da duração do pós-lançamento em meses?", value=4, step=0.01)
Valores_Comissao  =  pn.widgets.LiteralInput(name="Quais são os valores da comissão?", value=np.array([1092.27, 1092.27, 1092.27]), type=np.ndarray)

# Cabeçalho com uma mensagem acolhedora
header =  pn.Column(
    pn.pane.Markdown("## Vamos começar que vai ser legal! \n### Insira os dados abaixo para continuarmos."),
    Nome_Do_Usuario ,Cidade ,Nome_Empresa )

    # pn.widgets.TextInput(name='Vamos começar, qualo seu nome?'),
    # pn.widgets.TextInput(name='Qual a cidade do empreendimento?'),
    # pn.widgets.TextInput(name='E para finalizar essa etapa, qual o nome do empreendimento ou da sua empresa?'))

# Passo 1: Entradas relacionadas a vendas e lotes
Passo2 = pn.Column(
    Parcelas_Entrada ,
    Entrada_A_Vista ,
    Entrada_A_Prazo_1 ,
    Entrada_A_Prazo_2 ,
    Saldo_Parcelado ,
    Parcelas ,
    Juros ,
    Juros_Mensal ,
    Valor_Do_Lote ,
    Valor_Parcela ,
    Tamanho ,
    Percentual_empreendedor 

)

# Passo 2: Entradas relacionadas à obra e comissões
Passo3 = pn.Column(
    pn.pane.Markdown("### Passo 2: Informações da Obra e Comissões"),
    Comissao_Total ,
    Parcelamento_Comissao ,
    Imposto ,
    Taxa_Adm ,
    Meses_Para_Vender ,
    Media_De_Venda ,
    Std_De_Venda ,
    Numero_De_Lotes ,
    Valores_Entrada ,
    Obra ,
    Total_Obra ,
    Obra_Pre_Lancamento ,
    Aprovacao ,
    Valor_pre_Lancamento ,
    Meses_Pre_Lancamento ,
    Media_Pre_Lancamento ,
    Std_Dev_Pre_Lancamento ,
    Valor_Pos_Lancamento ,
    Meses_Pos_Lancamento ,
    Media_Pos_Lancamento ,
    Std_Dev_Pos_Lancamento ,
    Valores_Comissao 
)

# Botão de submissão
botao_submit = pn.widgets.Button(name="Enviar", button_type="primary")

# Função para capturar os valores
# Função para capturar os valores e salvar em CSV
def capturar_valores(event):
    # Cria um dicionário com os valores capturados
    valores = {
        'Nome_Do_Usuario': Nome_Do_Usuario.value,
        'Cidade': Cidade.value,
        'Nome_Empresa': Nome_Empresa.value,
        'Parcelas_Entrada': Parcelas_Entrada.value,
        'Entrada_A_Vista': Entrada_A_Vista.value,
        'Entrada_A_Prazo_1': Entrada_A_Prazo_1.value,
        'Entrada_A_Prazo_2': Entrada_A_Prazo_2.value,
        'Saldo_Parcelado': Saldo_Parcelado.value,
        'Parcelas': Parcelas.value,
        'Juros': Juros.value,
        'Juros_Mensal': Juros_Mensal.value,
        'Valor_Do_Lote': Valor_Do_Lote.value,
        'Valor_Parcela': Valor_Parcela.value,
        'Tamanho': Tamanho.value,
        'Percentual_empreendedor': Percentual_empreendedor.value,
        'Comissao_Total': Comissao_Total.value,
        'Parcelamento_Comissao': Parcelamento_Comissao.value,
        'Imposto': Imposto.value,
        'Taxa_Adm': Taxa_Adm.value,
        'Meses_Para_Vender': Meses_Para_Vender.value,
        'Media_De_Venda': Media_De_Venda.value,
        'Std_De_Venda': Std_De_Venda.value,
        'Numero_De_Lotes': Numero_De_Lotes.value,
        'Valores_Entrada': Valores_Entrada.value,
        'Obra': Obra.value,
        'Total_Obra': Total_Obra.value,
        'Obra_Pre_Lancamento': Obra_Pre_Lancamento.value,
        'Aprovacao': Aprovacao.value,
        'Valor_pre_Lancamento': Valor_pre_Lancamento.value,
        'Meses_Pre_Lancamento': Meses_Pre_Lancamento.value,
        'Media_Pre_Lancamento': Media_Pre_Lancamento.value,
        'Std_Dev_Pre_Lancamento': Std_Dev_Pre_Lancamento.value,
        'Valor_Pos_Lancamento': Valor_Pos_Lancamento.value,
        'Meses_Pos_Lancamento': Meses_Pos_Lancamento.value,
        'Media_Pos_Lancamento': Media_Pos_Lancamento.value,
        'Std_Dev_Pos_Lancamento': Std_Dev_Pos_Lancamento.value,
        'Valores_Comissao': Valores_Comissao.value
    }

    # Salva os valores em um arquivo CSV
    df = pd.DataFrame([valores])
    df.to_csv('dados_usuario.csv', index=False)
    print("Valores capturados e salvos em CSV!")


# Vincular a função ao botão
botao_submit.on_click(capturar_valores)

# Multi-passos usando abas (tabs)
multi_step_layout = pn.Tabs(
    ("Introdução", pn.Column(header)),
    ("Passo 1 - Vendas e Lotes", Passo2),
    ("Passo 2 - Obra e Comissões", Passo3),
    ("Finalizar", pn.Column(pn.pane.Markdown("### Obrigado por preencher os dados!"), botao_submit))
)

# Mostrar o layout multi-passos
multi_step_layout.show()
