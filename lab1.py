import math


def get_valid_x() -> float:
    x = float(input("input x (range [-1, 1)): "))
    if not (-1.0 <= x < 1.0):
        raise ValueError("bad range")
    return x


def get_valid_eps() -> float:
    eps = float(input("input e: "))
    if eps <= 0:
        raise ValueError("e must be > 0")
    return eps


def compute_taylor_ln(x: float, eps: float) -> tuple[float, int]:
    """Вычисляет сумму ряда Тейлора для ln(1 - x) и количество слагаемых."""
    taylor_sum: float = 0.0
    n: int = 1
    x_pow: float = x
    current_term: float = -x_pow / n

    while abs(current_term) >= eps:
        taylor_sum += current_term
        n += 1
        x_pow *= x
        current_term = -x_pow / n

    return taylor_sum, n - 1


def print_results(taylor_sum: float, standard_value: float, terms_count: int) -> None:
    error: float = abs(taylor_sum - standard_value)
    print(f"\nown realization: {taylor_sum}")
    print(f"library realization: {standard_value}")
    print(f"pogreshnost: {error}")
    print(f"count of addition: {terms_count}")


def main() -> None:
    try:
        x = get_valid_x()
        eps = get_valid_eps()
    except ValueError as err:
        msg = str(err) if str(err) in ("bad range", "e must be > 0") else "must be digit"
        print(msg)
        return

    taylor_sum, terms_count = compute_taylor_ln(x, eps)
    standard_value = math.log(1 - x)
    print_results(taylor_sum, standard_value, terms_count)


if __name__ == "__main__":
    main()