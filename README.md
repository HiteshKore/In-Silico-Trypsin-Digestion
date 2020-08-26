# In-Silico-Trypsin-Digestion
Note:
1.	The script is written under Python 3.6
2.	It follows the proline rule (does not cut after lysine (K) or arginine (R) followed by proline (P)) and only cleaves the protein sequences after K and R.
3.	This script generates the peptides between 7 to 35 amino acids as most peptides resulted after the trypsin digestion are 7-35 amino acids long.
4.	Output file contains the fasta headers, count of tryptic peptides, and their corresponding sequences.

Command usage: python3 Insilico_Trypsin_digestion.py -i input_file -o output_file

Input file format- (Please refer the Input.txt file)
>Sq1	MKDEDFSQNLSLDSSTLLFTHIPAIFFVLRLVYEELKLNTLMGEGICSLLNFSFSWQG

>Sq2	PPYPYLPGICERSRLVVLSIALYILGDESSVSDESSQYLTRITVA
