import argparse



# Class definition for Hidden Markov Model (HMM)
# Do not make any changes to this class
# You are not required to understand the inner workings of this class
class HMM:
	"""
		Arguments:

		states: Sequence of strings representing all states
		vocab: Sequence of strings representing all unique observations
		trans_prob: Transition probability matrix. Each cell (i, j) contains P(states[j] | states[i])
		obs_likelihood: Observation likeliood matrix. Each cell (i, j) contains P(vocab[j] | states[i])
		initial_probs: Vector representing initial probability distribution. Each cell i contains P(states[i] | START)
	"""
	def __init__(self, states, vocab, trans_prob, obs_likelihood, initial_probs):
		self.states = states
		self.vocab = vocab
		self.trans_prob = trans_prob
		self.obs_likelihood = obs_likelihood
		self.initial_probs = initial_probs

    # Function to return transition probabilities P(q1|q2)
	def tprob(self, q1, q2):
		if not (q1 in self.states and q2 in ['START'] + self.states):
			raise ValueError("invalid input state(s)")
		q1_idx = self.states.index(q1)
		if q2 == 'START':
			return self.initial_probs[q1_idx]
		q2_idx = self.states.index(q2)
		return self.trans_prob[q2_idx][q1_idx]
    
    # Function to return observation likelihood P(o|q)
	def oprob(self, o, q):
		if not o in self.vocab:
			raise ValueError('invalid observation')
		if not (q in self.states and q != 'START'):
			raise ValueError('invalid state')
		obs_idx = self.vocab.index(o)
		state_idx = self.states.index(q)
		return self.obs_likelihood[obs_idx][state_idx]
	
	# Function to retrieve all states
	def get_states(self):
		return self.states.copy()


# Function to initialize an HMM using the weather-icecream example in Figure 6.3 (Jurafsky & Martin v2)
# Do not make any changes to this function
# You are not required to understand the inner workings of this function
def initialize_icecream_hmm():
	states = ['HOT', 'COLD']
	vocab = ['1', '2', '3']
	tprob_mat = [[0.7, 0.3], [0.4, 0.6]]
	obs_likelihood = [[0.2, 0.5], [0.4, 0.4], [0.4, 0.1]]
	initial_prob = [0.8, 0.2]
	hmm = HMM(states, vocab, tprob_mat, obs_likelihood, initial_prob)
	return hmm


# Function to implement viterbi algorithm
# Arguments:
# hmm: An instance of HMM class as defined in this file
# obs: A string of observations, e.g. ("132311")
# Returns: seq, prob
# Where, seq (list) is a list of states showing the most likely path and prob (float) is the probability of that path
# Note that seq sould not contain 'START' or 'END' and In case of a conflict, you should pick the state at lowest index
def viterbi(hmm, obs):
	# [YOUR CODE HERE]
	"""use the HMM class and look at viterby pseudocode to finisih this function."""

	
    return ['HOT', 'COLD'], 0.2


# Use this main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from terminal as: python3 q3.py
# It should produce the following output:
# 		  $python3 q3.py
#         P(HOT|COLD) = 0.4
#         P(COLD|START) = 0.2
#         P(1|COLD) = 0.5
#         P(2|HOT) = 0.4
#         Path: ['HOT', 'COLD']
#         Probability: 0.2

def main():
	# We can initialize our HMM using initialize_icecream_hmm function
	hmm = initialize_icecream_hmm()

	# We can retrieve all states as
	print("States: {0}".format(hmm.get_states()))

	# We can get transition probability P(HOT|COLD) as
	prob = hmm.tprob('HOT', 'COLD')
	print("P(HOT|COLD) = {0}".format(prob))

	# We can get transition probability P(COLD|START) as
	prob = hmm.tprob('COLD', 'START')
	print("P(COLD|START) = {0}".format(prob))

	# We can get observation likelihood P(1|COLD) as
	prob = hmm.oprob('1', 'COLD')
	print("P(1|COLD) = {0}".format(prob))

	# We can get observation likelihood P(2|HOT) as
	prob = hmm.oprob('2', 'HOT')
	print("P(2|HOT) = {0}".format(prob))

	# You should call the viterbi algorithm as
	path, prob = viterbi(hmm, "13213")
	print("Path: {0}".format(path))
	print("Probability: {0}".format(prob))


################ Do not make any changes below this line ################
if __name__ == '__main__':
    exit(main())