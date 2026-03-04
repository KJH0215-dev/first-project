while True:
    print("==========실행할 농도 변환 계산기를 선택하세요. ==========")
    print("1. 퍼센트_몰 변환계산")
    print("2. 몰_몰랄 변환계산")
    print("3. 퍼센트_몰랄 변환계산")
    print("4. 몰랄_퍼센트 변환계산")
    print("5. 몰_퍼센트 변환계산")
    print("6. 몰랄_몰 변환계산")
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
        print(f"M(몰농도)={result:.3f}M")
    elif choice == "2":
        molarity = float(input("몰 농도를 넣으세요:"))
        density = float(input("밀도를 넣으세요:"))
        molarmass = float(input("몰질량을 넣으세요"))
        def 몰_몰랄_변환(molarity, density, molarmass):
            molality = (1000*molarity)/(1000*density - molarity*molarmass)
            return molality
        result = 몰_몰랄_변환(molarity, density, molarmass)
        print(f"m(몰랄농도)={result:.3f}m")
    elif choice == "3":
        percent = float(input("질량 퍼센트를 넣으세요:"))
        molarmass = float(input("몰질량을 넣으세요:"))
        def 퍼센트_몰랄_변환(percent, molarmass):
            molality = percent*1000/molarmass(100-percent)
            return molality
        result = 퍼센트_몰랄_변환(percent, molarmass)
        print(f"m(몰랄농도)={result:.3f}m")
    elif choice == "4":
        molality = float(input("몰랄 농도를 넣으세요:"))
        molarmass = float(input("몰질량을 넣으세요:"))
        def 몰랄_퍼센트_변환(molality, molarmass):
            percent = 100*molality*molarmass/1000+(molarmass*molality)
            return percent
        result = 몰랄_퍼센트_변환(molality, molarmass)
        print(f"percent={result:.3f}%")
    elif choice == "5":
        molarity = float(input("몰 농도를 넣어주세요:"))
        molarmass =float(input("몰질량을 넣으세요:"))
        density = float(input("밀도를 넣으세요:"))
        def 몰_퍼센트_변환(molarity, molarmass, density):
            percent = molarity*molarmass/10*density
            return percent
        result = 몰_퍼센트_변환(molarity, molarmass, density)
        print(f"percent={result:.2f}%")
    elif choice == "6":
        density = float(input("밀도를 넣어주세요:"))
        molality = float(input("몰랄농도를 넣어주세요:"))
        molarmass = float(input("몰질량을 넣어주세요:"))
        def 몰랄_몰_변환(density, molality, molarmass):
            molarity = 1000*density*molarity/1000+(molarity*molarmass)
            return molarity
        print(f"molarity(몰농도)={result:.2f}M")
    elif choice == "0":
        print("계산기를 종료합니다")
        break
