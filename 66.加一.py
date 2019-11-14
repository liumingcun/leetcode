class Solution:
    def plusOne(self, digits) :
        str_ = ''
        for i in range(len(digits)):
            str_ += str(digits[i])
        int_ = int(str_) +1
        str_ = str(int_)
        new_digits = []
        for i in range(len(str_)):
            new_digits.append(int(str_[i]))
        return new_digits