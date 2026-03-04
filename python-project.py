percent = float(input("질량 퍼센트를 넣으세요:"))
density = float(input("밀도를 넣으세요:"))
molarmass = float(input("몰질량을 넣으세요:"))
def 퍼센트_몰_변환(percent, density, molarmass):
    molarity = (10*percent*density)/molarmass
    return molarity
result = 퍼센트_몰_변환(percent, density, molarmass)
print(f"M(몰농도)={result:.2f}M")


