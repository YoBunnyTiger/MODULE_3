def test(speed, time, distance=1000):
    if speed >= 50 and time <= 20 and distance == 1000:
        return f'Скорость: {speed} подходит, время: {time} подходит, расстояние: {distance} метров.'
    elif speed < 50 and time <= 20 and distance == 1000:
        return f'Скорость: {speed} меньше нужной, время: {time} подходит, расстояние: {distance} метров.'
    elif speed >= 50 and time > 20 and distance == 1000:
        return f'Скорость: {speed} подходит, время: {time} больше заданного, расстояние: {distance} метров.'
    elif speed >= 50 and time <= 20 and distance != 1000:
        return f'Скорость: {speed} подходит, время: {time} подходит, расстояние: {distance}м нарушает условие!'
    elif speed < 50 and time > 20 and distance == 1000:
        return (f'Скорость: {speed} меньше нужной, время: {time} '
                f'больше заданного, расстояние: {distance} метров.')
    elif speed >= 50 and time > 20 and distance != 1000:
        return (f'Скорость: {speed} подходит, время: {time} '
                f'больше заданного, расстояние: {distance}м нарушает условие!')
    elif speed < 50 and time <= 20 and distance != 1000:
        return (f'Скорость: {speed} меньше нужной, время: {time} '
                f'подходит, расстояние: {distance}м нарушает условие!')
    elif speed < 50 and time > 20 and distance != 1000:
        return (f'Скорость: {speed} меньше нужной, время: {time} '
                f'больше заданного, расстояние: {distance}м нарушает условие!')


# Решил перебрать все варианты
result1 = test(55, 15)
result2 = test(45, 20, 1000)
result3 = test(60, 22)
result4 = test(60, 18, 1200)
result5 = test(40, 22, 1000)
result6 = test(60, 22, 1200)
result7 = test(30, 15, 1200)
result8 = test(43, 22, 1200)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
