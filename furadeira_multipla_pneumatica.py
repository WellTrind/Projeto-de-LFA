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
