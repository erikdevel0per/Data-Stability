import random
import time

def lancar_dado():
    """Simula o lançamento de um dado de 6 faces."""
    return random.randint(1, 6)

def experimento(tempo_entre_batidas=1, limite_estabilidade=5):
    """
    Simula a experiência com dois dados sendo agitados por tapas.
    Calcula o tempo e o número de batidas necessárias para alcançar a estabilidade.
    
    Parâmetros:
    - tempo_entre_batidas: Tempo (em segundos) entre cada batida.
    - limite_estabilidade: Número de batidas consecutivas sem mudança para considerar estabilidade.
    """
    dado1 = lancar_dado()
    dado2 = lancar_dado()
    
    print(f"Valores iniciais: Dado 1 = {dado1}, Dado 2 = {dado2}")
    
    num_batidas = 0
    batidas_estaveis = 0
    inicio_experimento = time.time()
    
    while batidas_estaveis < limite_estabilidade:
        time.sleep(tempo_entre_batidas)  # Simula o tempo entre batidas
        num_batidas += 1
        
        novo_dado1 = lancar_dado()
        novo_dado2 = lancar_dado()
        
        print(f"Batida {num_batidas}: Dado 1 = {novo_dado1}, Dado 2 = {novo_dado2}")
        
        if novo_dado1 == dado1 and novo_dado2 == dado2:
            batidas_estaveis += 1
        else:
            batidas_estaveis = 0  # Reinicia o contador de estabilidade se houver mudança
        
        dado1, dado2 = novo_dado1, novo_dado2
    
    fim_experimento = time.time()
    tempo_total = fim_experimento - inicio_experimento
    
    print(f"\nEstabilidade alcançada após {num_batidas} batidas em {tempo_total:.2f} segundos.")

def main():
    tempo_entre_batidas = 1  # Ajustável conforme necessidade
    limite_estabilidade = 5   # Número de batidas consecutivas sem mudança para estabilidade
    experimento(tempo_entre_batidas, limite_estabilidade)

if __name__ == "__main__":
    main()