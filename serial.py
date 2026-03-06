import hashlib
import time

# hash que queremos quebrar
hashbuscado = "ca6ae33116b93e57b87810a27296fc36"


def md5_string(texto):
    return hashlib.md5(texto.encode()).hexdigest()


def buscahash9(hashbuscado):

    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            for d7 in range(10):
                                for d8 in range(10):
                                    for d9 in range(10):

                                        combinacao = f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}"

                                        hash_calculado = md5_string(combinacao)

                                        if hash_calculado == hashbuscado:
                                            print("Senha encontrada:", combinacao)
                                            return combinacao


inicio = time.time()

buscahash9(hashbuscado)

fim = time.time()

print("Tempo de execução:", fim - inicio, "segundos")