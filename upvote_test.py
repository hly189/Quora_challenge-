
def subrange(upvote):
	
	non_increasing = 0
	non_decreasing = 0
	count_increasing = 0
	count_decreasing = 0

	i = 1

	while i < len(upvote): 
		previous = upvote[i-1]
		current = upvote[i]
		
		if current < previous: 
		    if count_increasing == 0:
		        count_increasing = 1
		    else: 
		    	count_increasing = count_increasing + 1
		    non_increasing = non_increasing + count_increasing 
		    count_decreasing = 0
		elif current > previous: 
		    if count_decreasing == 0:
		        count_decreasing = 1
		    else: 
		    	count_decreasing = count_decreasing + 1
		    non_decreasing = non_decreasing + count_decreasing 
		    count_increasing = 0
		
		else: 
			if count_increasing ==0: 
				count_increasing = 1
				count_decreasing = count_decreasing + 1
			if count_decreasing == 0: 
				count_decreasing = 1
				count_increasing = count_increasing + 1
			non_increasing = non_increasing + count_increasing
			non_decreasing = non_decreasing + count_decreasing

		i = i + 1
	return non_decreasing - non_increasing


(n, k) = map(int, raw_input().split())
upvote = map(int, raw_input().split())

i = 0
while i < (n-k+1): 
	print subrange(upvote[i:i+k])
	i = i +1
