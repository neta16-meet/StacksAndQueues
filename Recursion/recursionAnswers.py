def reverse(q):
    if q.size() == 0:
        return None
    if q.size() == 1:
        return q
    else:
        value = q.dequeue()
        q = reverse(q)
        q.enqueue(value)
        return q

def hanoiTowers(discNum, fromPole, withPole, toPole):
	if discNum == 1:
		print("move from " + fromPole + " to " + toPole)
	else:
		hanoiTowers(discnum-1, fromPole, withPole, toPole)
		print("move from " + fromPole + " to " + toPole)
		hanoiTowers(discnum-1, withPole, fromPole, toPole)
