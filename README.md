# Hidden Markov Models (HMM) Algorithms

## Implementations of various calculations on HMMs 

My solutions for HMM part of course in Artificial Intelligence. Implementations are done from scratch without using any external libraries such as numpy.

- HMM1 - Probability of observation sequence
- HMM2 - Estimate sequence of states
- HMM3 - Estimate model parameters

A HMM consists of three primary components:

- Transition matrix (A)
    - Described the probabilities of transitioning from one state to another
- Emission matrix (B)
    - Probability of observing each possible emission (output) given current state
- Initial state probability (T)
    - Probability of starting in each state (t=0), given as a vector.


<strong>Input format:</strong> Each matrix is given on a separate line with the number of rows and columns followed by the matrix elements.

<strong>Input:</strong> HMM (Transition matrix, emission matrix, initial state probability distribution) and a sequence of emissions.

Example input:
```
4 4 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.8 0.1 0.1 0.0 
4 4 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.1 0.0 0.0 0.9 
1 4 1.0 0.0 0.0 0.0 
8 0 1 2 3 0 1 2 3 
```
