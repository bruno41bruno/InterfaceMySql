from PyQt5 import uic,QtWidgets
import sqlite3
from data import date
from PyQt5.QtWidgets import QMessageBox

data_time = "Data: "+date
ml = ["BRL","USD","EUR","GBP"]
moeda_orig = 0
moeda_dest = 0
cambio = 10
valor = 0
total_cambio = 0
result_final = 0

banco = sqlite3.connect("primeiro_bd")
cursor = banco.cursor()
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

def table_delete():
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
    cliente = Formulario.client_line.text()
    str_valor = Formulario.valor_cal.text()
    global valor
    valor = float(str_valor)
    global moeda_orig
    global moeda_dest
    if moeda_orig == moeda_dest:
        total_convert = 0
        global total_cambio
        total_cambio = 0 
        global result_final
        result_final = 0
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
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[0] and moeda_dest == ml[2]:
        global brl_eur
        total_convert = brl_eur * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[0] and moeda_dest == ml[3]:
        global brl_gbp
        total_convert = brl_gbp * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[1] and moeda_dest == ml[0]:
        global usd_brl
        total_convert = usd_brl * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[1] and moeda_dest == ml[2]:
        global usd_eur
        total_convert = usd_eur * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[1] and moeda_dest == ml[3]:
        global usd_gbp
        total_convert = usd_gbp * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[2] and moeda_dest == ml[0]:
        global eur_brl
        total_convert = eur_brl * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[2] and moeda_dest == ml[1]:
        global eur_usd
        total_convert = eur_usd* valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[2] and moeda_dest == ml[3]:
        global eur_gbp
        total_convert = eur_gbp * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[3] and moeda_dest == ml[0]:
        global gbp_brl
        total_convert = gbp_brl * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[3] and moeda_dest == ml[1]:
        global gbp_usd
        total_convert = gbp_usd * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio
    elif moeda_orig == ml[3] and moeda_dest == ml[2]:
        global gbp_eur
        total_convert = gbp_eur * valor
        total_cambio = total_convert * cambio/100 
        result_final = total_convert - total_cambio 
    Formulario.total_camb_cal.setText(
        "Total do Cambio: "+str(round(total_cambio,2)))
    Formulario.resultado_cal.setText(
        "Resultado Total: "+str(round(result_final,2)))
    Formulario.convert_calculo.setText(
        "Conversão Total: "+str(round(total_convert,2)))
    Tabela.table_list.addItem(data_time)
    Tabela.table_list.addItem("Cliente: "+cliente)
    Tabela.table_list.addItem(str(moeda_orig)+" to "+str(moeda_dest))
    Tabela.table_list.addItem("Valor Original: "+str(round(valor,2)))
    Tabela.table_list.addItem("Taxa Cobrada: "+str(round(total_cambio,2)))
    Tabela.table_list.addItem("Valor Completo: "+str(round(result_final,2)))

def salvar_dados():
    dados = data_time+"  Cliente: " +cliente+ "  Operação: " +str(moeda_dest)+ "   to  " +str(moeda_orig) +"  Valor Total:  "+ str(round(valor,2)) +"   Total da Taxa:  "+str(round(total_cambio,2)) +"   Rsultado Final: "+ str(round(result_final,2))

    arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]

    with open (arquivo + ".txt", "w") as arq:
        arq.write(dados)

def salvar_tudo():
    cursor.execute("Insert INTO clientes VALUES('"+data_time+"','"+cliente+"','"+str(moeda_dest) +"','"+ str(moeda_orig)+"','"+str(round(result_final,2))+"','"+str(round(total_cambio,2))+"','"+str(round(valor,2))+"')")

    print("Os dados foram salvos!!")
    banco.commit()

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

def criar_tabela():
    try :
        cursor.execute("CREATE TABLE clientes (data text, nome text, operacaodest text,operacaoorig text, valor_total text, valor_cambio text, valor_original text)")

        cursor.execute("SELECT * FROM clientes")
        print(cursor.fetchall())

        banco.commit()


    except sqlite3.Error as erro:
        print("Algo de Errado Ocorreu!!  ",erro)

