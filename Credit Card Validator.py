
# condition valid card

card_number = input("Enter a credit card #: " )
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

card_number = card_number[::-1]

print(card_number)
sum_odd_digits = 0
sum_even_digits = 0

#step 2 cộng ở vị trí lẻ
for x in card_number[::2]:
    sum_odd_digits += int(x)
#step 2 nhân đôi vị trí chẵn
# ví dụ ra 16 thì 1 + 6 = 7 cộng dồn vào sum_even
for x in card_number[1 :: 2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += int(x)

total = sum_odd_digits + sum_even_digits
if total % 10 == 0:
    print("valid")
else:
    print("INVALID")

