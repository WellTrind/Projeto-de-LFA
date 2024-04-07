!pip install automathon --upgrade # instalar a biblioteca automathon

from automathon import DFA # importando a biblioteca automathon

Q = {"q0", "q1", "q2"} # estados contidos nesse AFD.
sigma = {"0", "1"}
delta = { "q0" : {"1" : "q1", "0" : "q0"},
          "q1" : {"0" : "q0", "1" : "q2"},
          "q2" : {"0" : "q0", "1" : "q2"}
        } # tabela de estados.
estado_inicial = "q0" # definição do estado inicial.
estado_final = {"q0"} # definição do estado final.

automato = DFA(Q, sigma, delta, estado_inicial, estado_final)

automato.is_valid()

print ("Automato aceita alfabeto 1110: ", automato.accept("1110")) # funcionamento completo da máquina.

print("Automato aceita alfabeto 110: ", automato.accept("110")) # funcionamento parcial da máquina.

print("Automato aceita alfabeto 0000: ", automato.accept("0000")) #Máquina em estado de repouso

print("Automato aceita alfabeto 1111: ", automato.accept("1111")) #Máquina em loop de perfuração

automato.view("afd01")

automato.view(
    file_name="afd01_personalizado",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
) # geração de um PNG do AFD.
