PRA2003 – Bacterial tracking analysis (Emma Schwarz)

It answers the three questions from the assignment:

1) What are the average counts of each strain, and their statistical uncertainties?
2) Is there an asymmetry between the normal (wild-type) strain and its variant? Quantify it.
3) Is there an asymmetry as a function of momentum? Quantify it.

All 10 data sets were used (output-Set1.txt to output-Set10.txt), each set including about 500 000 events. Each event is one simulated experiment and lists every bacterium seen in it, as px py pz code.

Events with 0 bacteria were left excluded, since nothing was observed, leaving 4,617,993 events in total, about 462,000 per set.

The files contain 38 different codes. Only the 12 in the table below are the strains we're studying. All other codes are background and are left out of every result here.

Code	Strain	                     Code	Variant
211	     E. coli WT	                 −211	E. coli mutant
321	     Bacillus subtilis WT	     −321	B. subtilis mutant
2212	 Pseudomonas aeruginosa WT	−2212	P. aeruginosa, antibiotic-resistant
3122	 Streptococcus pneumoniae	−3122	Capsule-deficient S. pneumoniae
3312	 Mycobacterium tuberculosis	−3312	Drug-resistant M. tuberculosis
3334	 Salmonella enterica	    −3334	Salmonella mutant

                                METHODS

The subsampling method was used, treating each 10 data sets as as one independent subsample.

PART1: each data file is read in chunksso a file never has to fit in memory all at once. It works out an average number per event in that file for every code. The results for all 10 files are saved to sub_sample_results.csv.

PART2: the 10 subsamples are combined. The final average consists of the weighted mean of the 10 subsample averages. The uncertainty is the standard deviation of the 10 sub-sample averages. The weighted mean and the plain mean of the 10 values agree to the 4th decimal place, so the weighting doesn't change anything.

ASYMMETY SCRIPT: each wild type is compared to it's variant (set by set)
--> Question 2

                        Signifance criterion --> 3σ

A difference that was smaller than 3 standard deviations --> consistent with 0
A difference of 3σ or more --> counted as real, statistically significant asymmetry

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

                            Question 3 – Asymmetry as a function of momentum

For every bacterium the size of its momentum was calculated, |p| = √(px² + py² + pz²), in units of 10⁻²⁰ kg·m/s. 
 The bacteria were sorted into 5 momentum bins, with edges chosen so that each bin holds about the same number of bacteria. The same edges were used for every pair and every set.

In each set and each bin A was computed --> A = (N_WT − N_mutant)
As in Questions 1 and 2, the result is the mean of the 10 sets and the uncertainty is the standard deviation. The counts in the table are summed over all 10 sets.

                                            Results

