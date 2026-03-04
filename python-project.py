while True:
    print("==========실행할 농도 변환 계산기를 선택하세요. ==========")
    print("1. 퍼센트_몰 변환계산")
    print("2. 몰_몰랄 변환계산")
    print("0. 계산 종료")
    choice = input("번호 선택:")
    if choice == "1":
        percent = float(input("질량 퍼센트를 넣으세요:"))
        density = float(input("밀도를 넣으세요:"))
        molarmass = float(input("몰질량을 넣으세요:"))
        def 퍼센트_몰_변환(percent, density, molarmass):
            molarity = (10*percent*density)/molarmass
            return molarity
        result = 퍼센트_몰_변환(percent, density, molarmass)
        print(f"M(몰농도)={result:.2f}M")
    elif choice == "0":
        print("계산기를 종료합니다")
        break