# HMM2

Calculates the most likely sequence of hidden states that the system moves through given an emission sequence and HMM model using the <strong>Viterbi algorithm</strong>.

<strong>Output:</strong> Most probable sequence of states as zero-based indicies.

Example input:
```
4 4 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.8 0.1 0.1 0.0 
4 4 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.1 0.0 0.0 0.9 
1 4 1.0 0.0 0.0 0.0 
4 1 1 2 2 
```
Expected output:
```
0 1 2 1 
```
```
python hmm2.py < sample.in
```