Strain	              Momentum range	   Count WT	   Count mutant	        Asymmetry A
E. coli	                0 – 0.654	      18,403,119	18,400,222	     0.00030 ± 0.00082
E. coli	                0.654 – 1.32	  17,645,292	17,621,868	     0.00066 ± 0.00053
E. coli	                1.32 – 2.68	      19,555,864	19,531,055	     0.00066 ± 0.00041
E. coli	                2.68 – 5.88	      21,392,457	21,345,164	     0.00109 ± 0.00031
E. coli	                   > 5.88	      15,129,956	15,079,233	     0.00281 ± 0.00361
B. subtilis	            0 – 0.654	      1,240,435	    1,239,322	     0.00096 ± 0.00214
B. subtilis	            0.654 – 1.32	  2,020,151	    2,021,862	    −0.00023 ± 0.00194
B. subtilis	            1.32 – 2.68	      2,611,998	    2,611,426	     0.00008 ± 0.00127
B. subtilis	            2.68 – 5.88       3,021,488	    3,010,945	     0.00164 ± 0.00085
B. subtilis	               > 5.88	      2,693,155	    2,677,391	     0.00152 ± 0.00479
P. aeruginosa	        0 – 0.654	      337,477	    331,758	         0.00820 ± 0.00400
P. aeruginosa	        0.654 – 1.32	  774,680	    762,661	         0.00809 ± 0.00330
P. aeruginosa	        1.32 – 2.68	      1,251,665	    1,231,882	     0.00802 ± 0.00223
P. aeruginosa	        2.68 – 5.88	      1,582,696	    1,552,040	     0.00983 ± 0.00292
P. aeruginosa	            > 5.88	      1,632,175	    1,590,106	     0.01662 ± 0.01146
S. pneumoniae	        0 – 0.654	      63,106	    61,929	         0.00398 ± 0.01967
S. pneumoniae	        0.654 – 1.32	  154,988	    152,691	         0.00752 ± 0.00611
S. pneumoniae	        1.32 – 2.68	      278,738	    274,868	         0.00698 ± 0.00331
S. pneumoniae	        2.68 – 5.88	      372,537	    366,339	         0.00810 ± 0.00447
S. pneumoniae	           > 5.88	      407,961	    398,863	         0.01008 ± 0.00434
M. tuberculosis	        0 – 0.654	      6,943	        6,902	         0.00262 ± 0.03578
M. tuberculosis	        0.654 – 1.32	  18,660	    18,514	         0.00427 ± 0.01338
M. tuberculosis	        1.32 – 2.68	      37,833	    37,483	         0.00440 ± 0.01009
M. tuberculosis	        2.68 – 5.88	      54,481	    54,036	         0.00458 ± 0.01041
M. tuberculosis	            > 5.88	      64,222	    63,169	         0.01159 ± 0.01470
Salmonella	            0 – 0.654	      164	        146	             0.05829 ± 0.18672
Salmonella	            0.654 – 1.32	  461	        423	             0.03662 ± 0.08169
Salmonella	            1.32 – 2.68	     1,042	        984	             0.02716 ± 0.07854
Salmonella	            2.68 – 5.88	     1,662	        1,630	         0.01449 ± 0.05558
Salmonella	                > 5.88	     2,153	        2,135	         0.02276 ± 0.07772


Answer
    There is no significant asymmetry as a function of momentum --> for every pair, the differences in A between momentum bins are smaller than their uncertainties.

    To quantify this, the lowest and highest momentum bin were compared, the same way we compared WT and mutant in Question 2:

    Strain	   A(highest bin) − A(lowest bin)	Significance
    E. coli	         0.0025 ± 0.0037	           0.7σ
    B. subtilis	     0.0006 ± 0.0052	           0.1σ
    P. aeruginosa	 0.0084 ± 0.0121	           0.7σ
    S. pneumoniae	 0.0061 ± 0.0201	           0.3σ
    M. tuberculosis	 0.0090 ± 0.0387	           0.2σ
    Salmonella	     −0.036 ± 0.202	               0.2σ

    All of these are far below 3σ, so the asymmetry is consistent with being the same at every momentum.

    Explanation of results:

    - Three bins have a significant asymmetry on their own. If you test each bin against zero (A ÷ uncertainty ≥ 3σ), three bins pass: E. coli 2.68 – 5.88 (A = 0.00109 ± 0.00031, 3.5σ), P. aeruginosa 1.32 – 2.68 (A = 0.00802 ± 0.00223, 3.6σ) and P. aeruginosa 2.68 – 5.88 (A = 0.00983 ± 0.00292, 3.4σ). In all three the WT is more common. This doesn't contradict the answer above --> it shows there is a real asymmetry in these momentum ranges, while the comparison table shows it is about the same size at every momentum.
    - The WT is more common than the mutant in almost every bin, for every strain (Q2).
    - P. aeruginosa has an asymmetry of about 0.008–0.010 in the four lower bins.
    - The highest bin (> 5.88) has much larger uncertainties for E. coli, B. subtilis and P. aeruginosa. Set 10 has very few bacteria in that range (for example 7,979 E. coli WT, against about 1.68 million in each other set), so its asymmetry there is noisy and increases the spread between sets.
    - Splitting the data into 5 bins leaves about a fifth of the cells in each bin, so each bin is less precise than the overall result in Question 2. M. tuberculosis and Salmonella are too rare to say anything about momentum dependence.
