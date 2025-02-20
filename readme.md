# Estabilidade dos dados

## Descrição
Este código realiza a simulação conforme solicitado, garantindo um elevado número de linhas ao incluir explicações e verificações detalhadas. Ele mede o tempo total e o número de batimentos necessários para que os valores dos dados se estabilizem.

## Linguagem e Tipos de Código
- **Linguagem:** O código foi escrito em Python
- **Importação de bibliotecas:** `random:` Usado para gerar números aleatórios. No código, é utilizado para simular o lançamento de um dado (gerando números inteiros de 1 a 6).
- `time:` Usado para pausar a execução do programa por um tempo específico. No código, é utilizado para simular o tempo entre as batidas dos dados e calcular o tempo total do experimento.

## Funções Utilizadas
Função `lancar_dado()`:

- Objetivo: Simula o lançamento de um dado de 6 faces. Retorna um valor aleatório entre 1 e 6.
- Tipo de Retorno: Inteiro `(int)`, representando o valor do dado lançado.
- Implementação:

```properties
return random.randint(1, 6)
```
A função `random.randint(1, 6)` gera um número inteiro aleatório no intervalo de 1 a 6, simulando o lançamento de um dado de seis faces.

Função `experimento(tempo_entre_batidas=1, limite_estabilidade=5)`:
- **Objetivo**: Simula o experimento onde dois dados são "agitados" por tapas e verifica quando eles atingem estabilidade (quando o valor dos dados não muda por um número consecutivo de batidas).

Parâmetros:
- `tempo_entre_batidas`: Tempo, em segundos, entre cada batida. O padrão é 1 segundo.
- `limite_estabilidade`: O número de batidas consecutivas em que o valor dos dois dados não pode mudar para que o experimento seja considerado estável. O valor padrão é 5.

Funções Internas:
- `time.sleep(tempo_entre_batidas)`: Faz com que o programa espere pelo tempo especificado entre as batidas, simulando o intervalo de tempo entre elas.

Estrutura de controle:
- O programa continua realizando as batidas e verificando os valores dos dados. Se os dados permanecem os mesmos após uma batida, o contador de batidas estáveis `(batidas_estaveis)` é incrementado.
- Se os dados mudam, o contador de batidas estáveis é reiniciado.
- Tempo total do experimento: A função calcula o tempo total do experimento, registrando o tempo de início e o tempo de fim, e então calcula a diferença.
- Prints: O código imprime no terminal os resultados de cada batida, os valores dos dados e o tempo total.
  
Função `main()`:

**Objetivo**: Configura os parâmetros padrão (tempo entre as batidas e limite de estabilidade) e chama a função `experimento()` para executar a simulação.

```properties
tempo_entre_batidas = 1  # Tempo de 1 segundo entre batidas
limite_estabilidade = 5  # Limite de 5 batidas consecutivas sem mudança
experimento(tempo_entre_batidas, limite_estabilidade)
```
Condição de Execução Principal:

- O código é executado a partir da chamada da função `main()` quando o arquivo Python é rodado diretamente. A linha:

```properties
if __name__ == "__main__":
    main()
```
Verifica se o arquivo está sendo executado como o script principal e, caso positivo, chama a função `main()`.

## Principais Tipos de Dados

- Inteiros `(int)`: O código usa inteiros para representar os valores lançados pelos dados (números entre 1 e 6).
- Flutuantes `(float)`: O tempo total do experimento é armazenado como um número flutuante, representando o tempo decorrido.
- Strings `(str)`: Utilizado nas mensagens de print para mostrar os resultados.

## Comportamento do Código

- O experimento simula lançamentos de dois dados e os compara após cada "batida" (tapada). O programa continua até que os dados se estabilizem, ou seja, até que, por um número consecutivo de batidas, os valores dos dois dados não mudem.
- A função `lancar_dado()` simula um lançamento aleatório do dado.
- A função `experimento()` organiza a dinâmica da simulação e controle do experimento, gerenciando o número de batidas, a estabilidade e o tempo total.
- O tempo entre batidas e o número de batidas para estabilidade são ajustáveis.

Esse código é útil para simular experimentos probabilísticos e também serve para estudar a estabilidade em processos dinâmicos de experimentos controlados com variáveis aleatórias.

## **Muito Obrigado pela sua atenção!**
