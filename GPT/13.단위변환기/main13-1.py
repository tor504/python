def main():
    print("단위 변환 프로그램")
    value = float(input("변환할 값 입력: "))
    from_unit = input("현재 단위 입력: ")
    to_unit = input("변환할 단위 입력: ")

    result = perform_conversion(value, from_unit, to_unit)
    print(f"{value} {from_unit}은(는) {result} {to_unit}입니다.")

def perform_conversion(value, from_unit, to_unit):
    # 단위 변환 딕셔너리
    units = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'inch': 0.0254
    }

    # 변환 수행
    result = value * units[from_unit] / units[to_unit]
    return result

if __name__ == "__main__":
    main()