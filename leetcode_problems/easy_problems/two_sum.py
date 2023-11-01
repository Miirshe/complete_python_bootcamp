class Solution:
    def twoSum(self,nums , target):
        self.nums = nums
        self.target = target
        self.get_target = {}
        for self.i ,self.num in enumerate(self.nums):
            self.set_target = self.target - self.num
            if self.set_target in self.get_target:
                return  [self.get_target[self.set_target],self.i]
            self.get_target[self.num] = self.i
        else:
            print('The target value not found ! ')






get_solution = Solution()
set_solution = get_solution.twoSum([3,2,4],6)
print(f'The target : {set_solution}')