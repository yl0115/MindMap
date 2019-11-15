
import string,random
goal = ''.join(random.sample(string.ascii_letters+string.digits,8))
goal = goal.lower()
print(goal)
