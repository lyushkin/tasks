s = 'orange strawberry barley gooseberry apple apricot barley currant orange' \
    ' melon pomegranate banana banana orange barley apricot plum grapefruit' \
    ' banana quince strawberry barley grapefruit banana grapes melon strawberry' \
    ' apricot currant currant gooseberry raspberry apricot currant orange lime' \
    ' quince grapefruit barley banana melon pomegranate barley banana orange' \
    ' barley apricot plum banana quince lime grapefruit strawberry gooseberry' \
    ' apple barley apricot currant orange melon pomegranate banana banana' \
    ' orange apricot barley plum banana grapefruit banana quince currant' \
    ' orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
slovar = {}

for i in s:
    slovar[i] = slovar.get(i, 0) + 1

maximum = max(slovar.values())

lst = [i for i in slovar if slovar[i] == maximum]
lst.sort()
print(lst[0])