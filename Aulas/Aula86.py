# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# def generator(n=0):
#     yield 1 # Pausou
#     print("Não acabou!") 
#     yield 2 # Pausado
#     return "FIM!!"

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n > maximum:
            return

gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
for n in gen:
    print(n)