PRA2003 – Bacterial tracking analysis (Emma Schwarz)

It answers the three questions from the assignment:

What are the average counts of each strain, and their statistical uncertainties?
Is there an asymmetry between the normal (wild-type) strain and its variant? Quantify it.
Is there an asymmetry as a function of momentum? Quantify it.
All 10 data sets were used (output-Set1.txt to output-Set10.txt), each set including about 500 000 events. Each event is one simulated experiment and lists every bacterium seen in it, as px py pz code.

Events with 0 bacteria were left excluded, since nothing was observed, leaving 4,617,993 events in total, about 462,000 per set.

The files contain 38 different codes. Only the 12 in the table below are the strains we're studying. All other codes are background and are left out of every result here.

Code Strain Code Variant 211 E. coli WT −211 E. coli mutant 321 Bacillus subtilis WT −321 B. subtilis mutant 2212 Pseudomonas aeruginosa WT −2212 P. aeruginosa, antibiotic-resistant 3122 Streptococcus pneumoniae −3122 Capsule-deficient S. pneumoniae 3312 Mycobacterium tuberculosis −3312 Drug-resistant M. tuberculosis 3334 Salmonella enterica −3334 Salmonella mutant

                            METHODS
The subsampling method was used, treating each 10 data sets as as one independent subsample.

PART1: each data file is read in chunksso a file never has to fit in memory all at once. It works out an average number per event in that file for every code. The results for all 10 files are saved to sub_sample_results.csv.

PART2: the 10 subsamples are combined. The final average consists of the weighted mean of the 10 subsample averages. The uncertainty is the standard deviation of the 10 sub-sample averages. The weighted mean and the plain mean of the 10 values agree to the 4th decimal place, so the weighting doesn't change anything.

ASYMMETY SCRIPT: each wild type is compared to it's variant (set by set) --> Question 2

                    Signifance criterion --> 3σ
A difference that was smaller than 3 standard deviations --> consistent with 0 A difference of 3σ or more --> counted as real, statistically significant asymmetry

                Question 1 – Average count per event

        Code	  Strain	                     Average per event ± SD
        211	    E. coli WT	                         19.949 ± 0.033
        −211	E. coli mutant	                     19.917 ± 0.032
        321	    B.subtilis WT	                     2.5091 ± 0.0048
        −321	B. subtilis mutant	                 2.5035 ± 0.0055
        2212	P. aeruginosa WT	                 1.2080 ± 0.0019
        −2212	P. aeruginosa, antibiotic-resistant	 1.1842 ± 0.0024
        3122	S. pneumoniae	                     0.2766 ± 0.0011
        −3122	Capsule-deficient S. pneumoniae      0.2717 ± 0.0010
        3312	M. tuberculosis	                     0.03944 ± 0.00028
        −3312	Drug-resistant M. tuberculosis	     0.03900 ± 0.00040
        3334	Salmonella enterica	                 0.00119 ± 0.00004
        −3334	Salmonella mutant	                 0.00115 ± 0.00005
Together these 12 strains make up about 48 bacteria per event. E. coli is by far the most common, at about 20 per event for each of WT and mutant. Salmonella is the rarest, at roughly one cell per 1,000 events.

Question 2 – Is there an asymmetry between wild type and variant?

 How were they compared:
    The differnces was taken for each pair 

    --> Δ = (WT average) − (variant average) 

    seperately (in each of the 10 sets). The mean of the 10 differences as the results as well as their standard deviation as the uncertainty 
    We also give the normalised asymmetry

    A = (WT − variant) / (WT + variant)

    worked out the same way, so pairs with very different abundances can be compared.
    Why set by set? 
        The numbers show that WT and variant rise and fall together from one set to the next. In set 1, for example, E. coli WT and mutant are both high (20.010 and 19.982). In set 9 they are both low (19.912 and 19.889). 
        Comparing within each set --> cancels out that shared fluctuation + only the real WT–variant difference is left.
If you instead subtract the two final averages and combine their uncertainties in quadrature, that shared fluctuation gets counted as noise. For E. coli that approach gives only 0.7σ, even though the WT is ahead of the mutant in all 10 sets.


                                                RESULTS
Pair	                     Δ (per event)	             A	        Significance	Sets with WT > variant	        Result
E. coli(±211)               0.0323 ± 0.0045	      0.00081 ± 0.00011	       7.2σ	        10 / 10                     Significant
B. subtilis (±321)	        0.0057 ± 0.0033	      0.0011 ± 0.0007	       1.7σ	        9 / 10	                    Consistent with 0
P. aeruginosa (±2212)	    0.0239 ± 0.0024	      0.0100 ± 0.0010	       10.1σ	    10 / 10	                    Significant
S. pneumoniae (±3122)	    0.00490 ± 0.00058	  0.0089 ± 0.0011	       8.5σ	        10 / 10	                    Significant
M. tuberculosis (±3312)	    0.00044 ± 0.00049	  0.006 ± 0.006	           0.9σ         9  / 10	                    Consistent with 0
Salmonella (±3334)	        0.00004 ± 0.00007	  0.016 ± 0.029	           0.5σ	        6 / 10	                    Consistent with 0

Answer:
There is an asymmetry but only in 3 of the 6 pairs and in each one the wild type is the more common one.

- P. aeruginosa: clear asymmetry (10.1σ) --> wild typs = about 2% more common than antibiotic resistant one (ahead in all 10 sets) 
    --> Strongest result

- S. pneumoniae: clear asymmetry (8.5σ) --> normal strain = about 1.8% more common than capsule-deficient variant (in all 10 sets)

- E. coli: small but real asymmetry (7.2σ) --> Tiny effect : WT 0.16% more common: it is still far above 3σ and holds in every set. E. coli is so abundant that    even a very small difference can be measured

- B. subtilis: no significant asymmetry (1.7σ) --> The WT is slightly ahead in 9 of the 10 sets : hints at something, but at 1.7σ it is well below our 3σ criterion -->  with the data it is consistent with no asymmetry

- M. tuberculosis and Salmonella: no significant asymmetry (0.9σ and 0.5σ)-->  These strains are rare, so their uncertainties are large compared with any difference. We can't rule out a small asymmetry: with 3σ we could only have detected one bigger than about 2% for M. tuberculosis and about 9% for Salmonella.
The three significant results clear 3σ even with these larger errors --> the conclusion that they are real asymmetries holds.
