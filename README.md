# DNA-Sequence-Melting-Point-Calculator

Introduction

A polynucleotide sequence is the most basic form of genetic material. Although there are two types of polynucleotide sequences, whether it is single-stranded Ribonucleic Acid (RNA) or double-stranded Deoxyribonucleic Acid (DNA), all such genetic materials are composed of chains of nucleotides, a combination of a phosphate and a pentagonal sugar with a nitrogenous base attached to it. There are four types of nitrogenous bases known to exist in DNA: adenine, cytosine, guanine, and thymine. These unique DNA sequences determine the phenotypes and genotypes of its host organism.

Since polynucleotide sequence analysis serves as the basis for many subdisciplines of biology, it is a key step in designing experiments in such scientific fields. As a student passionate for biology, I have created my own polynucleotide sequence analyser using Python programming to use in my future scientific endeavors. 

How to Use

Download any programming application that supports python using your browser. Once that has been completed, reference the links below that will redirect you to my GitHub pages containing the projects. Download and open them in the application. In the input terminal, enter the DNA sequence without any hyphens or spaces (ex. ATCGATCG). Once that has been completed, the analyzed results to the components below will be returned.

Features

1. Melting Point (Tm) Calculator

DNA naturally exists as a duplex polynucleotide, but for it to be analyzed in laboratorical settings, it will have to undergo transcription and be converted into a single-stranded form. The Tm of a DNA sample is the temperature where exactly 50% it is converted to single strand, and at any temperature above that, the percentage of single strands will increase. In experiments where DNA is duplicated, the samples must be heated precisely to its Tm to be converted into single strands for Polymerase Chain Reactions to occur. The following is the equation for the Tm calculation: 

*Note that all alphabets represent the number of the corresponding bases in the sample

If the DNA sequence is less than or equal to 13 nucleotides:
Tm = (A + T) * 2 + (C + G) * 4
If elsewise:
Tm = 64.9 + (C + G - 16.4) * 41 / Sample Length

2. Longest Palindrome Finder

Palindromic sequences are DNA subsequences with significance in representing mammalian genome evolution. This calculator returns the longest palindromic sequence of any imputed DNA sample.

3. Polypeptide Translation

Single-stranded polynucleotide sequences are converted to protein in a process known as translation, where the sequence is broken into codons (triplets of amino acids) and their corresponding amino acids. The resulting sequence of amino acids is known as a polypeptide sequence. There can be a maximum of 3 distinct possible polypeptide sequences depending on the reading frame, and this program returns all possibilities. It should be noted that although this program returns all polypeptide sequences theoretically produceable based on the inputted DNA sample, it is possible that post-translational protein processing proves otherwise.
