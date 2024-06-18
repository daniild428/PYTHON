price_rubles = int(input("Введите цену пирожка в рублях: "))
price_kopeks = int(input("Введите цену пирожка в копейках: "))
quantity = int(input("Введите количество пирожков: "))


total_price = price_rubles * quantity + price_kopeks * quantity // 100
total_kopeks = price_kopeks * quantity % 100

print(f"Сумма к оплате: {total_price} руб. {total_kopeks} коп.")