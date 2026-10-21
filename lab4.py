import numpy as np

def create_matrix(n: int, m: int, choice: int) -> np.ndarray:
    if choice == 1:
        a: int = int(input("От: "))
        b: int = int(input("До: "))
        return np.random.randint(a, b + 1, size=(n, m))
    return np.array([[int(input(f"Элемент [{i}][{j}]: ")) for j in range(m)] for i in range(n)])

def get_non_negative_row_products(arr: np.ndarray) -> list[tuple[int, np.integer]]:
    return [(i + 1, np.prod(arr[i])) for i in range(len(arr)) if min(arr[i]) >= 0]

def move_max_positive_to_top_left(arr: np.ndarray) -> np.ndarray | None:
    if np.max(arr) <= 0:
        return None
    res: np.ndarray = arr.copy()
    rows, cols = np.where(res == np.max(res))
    i_max, j_max = rows[0], cols[0]
    res[[0, i_max]] = res[[i_max, 0]]
    res[:, [0, j_max]] = res[:, [j_max, 0]]
    return res

if __name__ == "__main__":
    n: int = int(input("Введите количество строк: "))
    m: int = int(input("Введите количество столбцов: "))
    if n <= 0 or m <= 0:
        print("Размеры матрицы должны быть положительными")
    else:
        choice: int = int(input("Способ заполнения (1 - случайно, 2 - с клавиатуры): "))
        arr: np.ndarray = create_matrix(n, m, choice)
        print("\nИсходная матрица:\n", arr)

        row_products: list[tuple[int, np.integer]] = get_non_negative_row_products(arr)
        if row_products:
            for row_num, prod in row_products:
                print(f"1) Произведение в строке {row_num}: {prod}")
        else:
            print("1) Вычислить произведение невозможно")

        transformed: np.ndarray | None = move_max_positive_to_top_left(arr)
        if transformed is not None:
            print("2) Преобразованная матрица:\n", transformed)
        else:
            print("2) Перестановка невозможна")