import pandas as pd


def time_to_seconds(time_str):
    mas_time = []
    for time in time_str:
        print(time)
        if (' сек.' in time):
            minutes, seconds = map(int, time.replace(' мин.', '').replace(' сек.', '').split())
            mas_time.append(minutes * 60 + seconds)
        else:
            hours, minutes = map(int, time.replace(' час.', '').replace(' ч.', '').replace(' мин.', '').split())
            mas_time.append(hours * 60 * 60 + minutes * 60)


    return pd.Series(mas_time)

data = pd.read_csv("7 - 1.csv")

# index_names = data[data.get("Фамилия", "") == "Среднее по группе"].index
# index_names1 = data[data.get("Фамилия", "") == "Общее среднее"].index
# data.drop(index_names, inplace=True)
# data.drop(index_names1, inplace=True)
data.drop([len(data) - 1, len(data) - 2], inplace=True)
# print(data)

result_data = data[(data.get("Оценка/10,00", "") > "7,00")].reset_index()

result_data.sort_values(by=["Фамилия"], inplace=True)
print(result_data, "\n")

result_time = time_to_seconds(result_data.get("Затраченное время", ""))
avg_time = result_time.mean()
# result_time = result_data[time_to_seconds(result_data.get("Затраченное время", ""))].mean()
print()
print(result_time, "\n")
print("Среднее время выполнения работы: ", avg_time, " секунд.")

