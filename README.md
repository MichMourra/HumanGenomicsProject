# HumanGenomicsProject
*Description*


## GetVariants
This program takes the genemap2.txt OMIM file and retrieve the interest fields like the MIMnumber and chromosomic coordinates. With this fields the program save in VariantFileOMIM3.txt all the variants associated to heritable diseases in Ensembl database. Once we have all the variants the programmatic access with urllib use this file to locate the nucleotide changes between reference and alternative aleles.

Finally GetVariants use this data to generate the file Monogenic2.avinput with the next fields per column:
1. The variant Chromosome
2. The Variant Start Position
3. The Variant End Position
4. The Reference Allele
5. The Alternative Allele

## Filters
Once created Monogenic2.avinput, the variants were filtered, depending their inheritance and pathogenicity using FilterVariants.Rmd and a file Monogenic3.avinput is created.
The annotation is performed with annovar using annotate_variation.pl with the following parameters
*-out Monogenic3 -build hg38  humandb/*

## SimpleRegion
The correct sequences of the reference alleles of the invalid variants in Monogenic3.invalid_input are retrieved with annovar using FilterInvalid.Rmd. 
This script creates a file .simple_format required to use an accesory program of annovar, retrieve_seq_from_fasta.pl. creating a .simple_format.fa 
Using RetrieveSequences.Rmd an Invalid.avinput was created which was also annotated.

## Annotation 
In FilterInvalid.Rmd is the code to use in annovar using annotate_variation.pl which uses genome version hg38. Also further details are in GHproject.ipynb

### ANNOVAR_hg38_filtered
Outputs of the annotation of Monogenic3.avinput file

### ANOVAR_hg38_invalid_filtered
Outputs of the annotation of Invalid.avinput

## Plots

## Further Info
See the Results in PDF for further information about the format of the files.

Also see 

avinput format, values of .variant_function and .exonic_variant_function files from annotate_variation.pl of [annovar](https://annovar.openbioinformatics.org/en/latest/user-guide/gene/)
.simple_region format and .simple_region.fa [retrieve_seq_from_fasta.pl](https://annovar.openbioinformatics.org/en/latest/misc/accessory/#retrieve_seq_from_fasta-retrieve-nucleotideprotein-sequences)

### Contacts
jlealriv@lcg.unam.mx
cmourra@lcg.unam.mx
