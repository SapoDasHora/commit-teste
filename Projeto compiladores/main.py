"\"\"\"Módulo didático para converter uma palavra em representação binária.\"\"\""

from __future__ import annotations


class Compiler:
    """Compila uma palavra (string) em uma sequência binária de 8 bits."""

    def __init__(self, palavra: str) -> None:
        self.palavra = palavra
        self._bytes_binarios: list[str] = []
        self._bytes_hexadecimais: list[str] = []

    def compile(self) -> str:
        """Converte cada caractere da palavra em binário de 8 bits."""
        self._bytes_binarios = []

        for caractere in self.palavra:
            valor_decimal = ord(caractere)
            byte_binario = format(valor_decimal, "08b")
            self._bytes_binarios.append(byte_binario)

        return " ".join(self._bytes_binarios)

    def compile_hex(self) -> str:
        """Converte cada caractere da palavra em representação hexadecimal."""
        self._bytes_hexadecimais = []

        for caractere in self.palavra:
            valor_decimal = ord(caractere)
            byte_hex = format(valor_decimal, "02X")
            self._bytes_hexadecimais.append(byte_hex)

        return " ".join(self._bytes_hexadecimais)

    def verbose_compilation(self) -> None:
        """Mostra o passo a passo da compilação no terminal."""
        if not self.palavra:
            print("Nenhum caractere fornecido para compilação.")
            return

        print("Iniciando compilação...\n")

        for caractere in self.palavra:
            valor_decimal = ord(caractere)
            byte_binario = format(valor_decimal, "08b")
            byte_hex = format(valor_decimal, "02X")
            print(
                f"Caractere '{caractere}' -> Decimal {valor_decimal} -> "
                f"Binário {byte_binario} -> Hex {byte_hex}"
            )

        print("\nCompilação concluída!\n")


def main() -> None:
    """Função principal: solicita palavra, compila e exibe o resultado."""
    print("Mini-compilador Texto -> Máquina (Binário)")
    print(
        "Digite uma palavra para ver a compilação; use 'exit' ou pressione Enter sem texto para sair.\n"
    )

    while True:
        palavra = input("Palavra: ")
        if not palavra or palavra.strip().lower() == "exit":
            print("Encerrando compilador. Até a próxima!")
            break

        compilador = Compiler(palavra)
        compilador.verbose_compilation()
        codigo_binario = compilador.compile()
        codigo_hexadecimal = compilador.compile_hex()

        print(f"Código de Máquina Gerado (Binário): {codigo_binario}")
        print(f"Código de Máquina Gerado (Hexadecimal): {codigo_hexadecimal}\n")


"""
Exemplo de execução:

Mini-compilador Texto -> Máquina (Binário)
Digite uma palavra para ver a compilação; use 'exit' ou pressione Enter sem texto para sair.

Palavra: Hi
Iniciando compilação...

Caractere 'H' -> Decimal 72 -> Binário 01001000 -> Hex 48
Caractere 'i' -> Decimal 105 -> Binário 01101001 -> Hex 69

Compilação concluída!

Código de Máquina Gerado (Binário): 01001000 01101001
Código de Máquina Gerado (Hexadecimal): 48 69

Palavra: exit
Encerrando compilador. Até a próxima!
"""


if __name__ == "__main__":
    main()

