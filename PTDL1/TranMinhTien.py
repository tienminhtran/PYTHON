def calculate_mean(arr):
    return sum(arr) / len(arr)

def calculate_mode(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    mode = [key for key, value in frequency.items() if value == max(frequency.values())]
    return mode

def calculate_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        median = sorted_arr[n // 2]
    return median

def calculate_quartiles(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    q1 = calculate_median(sorted_arr[:n // 2])
    q2 = calculate_median(sorted_arr)
    q3 = calculate_median(sorted_arr[(n + 1) // 2:])
    return q1, q2, q3

def calculate_variance(arr):
    mean = calculate_mean(arr)
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)
    return variance

def calculate_standard_deviation(arr):
    return calculate_variance(arr) ** 0.5

def calculate_range(arr):
    return max(arr) - min(arr)

def main():
    while True:
        try:
            n = int(input("Nhập số lượng phần tử trong mảng: "))
            arr = list(map(float, input("Nhập mảng (các phần tử cách nhau bằng dấu cách): ").split()))

            if len(arr) != n:
                raise ValueError("Số lượng phần tử không khớp với số lượng đã nhập.")

            print("\nChọn một trong các tính toán sau:")
            print("1. Trung bình (Mean)")
            print("2. Yếu vị (Mode)")
            print("3. Trung vị (Median)")
            print("4. Tứ phân vị (Quartiles)")
            print("5. Phương sai (Variance)")
            print("6. Độ lệch chuẩn (Standard Deviation)")
            print("7. Khoảng biến thiên (Range)")
            print("0. Thoát")

            choice = int(input("Nhập lựa chọn của bạn (0-7): "))

            if choice == 0:
                print("Chương trình kết thúc.")
                break
            elif choice == 1:
                result = calculate_mean(arr)
                print(f"Trung bình (Mean): {result}")
            elif choice == 2:
                result = calculate_mode(arr)
                print(f"Yếu vị (Mode): {result}")
            elif choice == 3:
                result = calculate_median(arr)
                print(f"Trung vị (Median): {result}")
            elif choice == 4:
                quartiles = calculate_quartiles(arr)
                print(f"Tứ phân vị (Quartiles): {quartiles}")
            elif choice == 5:
                result = calculate_variance(arr)
                print(f"Phương sai (Variance): {result}")
            elif choice == 6:
                result = calculate_standard_deviation(arr)
                print(f"Độ lệch chuẩn (Standard Deviation): {result}")
            elif choice == 7:
                result = calculate_range(arr)
                print(f"Khoảng biến thiên (Range): {result}")
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError as e:
            print(f"Lỗi: {e}")
main()
