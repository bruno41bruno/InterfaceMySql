from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

ml = ["BRL","USD","EUR","GBP"]
banco = "database"
cursor = "cursor"
moeda_orig = 0
moeda_dest = 0
cambio = 10
operacao = "nenhuma"

#22/05/2021
brl_eur = 0.15350
brl_usd = 0.18700
brl_gbp = 0.13200
usd_brl = 5.3661
usd_eur = 0.82090
usd_gbp = 0.70660
eur_brl = 6.5425
eur_usd = 1.22020
eur_gbp = 0.86240
gbp_brl = 7.5938
gbp_usd = 1.41500
gbp_eur = 1.16160



def formulario_Janela_Aba1():
    Formulario.W_formulario.close()

def formulario_Janela_Aba2():
    Formulario.W_formulario.show()

def cot_janela_Aba1():
    Cotacao.janela1_m.close()

def cot_janela_Aba2():
    Cotacao.janela1_m.show()

def table_config():
    Tabela.show()

def calendario():
    Calendario.show()

def add_dados():
    dados = Tabela.line_t_tabela.text()
    Tabela.table_list.addItem(dados)
    Tabela.line_t_tabela.setText("")
    cliente = Tabela.line_t_cliente.text()
    Tabela.table_list.addItem(cliente)
    Tabela.line_t_cliente.setText("")
    cursor.execute("CREATE TABLE {dados} ({cliente} text,{operacao} text,{total_convert} text, {total_camb} text, {data_formatada} text)")

def delete_dados_table():
    Tabela.table_list.takeItem(Tabela.table_list.currentRow())

def cotacao_config():
    Cotacao.show()

def choose_save_moeda():
    global moeda_orig
    moeda_orig = Formulario.combo_Orig_3.currentText()
    global moeda_dest
    moeda_dest = Formulario.combo_Dest_3.currentText()
    Formulario.dest_select_3.setText("Selecionada:   "+ moeda_dest)
    Formulario.orig_select_3.setText("Selecionada:   "+ moeda_orig)
    Formulario.moeda_orig_cal.setText("Moeda de Origem:   "+ moeda_orig)
    Formulario.moeda_dest_cal.setText("Moeda de Destino:   "+ moeda_dest)
    Formulario.camb_cal.setText("Taxa de cambio:   "+str(cambio))

def calculadora():
    str_valor = Formulario.valor_cal.text()
    valor = float(str_valor)
    global moeda_orig
    global moeda_dest
    if moeda_orig == moeda_dest:
        QMessageBox.about(Formulario,
        "Erro!!!",
        "  Uma das moedas deve ser diferente!    "
        )
    elif valor <= 0:
        QMessageBox.about(Formulario,
        "Erro!!!",
        "  Valor não pode ser igual ou menor que 0!    "
        )
    elif moeda_orig == ml[0] and moeda_dest == ml[1]:
        global brl_usd
        total_convert = brl_usd * valor
        global cambio
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[0] and moeda_dest == ml[2]:
        global brl_eur
        total_convert = brl_eur * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[0] and moeda_dest == ml[3]:
        global brl_gbp
        total_convert = brl_gbp * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[1] and moeda_dest == ml[0]:
        global usd_brl
        total_convert = usd_brl * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[1] and moeda_dest == ml[2]:
        global usd_eur
        total_convert = usd_eur * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[1] and moeda_dest == ml[3]:
        global usd_gbp
        total_convert = usd_gbp * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[2] and moeda_dest == ml[0]:
        global eur_brl
        total_convert = eur_brl * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[2] and moeda_dest == ml[1]:
        global eur_usd
        total_convert = eur_usd* valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[2] and moeda_dest == ml[3]:
        global eur_gbp
        total_convert = eur_gbp * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[3] and moeda_dest == ml[0]:
        global gbp_brl
        total_convert = gbp_brl * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[3] and moeda_dest == ml[1]:
        global gbp_usd
        total_convert = gbp_usd * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    elif moeda_orig == ml[3] and moeda_dest == ml[2]:
        global gbp_eur
        total_convert = gbp_eur * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_cambio + total_convert
    Formulario.total_camb_cal.setText(
        "Total do Cambio: "+str(round(total_cambio,2)))
    Formulario.resultado_cal.setText(
        "Resultado Total: "+str(round(result_final,2)))
    Formulario.convert_calculo.setText(
        "Conversão Total: "+str(round(total_convert,2)))
    global operacao
    operacao = moeda_orig+"para"+moeda_dest


def cot_change():
    m_orig_m = Cotacao.combo_orig_m.currentText()
    m_dest_m = Cotacao.combo_dest_m.currentText()
    cotacao_value = Cotacao.cot_change_m.text()
    if m_orig_m == ml[0] and m_dest_m == ml[1]:
        global brl_usd
        brl_usd = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[0] and m_dest_m == ml[2]:
        global brl_eur
        brl_eur = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[0] and m_dest_m == ml[3]:
        global brl_gbp
        brl_gbp = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[1] and m_dest_m == ml[0]:
        global usd_brl
        usd_brl = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[1] and m_dest_m == ml[2]:
        global usd_eur
        usd_eur = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[1] and m_dest_m == ml[3]:
        global usd_gbp
        usd_gbp = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[2] and m_dest_m == ml[0]:
        global eur_brl
        eur_brl = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[2] and m_dest_m == ml[1]:
        global eur_usd
        eur_usd = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[2] and m_dest_m == ml[3]:
        global eur_gbp
        eur_gbp = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[3] and m_dest_m == ml[0]:
        global gbp_brl
        gbp_brl = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[3] and m_dest_m == ml[1]:
        global gbp_usd
        gbp_usd = float(cotacao_value.replace(".",","))
    elif m_orig_m == ml[3] and m_dest_m == ml[2]:
        global gbp_eur
        gbp_eur = float(cotacao_value.replace(".",","))

