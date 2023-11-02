class Solution:
    def palindrome_num(self,number):
        self.number = number
        self.p_number = int(str(number)[::-1])
        if int(self.number) == int(self.p_number):
            print(f'{int(self.number)} is a palindrome number')
        else:
            print(f'{int(self.number)} is not a palindrome number')


palindrome = Solution()
palindrome.palindrome_num(122)