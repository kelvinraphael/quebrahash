import hashlib
import time
import threading

hashbuscado = "ca6ae33116b93e57b87810a27296fc36"

encontrado = False
senha = None


def md5_string(texto):
    return hashlib.md5(texto.encode()).hexdigest()


def worker(inicio_d1, fim_d1):

    global encontrado, senha

    for d1 in range(inicio_d1, fim_d1):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            for d7 in range(10):
                                for d8 in range(10):
                                    for d9 in range(10):

                                        if encontrado:
                                            return

                                        combinacao = f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}"

                                        hash_calculado = md5_string(combinacao)

                                        if hash_calculado == hashbuscado:
                                            senha = combinacao
                                            encontrado = True
                                            print("Senha encontrada:", combinacao)
                                            return


def executar(num_threads):

    global encontrado, senha

    # RESETAR variáveis
    encontrado = False
    senha = None

    threads = []

    intervalo = 10 // num_threads

    inicio = time.time()

    start = 0

    for i in range(num_threads):

        end = start + intervalo

        if i == num_threads - 1:
            end = 10

        t = threading.Thread(target=worker, args=(start, end))
        threads.append(t)
        t.start()

        start = end

    for t in threads:
        t.join()

    fim = time.time()

    tempo = fim - inicio

    print(f"Threads: {num_threads} | Tempo: {tempo:.2f}s\n")

    return tempo


if __name__ == "__main__":

    tempos = {}

    for t in [2,4,8,12]:
        tempos[t] = executar(t)

    print("Resultados finais:", tempos)