def cot_view():
    cot = "Cotação Atual :"
    #BRL
    if (Cotacao.brl_m_orig.isChecked()) and (Cotacao.eur_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(brl_eur))
    elif (Cotacao.brl_m_orig.isChecked()) and (Cotacao.usd_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(brl_usd))
    elif (Cotacao.brl_m_orig.isChecked()) and (Cotacao.gbp_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(brl_gbp))
    #USD
    elif (Cotacao.usd_m_orig.isChecked()) and (Cotacao.eur_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(usd_eur))
    elif (Cotacao.usd_m_orig.isChecked()) and (Cotacao.brl_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(usd_brl))
    elif (Cotacao.usd_m_orig.isChecked()) and (Cotacao.gbp_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(usd_gbp))
    #EUR
    elif (Cotacao.eur_m_orig.isChecked()) and (Cotacao.usd_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(eur_usd))
    elif (Cotacao.eur_m_orig.isChecked()) and (Cotacao.brl_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(eur_brl))
    elif (Cotacao.eur_m_orig.isChecked()) and (Cotacao.gbp_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(eur_gbp))
    #GBP
    elif (Cotacao.gbp_m_orig.isChecked()) and (Cotacao.usd_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(gbp_usd))
    elif (Cotacao.gbp_m_orig.isChecked()) and (Cotacao.brl_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(gbp_brl))
    elif (Cotacao.gbp_m_orig.isChecked()) and (Cotacao.eur_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(gbp_eur))
    (Cotacao.gbp_m_orig.setChecked(False))
    (Cotacao.eur_m_orig.setChecked(False))
    (Cotacao.usd_m_orig.setChecked(False))
    (Cotacao.brl_m_orig.setChecked(False))
    (Cotacao.eur_m_dest.setChecked(False))
    (Cotacao.usd_m_dest.setChecked(False))
    (Cotacao.gbp_m_dest.setChecked(False))
    (Cotacao.brl_m_dest.setChecked(False))

def pegar_data():
    date = str(Calendario.datinha_c.selectedDate())
    data_formatada = date[19:30]
    print(data_formatada)
#banco de dados
def database_controll():
    #criar
    global banco
    banco_db = banco
    global cursor
    cursor_db = cursor
    database = Formulario.bd1_f.text()
    cursor = banco.cursor()
    if database == "":
        QMessageBox.about(Formulario,
        "Erro!!!",
        "Digite um nome para o banco de Dados   "
        )
    else:
        banco = sqlite3.connect(database+".db")
        print(database+".db")
        QMessageBox.about(Formulario,
        "Criação concluída!",
        "       Banco de Dados"+database+".db         "
        )
def salvar_tudo():
    banco.commit()

def filtro():
    cursor.execute("SELECT * FROM {dados}")
    print(cursor.fetchall())
    print("funfei")

app=QtWidgets.QApplication([])
Formulario=uic.loadUi("Formulario.ui")
Tabela=uic.loadUi("Tabela.ui")
Cotacao=uic.loadUi("Cotacao.ui")
Calendario=uic.loadUi("Calendario.ui")
#botões

Calendario.datinha_c.selectionChanged.connect(pegar_data)
Formulario.next_Janela_3.clicked.connect(formulario_Janela_Aba1)
Formulario.back_janela_2.clicked.connect(formulario_Janela_Aba2)
Formulario.save_moeda_3.clicked.connect(choose_save_moeda)
Formulario.choose_table_3.clicked.connect(table_config)
Formulario.window_moeda_3.clicked.connect(cotacao_config)
Formulario.calcular_cal.clicked.connect(calculadora)
Formulario.create_db.triggered.connect(database_controll)
Formulario.calen_b.clicked.connect(calendario)
Cotacao.verific_m.clicked.connect(cot_view)
Cotacao.next_janela_m.clicked.connect(cot_janela_Aba1)
Cotacao.back_janela1_m.clicked.connect(cot_janela_Aba2)
Cotacao.save_cot_m.clicked.connect(cot_change)
Tabela.add_table_t.clicked.connect(add_dados)
Tabela.clear_t.clicked.connect(delete_dados_table)
Tabela.actionSalvar_no_Banco_de_Dados.triggered.connect(salvar_tudo)
Tabela.filtrar_t.clicked.connect(filtro)

#comboBox
Formulario.combo_Orig_3.addItems(ml)
Formulario.combo_Dest_3.addItems(ml)
Cotacao.combo_orig_m.addItems(ml)
Cotacao.combo_dest_m.addItems(ml)

Formulario.show()
app.exec()