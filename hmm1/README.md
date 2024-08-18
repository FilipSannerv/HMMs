# HMM1

### Calculates the probability to observe a certain emission (observation) sequence given a HMM model.

Uses the <strong>Forward Algorithm</strong> to compute the probability of observing a given sequence using the HMM defined by the transition matrix, emission matrix, and initial state probabilities.

Example input:
```
4 4 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.8 0.1 0.1 0.0 
4 4 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.1 0.0 0.0 0.9 
1 4 1.0 0.0 0.0 0.0 
8 0 1 2 3 0 1 2 3 
```

Expected output:
```
0.090276 
```

```
python hmm1.py < sample.in
```