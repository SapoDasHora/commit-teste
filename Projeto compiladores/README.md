# Mini-Compilador: Texto para Código de Máquina

Projeto acadêmico desenvolvido para demonstrar, de forma simples e visual, a tradução de texto para representações de máquina: binário e hexadecimal. O foco é trabalhar o conceito de compilação em um cenário reduzido, onde cada caractere da palavra de entrada é convertido para seu equivalente em código de máquina.

---

## Objetivos do Projeto

- Mostrar, passo a passo, o processo de tradução de caracteres para códigos numéricos.
- Ilustrar como bytes podem ser representados em diferentes bases (binário e hexadecimal).
- Prover uma experiência interativa e didática para uso em sala de aula ou em apresentações.

---

## Estrutura do Repositório

```
.
├── README.md
└── text_to_binary.py
```

- `text_to_binary.py`: script principal contendo a classe `Compiler`, responsável por compilar a palavra para código de máquina.
- `README.md`: documentação detalhada do projeto.

---

## Pré-requisitos

- Python 3.10 ou superior (recomendado).
- Nenhuma dependência externa é necessária.

---

## Como Executar

1. Abra um terminal na pasta do projeto:

   ```bash
   cd C:/Users/joaov/Documents/Faculdade/Compiladores
   ```

2. Execute o programa:

   ```bash
   python text_to_binary.py
   ```

3. Interaja com o mini-compilador:
   - Digite qualquer palavra para ver a compilação.
   - Utilize `exit` (ou pressione Enter sem texto) para encerrar.

---

## Como Rodar

Siga este roteiro rápido para executar a aplicação em qualquer computador com Python instalado:

1. **Verifique a versão do Python**

   ```bash
   python --version
   ```

   O comando deve retornar `Python 3.10` ou superior.

2. **Acesse o diretório do projeto**

   ```bash
    cd C:/Users/joaov/Documents/Faculdade/Compiladores
   ```

3. **Inicie o programa**

   ```bash
   python text_to_binary.py
   ```

4. **Use o compilador**
   - Digite a palavra que deseja converter.
   - Observe a versão detalhada em binário e hexadecimal.
   - Digite `exit` (ou pressione Enter sem texto) quando quiser encerrar.

---

## Funcionamento do Programa

### Classe `Compiler`

- Recebe a palavra a ser compilada no `__init__`.
- Método `compile()`:
  - Percorre cada caractere da palavra.
  - Converte para decimal (`ord`) e depois para binário (`format(valor, "08b")`).
  - Retorna todos os bytes binários separados por espaço.
- Método `compile_hex()`:
  - Realiza a mesma iteração, mas converte os valores para hexadecimal (`format(valor, "02X")`).
  - Retorna a string com os bytes hexadecimais separados por espaço.
- Método `verbose_compilation()`:
  - Imprime, passo a passo, a transformação de cada caractere.

### Função `main()`

- Exibe instruções iniciais.
- Mantém um loop interativo para coletar palavras do usuário.
- Chama `verbose_compilation()` para detalhar o processo.
- Apresenta as representações em binário e hexadecimal ao final de cada compilação.

---

## Exemplo de Execução

```
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
```

---

## Possíveis Extensões

- Adicionar suporte a arquivos de entrada e saída.
- Implementar uma interface gráfica para visualização dos bytes.
- Expandir o compilador para converter frases completas com pontuação.
- Oferecer outras bases numéricas (por exemplo, octal).

---

## Considerações Finais

Este mini-compilador é uma ferramenta simples, porém eficaz, para introduzir conceitos de compilação e representação de dados em baixo nível. O projeto pode ser facilmente adaptado para diferentes contextos educacionais, permitindo explorar temas como codificação de caracteres, bases numéricas e fluxos de processamento de dados.
