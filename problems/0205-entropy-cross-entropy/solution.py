import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
	"""
	Compute entropy of P and cross-entropy between P and Q.
	
	Args:
		P: True probability distribution
		Q: Predicted probability distribution
	
	Returns:
		Tuple of (entropy H(P), cross-entropy H(P,Q))
	"""
	# Your code here
	hp = 0
	hpq = 0
	for i in range(len(P)):
		if P[i] == 0:
			continue
		hp += P[i]*np.log(P[i])
		hpq += P[i]*np.log(Q[i])
	return (-hp, -hpq)