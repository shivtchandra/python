# so here we are asked to calculate the biggest subsequence possible in a given array.
# Another condition is that no value shhould repeat two times in the subsequence .
# Hash Set is the best way to Tackle this problem .

seen = set()
j = 0 #The left index
summ = 0
maxx = 0

for i in range(len(nums)):
  if nums[i] in seen:
#Here we check if the new number is already present in the seen set and if thats the case , we delete the left most element from the sum and also from the hash set.
# Now the code will again check for this condition and if it still True then again the left most element will get deleted untill the condition turns into False.
# We can either reduce the right or left , But we choose to remove left bcos we need to explore the right part of array and it needs to be in a sequence.
    summ -= nums[j]
    seen.remove(nums[j])
# If the if loop doesnt apply they will get added to the sum and the Hashset .
  seen.add(nums[i])
  summ += nums[i]
  maxx = max(summ,maxx)

return maxx
