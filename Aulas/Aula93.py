import importlib
import Aula93_m

print(Aula93_m.variavel)

for i in range(10):
    importlib.reload(Aula93_m)
    print(i)

print("FIM")