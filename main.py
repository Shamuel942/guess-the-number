import random

def jugar():
    numero = random.randint(1, 100)
    intentos = 0

    print("🎲 ¡Adivina el número entre 1 y 100!")

    while True:
        intento = int(input("Tu intento: "))
        intentos += 1

        if intento < numero:
            print("📉 Es mayor.")
        elif intento > numero:
            print("📈 Es menor.")
        else:
            print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos.")
            break

if __name__ == "__main__":
    jugar()
