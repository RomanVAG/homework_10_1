def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по значению ключа 'state'.
    """
    list_1 = []
    for transaction in transactions:
        if transaction.get("state") == state:
            list_1.append(transaction)
    return list_1


def sort_by_date(transactions: list[dict], reverse=True) -> list[dict]:
    """
    Фильтрует список операций по значению ключа 'date'.
    """
    sorted_list = sorted(transactions, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
