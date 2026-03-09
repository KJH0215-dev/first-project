while True:
    print("=======농도 희석 계산기를 실행합니다.=======")
    print("1. 희석 계산기_농도")
    print("2. 희석 계산기_부피")
    print("0. 계산 종료")
    
    choice = input("번호 선택")

    if choice == "1":
        concentration_1 = float(input("희석 전 용액 농도(M: 몰농도)를 입력하세요:"))
        volume_1 =float(input("희석 전 부피(L: 리터)를 입력하세요:"))
        volume_2 = float(input("희석 용액의 부피(L: 리터)를 입력하세요:"))
        def 희석계산기_농도(concentration_1, volume_1, volume_2):
            concentration_2 = (concentration_1*volume_1)/(volume_2)
            return concentration_2
        result = 희석계산기_농도(concentration_1, volume_1, volume_2)
        print(f"변화 농도={result:.3f}M")
    elif choice == "2":
        concentration_1 = float(input("희석 전 용액 농도(M: 몰농도)를 입력하세요:"))
        volume_1 = float(input("희석 전 용액의 부피(L: 리터)를 입력하세요:"))
        concentration_2 = float(input("희석 용액의 농도(M: 몰농도)를 입력하세요:"))
        def 희석계산기_부피(concentration_1, volume_1, concentration_2):
            volume_2 = (concentration_1*volume_1)/(concentration_2)
            return volume_2
        result = 희석계산기_부피(concentration_1, volume_1, concentration_2)
        print(f"변화 부피={result:.3f}L")
    elif choice == "0":
        print("계산을 종료합니다.")
        break
        