import numpy as np

def count_sign_changes(arr: np.ndarray) -> int:
    return np.count_nonzero(np.diff(arr >= 0))

def prod_between_zeros(arr: np.ndarray) -> np.integer | None:
    zeros: np.ndarray = np.where(arr == 0)[0]
    if len(zeros) >= 2 and zeros[1] - zeros[0] > 1:
        return np.prod(arr[zeros[0] + 1 : zeros[1]])
    return None

def sort_even_odd(arr: np.ndarray) -> np.ndarray:
    evens: np.ndarray = arr[arr % 2 == 0]
    odds: np.ndarray = arr[arr % 2 != 0]
    return np.concatenate((evens, odds))

if __name__ == "__main__":
    n: int = int(input("Введите количество элементов: "))
    arr: np.ndarray = np.random.randint(-10, 11, size=n)
    print("\nИсходный массив:", arr)

    print(f"1) Количество перемен знака: {count_sign_changes(arr)}")

    prod: np.integer | None = prod_between_zeros(arr)
    if prod is not None:
        print(f"2) Произведение: {prod}")
    else:
        print("2) Вычислить произведение невозможно")

    print("3) Преобразованный массив:", sort_even_odd(arr))