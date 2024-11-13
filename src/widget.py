def mask_account_card(info):
    card_types = ["Visa", "Maestro", "MasterCard"]
    # Проверяем тип карты или счета
    for card_type in card_types:
        if info.startswith(card_type):
            num = info.split()[-1]  # получаем номер карты
            return f"{' '.join(info.split()[:-1])} {num[:4]} {num[4:6]}** **** {num[-4:]}"

    # Если это счет
    if info.startswith("Счет"):
        num = info.split()[-1]
        return f"Счет **{num[-4:]}"

    return "Неизвестный тип информации"
