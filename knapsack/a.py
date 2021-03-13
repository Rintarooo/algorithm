n, W = list(map(int, input().split()))
vlis, wlis = [], []
for i in range(n):
	w, v = list(map(int, input().split()))
	vlis.append(v)
	wlis.append(w)

# return max value using from 0th the item to "i"th one
# under jkg  
def recursive(i, j):
	if i == -1:
		v = 0
		return v
	
	if j < wlis[i]:
		v = recursive(i-1, j)
	else:
		v1 = recursive(i-1, j-wlis[i])+vlis[i]
		v2 = recursive(i-1, j)
		v = max(v1, v2)
	print(i, j, v)
	return v

def func_dp():
	global dp
	# dp = [[] _ for i in range(n+1)]
	dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
	# dp[:,0] = dp[0,:] = 0
	vlis.insert(0,0)
	wlis.insert(0,0)
	print("insert 0: ", wlis, vlis)

	for i in range(n):
		for j in range(W+1):
			if j < wlis[i+1]:
				dp[i+1][j]= dp[i][j]
			else:
				v1 = dp[i][j-wlis[i+1]]+vlis[i+1]
				v2 = dp[i][j]
				# use i+1 item or not use
				dp[i+1][j] = max(v1, v2)
	print(dp)
	print("output: ", dp[-1][-1])


if __name__ == '__main__':
	print("wlis, vlis: ", wlis, vlis)
	i = n-1
	j = W

	# print("output: ", recursive(i, j))
	func_dp()

