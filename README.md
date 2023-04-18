# Read me for Rhythmic cortex 

## Demand library: 

### For temporal de-correlation and intrinsic frequency:
  Numpy; Scipy


### For clustering analysis:
  nitime; tslearn
  
## Included files

1. Code snippet for running the temporal de-correlation and harvest the intrinsic frequency. 
      
   Note here, we did not provide the source HCP-900 data, but supply the pre-processed subject-level, Power parcellation masked Npy file.
   It stores over 400 subjs data that are Power et al (2011) masked, creating a [443, 1200, 264] data matrix for the input.
   
2. Code snippet for running clustering analysis to break  the spectrum (264) into meaningful 6 clusters


