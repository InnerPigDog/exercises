class Luhn:
    """Implementation of Luhn Algorithm. Used for identification numbers. 
    """
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if not self.card_num.isdigit():
            return False
        if len(self.card_num) < 2:
            return False 
        return self.luhn_algo()
        
    def luhn_algo(self):
        sum_result = 0
        for i, digit in enumerate(self.card_num[::-1]): 
            digit = int(digit)
            if i % 2 != 0: 
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum_result += digit
        return sum_result % 10 == 0