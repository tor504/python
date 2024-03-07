def save_exchange_rates(exchange_rates, filename):
    """
    환율 정보를 텍스트 파일로 저장하는 함수.

    Args:
    - exchange_rates (dict): 환율 정보를 담은 딕셔너리.
    - filename (str): 저장할 파일의 이름.
    """
    with open(filename, 'w') as file:
        for currency, rate in exchange_rates.items():
            file.write(f"{currency}:{rate}\n")

def load_exchange_rates(filename):
    """
    텍스트 파일에서 환율 정보를 읽어오는 함수.

    Args:
    - filename (str): 읽어올 파일의 이름.

    Returns:
    - exchange_rates (dict): 환율 정보를 담은 딕셔너리.
    """
    exchange_rates = {}
    with open(filename, 'r') as file:
        for line in file:
            currency, rate = line.strip().split(':')
            exchange_rates[currency] = float(rate)
    return exchange_rates

def convert_currency(amount, base_currency, target_currency, exchange_rates):
    """
    주어진 금액을 기준 통화에서 대상 통화로 변환하는 함수.

    Args:
    - amount (float): 변환할 금액.
    - base_currency (str): 기준 통화 코드.
    - target_currency (str): 대상 통화 코드.
    - exchange_rates (dict): 환율 정보를 담은 딕셔너리.

    Returns:
    - converted_amount (float 또는 None): 변환된 금액. 변환에 실패한 경우 None을 반환.
    """
    base_rate = exchange_rates.get(base_currency)
    target_rate = exchange_rates.get(target_currency)
    if base_rate is not None and target_rate is not None:
        converted_amount = amount * (target_rate / base_rate)
        return converted_amount
    else:
        print("환율 정보를 찾을 수 없습니다.")
        return None

# 예시 환율 정보
example_exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.72,
    'JPY': 109.24,
    # 추가적인 환율 정보를 필요에 따라 추가할 수 있습니다.
}

# 환율 정보 저장 및 로드 예시
filename = 'exchange_rates.txt'
save_exchange_rates(example_exchange_rates, filename)
loaded_exchange_rates = load_exchange_rates(filename)

# 사용자 입력 받기
amount = float(input("변환할 금액을 입력하세요: "))
base_currency = input("변환할 기준 통화를 입력하세요 (예: USD): ").upper()
target_currency = input("변환할 대상 통화를 입력하세요 (예: EUR): ").upper()

# 환율 변환
converted_amount = convert_currency(amount, base_currency, target_currency, loaded_exchange_rates)
if converted_amount is not None:
    print(f"{amount} {base_currency}은(는) {converted_amount:.2f} {target_currency}입니다.")
else:
    print("환율 변환에 실패했습니다.")