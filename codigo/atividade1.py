temp = float(input("Digite a temperatura: "))

SAFE = 15

if temp <= SAFE:
    print(f"O sistema está seguro, a temperatura está  em {temp:.1f} c°")
else:
    print(f"É necessário a manutenção, a temperatura está  em {temp:.1f} c°")