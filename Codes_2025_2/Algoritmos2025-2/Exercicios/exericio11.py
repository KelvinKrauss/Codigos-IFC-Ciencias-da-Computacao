import importlib
import multiprocessing
import os
import time

MODULE_NAME = "KK-Alg-051-EX-06"
TOTAL_ROLLS = 10_000_000

def run_simulation_chunk(num_rolls):
   

    sorteiadado = importlib.import_module(MODULE_NAME)
    
    local_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for _ in range(num_rolls):
        dado = sorteiadado.sorteia_dado()
        if dado in local_counts:
            local_counts[dado] += 1
            
    return local_counts

if __name__ == "__main__":
    num_processes = os.cpu_count()
    if num_processes is None:
        num_processes = 4 

    rolls_per_process = TOTAL_ROLLS // num_processes

    jobs = [rolls_per_process] * num_processes
    
    print(f"Iniciando simulação com {num_processes} processos...")
    start_time = time.time()


    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(run_simulation_chunk, jobs)

    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    for local_result in results:
        a += local_result.get(1, 0)
        b += local_result.get(2, 0)
        c += local_result.get(3, 0)
        d += local_result.get(4, 0)
        e += local_result.get(5, 0)
        f += local_result.get(6, 0)

    end_time = time.time()
    
    print(f"\nSimulação concluída em {end_time - start_time:.2f} segundos.\n")

    print(f"O 1 saiu: {a} vezes \nO 2 saiu: {b} vezes\nO 3 saiu: {c} vezes\nO 4 saiu: {d} vezes\nO 5 saiu: {e} vezes\nO 6 saiu: {f} vezes")