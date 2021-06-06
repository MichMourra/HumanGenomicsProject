# HumanGenomicsProject

## GetVariants

## Filters
Once created Monogenic2.avinput, the variants were filtered, depending tehir inheritance and pathogenicity using FilterVariants.Rmd and a file Monogenic3.avinput was created.
The annotation was performed with annovar using annotate_variation.pl with the following parameters
*-out Monogenic3 -build hg38  humandb/*

## SimpleRegion
The correct sequences of the reference alleles of the invalid variants in Monogenic3.invalid_input were retrieve with annovar using FilterInvalid.Rmd. 
This script creates a file .simple_format required to use an accesory program of annovar, retrieve_seq_from_fasta.pl. creating a .simple_format.fa 
Using RetrieveSequences.Rmd an Invalid.avinput was created which was also annotated.

## Annotation 
In FilterInvalid.Rmd is the code to use in annovar using annotate_variation.pl which uses genome version hg38. Also further details are in GHproject.ipynb

### ANNOVAR_hg38_filtered
Outputs of the annotation of Monogenic3.avinput file

### ANOVAR_hg38_invalid_filtered
Outputs of the annotation of Invalid.avinput

## Plots

See the Results in PDF for further information about the format of the files.
Also see 
avinput format, values of .variant_function and .exonic_variant_function files from annotate_variation.pl of[annovar](https://annovar.openbioinformatics.org/en/latest/user-guide/gene/)
.simple_region format and .simple_region.fa [retrieve_seq_from_fasta.pl](https://annovar.openbioinformatics.org/en/latest/misc/accessory/#retrieve_seq_from_fasta-retrieve-nucleotideprotein-sequences)
