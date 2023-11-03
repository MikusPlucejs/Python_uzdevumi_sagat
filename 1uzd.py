"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""
class RIDE:
    def __init__(self):
        self.roma_sk={
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX', 
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result

skaitlis=2023

kk=RIDE()

romieshu=kk.to_roman(skaitlis)

print(f'{skaitlis} ar romiešu cipariem ir {romieshu}.')