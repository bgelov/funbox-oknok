import re

def main():
    # Искомый статус
    status = "NOK"
    # Словарь для результата
    counting_dict = {}
    # Regex для даты в нашем формате
    valid_date = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$')

    with open('events.log','r') as f:
        for line in f.readlines():
            # Проверка строки на соответствие искомой
            if status in line:
                split_line = line.split()
                if len(split_line) == 3 and split_line[2] == status:
                    # Если строка подходит, склеиваем и проверяем валидность даты
                    event_date = f"{split_line[0][1::]} {split_line[1][0:5]}"
                    if valid_date.match(event_date):

                        # Если дата валидна, добавляем в словарь
                        if event_date not in counting_dict:
                            counting_dict[event_date] = 0
                        counting_dict[event_date] += 1

    # Вывод результата
    print(counting_dict)

    for key in counting_dict.keys():
        print(f"{key} - {counting_dict[key]}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
