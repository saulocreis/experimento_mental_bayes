from random import randint as aleatorio

while(True):
 print("=== ALGORITMO BAYESIANO ===")
 print("Para sair do programa, basta apertar ENTER sem fornecer informacao util ao programa em qualquer momento.")
 try: 
  n_reg = int(input("Numero de regioes da mesa: "))
  marc = aleatorio(1, n_reg)
  print(f"A mesa foi dividida igualmente em regioes numeradas de 1 a {n_reg}, da esquerda para a direita.")
  print("(quanto mais proximo de 1, a regiao estah mais a esquerda)")
  print(f"(quanto mais proximo de {n_reg}, a regiao estah mais a direita)")
  print("A bola foi lancada na mesa. O ajudante marcou a posicao dela em uma dessas regioes.\n")
  n_esq_t, n_dir_t, n_lanc_t = 0, 0, 0
  while(True):
   print("SEU OBJETIVO: descobrir em qual regiao a marcacao foi feita.")
   print("Agora o ajudante vai lancar a bola quantas vezes voce desejar para obter informacao.")
   print("Depois desses lancamentos, ele lhe dira em quantos deles a bola ficou a ESQUERDA ou a DIREITA da marcacao.")
   n_esq, n_dir, n_lanc = 0, 0, int(input("\nAJUDANTE: Quantas vezes devo lancar a bola? "))
   for i in range(n_lanc):
    reg_lanc = aleatorio(1, n_reg)
    n_esq,n_dir = n_esq+(reg_lanc<marc)*1, n_dir+(reg_lanc>marc)*1
   n_esq_t,n_dir_t,n_lanc_t = n_esq_t+n_esq,n_dir_t+n_dir,n_lanc_t+n_lanc
   print(f"AJUDANTE: A bola foi lancada {n_lanc} vez(es) agora. Em relacao a marcacao,")
   print(f"{n_esq} foram a esquerda ({100*n_esq/n_lanc:.1f} % desses lancamentos)")
   print(f"{n_dir} foram a direita ({100*n_dir/n_lanc:.1f} % desses lancamentos)")
   print(f"\nAJUDANTE: Total de {n_lanc_t} lancamentos, sendo:")
   print(f"{n_esq_t} a esquerda ({100*n_esq_t/n_lanc_t:.1f} % do total)")
   print(f"{n_dir_t} a direita ({100*n_dir_t/n_lanc_t:.1f} % do total)")
   tent = int(input("\nAJUDANTE: Em qual regiao voce acha marcacao foi feita? "))
   if tent == marc:
    print(f"AJUDANTE: VOCE ACERTOU! A marcacao foi feita na regiao {marc}.\n")
    break
   else:
    print(f"AJUDANTE: VOCE ERROU. A marcacao nao foi feita na regiao {tent}. Vamos tentar de novo?\n")
 except:
  print("=== FIM ===")
  break