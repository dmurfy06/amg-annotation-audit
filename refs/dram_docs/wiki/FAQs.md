# DRAM in general
1. I am very interested in metabolism X which is not included in the distillate. Can you add it to the distillate in a future release?

    Maybe! If you are interested in contributing a metabolism or other function to DRAM [you can fill out the form here](https://forms.gle/82rkdf1XL9wx7CdM9). It will then be reviewed by the DRAM team and if approved will be included in a future release. Alternatively, submit a pull request or add [an issue](https://github.com/shafferm/DRAM/issues). To do this take the columns form [here](https://github.com/shafferm/DRAM/blob/master/data/genome_summary_form.tsv) and add your functions as new rows. 

# DRAM for genomes
1. When I run `DRAM.py annotate` I get an error saying there are too many genomes what does this mean?

    When you want to run DRAM on multiple genomes at once you must use linux wildcard syntax surrounded in quotes. For example if you have a folder full of fasta files of genomes that all end in `.fasta` called `genomes` you need to use the command `DRAM.py annotate -i 'genomes/*.fasta' -o annotations`. If you use `DRAM.py annotate -i genomes/*.fasta -o annotations` your command will not work because then your linux environment is trying to expand the wildcard which will not work with DRAM. Always remember quotes around your input paths with wildcards!

2. What do the gene names that are assigned to each gene mean?

    All genes are named based on the fasta file they come from, the scaffold they come from and the gene number of the scaffold that they are. This format looks like `{fasta name}_{scaffold name}_{gene number}`. For example the gene name `bin.55_scaffold_53_7` would be 7th gene on `scaffold_53` which is from the fasta file called `bin.55`.

3. The scaffolds that are in my `scaffolds.fa` and `annotations.tsv` are not the same as my input what are they now?

    They aren't! Scaffolds cannot have the same name across genomes so DRAM renames them based on the name of the fasta file they are from. FASTA names also should not be repeated across files but DRAM does not check for this. Please make sure that doesn't happen. Scaffolds are renamed to `{fasta name}_{scaffold name}`.

# DRAM-v
1. Why is there more cells lit up in my DRAM-v liquor than there are genes listed in the number of pAMGs column?

    This is because each gene can have more than one annotation and each annotation can be associated with more than one function. An example of the former is a gene with multiple functional domains each of which have their own annotation each of which are associated with a function in the DRAM distillate. This is common in genes which are transporters that also have a catalytic function. An example of the later is an annotation of a function that is associated with the metabolism of multiple substrates. This happens in some CAZymes which can act on multiple classes of sugars.

2. Why are there more rows in my AMG summary table than there are listed AMGs?

   See 1 above. Each row represents a function and a gene can have multiple functions or one annotation can be associated with multiple functions.