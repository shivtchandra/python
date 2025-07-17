#Here we follow the dynamic programming approach to solve this question
def climbing(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  # we create a long enough dp to store the nums
  dp = [0] * (n+1)
  dp[1]=1
  dp[2]=2
  # As we cant directly find the num we want we iterate through the nums as we dont have those values starting from 3 .
  # So in this process we get the ans for all the nums which are less than the given N value.
  for num in range(3,n+1):
    dp[num] = dp[num-1]+dp[num-2]
  # we have a full length array . so we just print the value which we want annd in this question case its n
  return dp[n]
