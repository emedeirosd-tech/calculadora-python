continuar = "s"
while continuar == "s":
   print("=" * 30)
   print ("CALCULADORA EM PYTHON")
   print("=" * 30)
   print ("1 - Adição")
   print ("2 - Subtração")
   print ("3 - Multiplicação")
   print ("4 - Divisão")
   print ("0 - Sair")
   operação = input("Escolha uma operação: ")
   primeiro_numero = float(input("Primeiro número: "))
   segundo_numero = float(input("Segundo número: "))
   if operação == "1":
        print(f" {primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}")
   elif operação == "2":
        print (f" {primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}")
   elif operação == "3":
        print (f" {primeiro_numero} * {segundo_numero} = {primeiro_numero * segundo_numero}")
   elif operação == "4":
       if segundo_numero == 0:
            print("Erro: divisão por zero não é permitida.")
       else: 
            print (f" {primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero}")
   elif operação == "0":
        break
   else: 
        print ("Opção invalida.")
   continuar = input("Outro cálculo? (s/n): ")
print("Programa encerrado.")