def cot_view():
    cot = "Cotação Atual :"
    #BRL
    if (Cotacao.brl_m_orig.isChecked()) and (Cotacao.eur_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(brl_eur,2)))
    elif (Cotacao.brl_m_orig.isChecked()) and (Cotacao.usd_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(brl_usd,2)))
    elif (Cotacao.brl_m_orig.isChecked()) and (Cotacao.gbp_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(brl_gbp,2)))
    #USD
    elif (Cotacao.usd_m_orig.isChecked()) and (Cotacao.eur_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(usd_eur,2)))
    elif (Cotacao.usd_m_orig.isChecked()) and (Cotacao.brl_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(usd_brl,2)))
    elif (Cotacao.usd_m_orig.isChecked()) and (Cotacao.gbp_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(usd_gbp,2)))
    #EUR
    elif (Cotacao.eur_m_orig.isChecked()) and (Cotacao.usd_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(eur_usd,2)))
    elif (Cotacao.eur_m_orig.isChecked()) and (Cotacao.brl_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(eur_brl,2)))
    elif (Cotacao.eur_m_orig.isChecked()) and (Cotacao.gbp_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(eur_gbp,2)))
    #GBP
    elif (Cotacao.gbp_m_orig.isChecked()) and (Cotacao.usd_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(gbp_usd,2)))
    elif (Cotacao.gbp_m_orig.isChecked()) and (Cotacao.brl_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(gbp_brl,2)))
    elif (Cotacao.gbp_m_orig.isChecked()) and (Cotacao.eur_m_dest.isChecked()):
        Cotacao.cot_atual_m.setText(cot +str(round(gbp_eur,2)))
    (Cotacao.gbp_m_orig.setChecked(False))
    (Cotacao.eur_m_orig.setChecked(False))
    (Cotacao.usd_m_orig.setChecked(False))
    (Cotacao.brl_m_orig.setChecked(False))
    (Cotacao.eur_m_dest.setChecked(False))
    (Cotacao.usd_m_dest.setChecked(False))
    (Cotacao.gbp_m_dest.setChecked(False))
    (Cotacao.brl_m_dest.setChecked(False))

def listar():
    cursor.execute("SELECT * FROM clientes")
    print(cursor.fetchall())

def clean():
    Formulario.total_camb_cal.setText("Total do Cambio: ")
    Formulario.resultado_cal.setText("Resultado Total: ")
    Formulario.convert_calculo.setText("Conversão Total: ")
    Formulario.valor_cal.setText("")
    Formulario.client_line.setText("")

app=QtWidgets.QApplication([])
Formulario=uic.loadUi("Formulario.ui")
Tabela=uic.loadUi("Tabela.ui")
Cotacao=uic.loadUi("Cotacao.ui")
#data
Formulario.data.setText(data_time)
cliente = Formulario.client_line.text()
#botões
Formulario.clear_all.clicked.connect(clean)
Formulario.next_Janela_3.clicked.connect(formulario_Janela_Aba1)
Formulario.back_janela_2.clicked.connect(formulario_Janela_Aba2)
Formulario.save_moeda_3.clicked.connect(choose_save_moeda)
Formulario.choose_table_3.clicked.connect(table_config)
Formulario.window_moeda_3.clicked.connect(cotacao_config)
Formulario.calcular_cal.clicked.connect(calculadora)
Formulario.create_table.triggered.connect(criar_tabela)
Cotacao.verific_m.clicked.connect(cot_view)
Cotacao.next_janela_m.clicked.connect(cot_janela_Aba1)
Cotacao.back_janela1_m.clicked.connect(cot_janela_Aba2)
Cotacao.save_cot_m.clicked.connect(cot_change)
Tabela.save.triggered.connect(salvar_dados)
Tabela.delete_t.clicked.connect(table_delete)
Tabela.save_bd.triggered.connect(salvar_tudo)
Tabela.filtrar_t.clicked.connect(listar)

#comboBox
Formulario.combo_Orig_3.addItems(ml)
Formulario.combo_Dest_3.addItems(ml)
Cotacao.combo_orig_m.addItems(ml)
Cotacao.combo_dest_m.addItems(ml)

Formulario.show()
app.exec()