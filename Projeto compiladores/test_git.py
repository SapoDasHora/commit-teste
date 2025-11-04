def main():
    print("=== Compilador - Calculadora ===")
    print("Digite expressões matemáticas para calcular.")
    print("Use o comando 'sair' para encerrar.\n")

    while True:
        entrada = input(">> ")

        if entrada.lower() == "sair":
            print("Encerrando o compilador. Até logo!")
            break

        try:
            # Avalia a expressão digitada
            resultado = eval(entrada)

            if not isinstance(resultado, (int, float)):
                print("Expressão inválida. Tente novamente.\n")
                continue

            print(f"Resultado decimal: {resultado}")
            print(f"Resultado hexadecimal: {hex(int(resultado))}\n")

        except Exception as e:
            print(f"Erro: {e}\nTente novamente.\n")


if __name__ == "__main__":
    main()
