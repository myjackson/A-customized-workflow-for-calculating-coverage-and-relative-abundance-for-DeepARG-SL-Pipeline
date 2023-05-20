### Title : A customized workflow for calculating coverage and 16S-normalized abundance from intermediate data produced by DeepARG-SL-Pipeline.v2
## Written by Jangwoo Lee, PhD, Postdoctoral Fellow, University of Calgary, Calgary, AB, Canada
## Related publication : Acosta, Lee et al., 2023, Metagenomic analysis after selective culture enrichment of wastewater demonstrates increased burden of antibiotic resistant genes in hospitals relative to the community, medRxiv (Doi: https://doi.org/10.1101/2023.03.07.23286790) - Submitted to Nature Communications

### Overview : This customized workflow is designed to extract ARGs at more granular level (e.g., OXA-1, 2, ...) from intermediate data produced by DeepARG-SL-Pipeline.v2 (Arango-Argoty et al., 2018; https://doi.org/10.1186/s40168-018-0401-z). The final products (*.clean.deeparg.mapping.ARG.merged.quant.subtype) of this pipeline suggest ARG-subtypes at more aggregated level (e.g., OXA), thus a self-written workflow is required to explore ARG data at more granular level. This workflow consists of a total of 5-steps (Workflow_1 to 5).  

### Input Files :
#features.gene.length : A reference file where gene length for each ARG-subtype (gene_id) information is located. This could be found from the folder where DeepARG-DB is located (.../deeparg_db/database/v2/features.gene.length). Please refer to the pipeline developer's GitHub (https://hub.docker.com/r/gaarangoa/deeparg)
#Nicole_Hospital_16S_mapped_reads_and_sample_list_v1.csv : A sample list where sample ID (Seq_ID) and their corresponding 16S rRNA gene read number (#16S_reads) information is located. This should be manually created. For '#16S_reads', please refer to the final log files after running DeepARG-SL-Pipeline.
#*.clean.deeparg.mapping.ARG : An intermediate file from DeepARG-SL-Pipeline. This will be an input file for the first step of our workflow (1. Workflow_1_coverage_per_subtype.py).

### Python scripts for 5-step workflows : 
#1. Workflow_1_coverage_per_subtype.py : 'Coverage' for each ARG-subtype was calculated
#2. Workflow_2_ARGper16S_per_subtype.py : Relative abundace (ARGs normalized by 16S rRNA gene) was calculated
#3. Workflow_3_index-id_and_consolidating_files.py : All the files produced from the previous step were consolidated to produce a single summarized file
#4. Workflow_4_assigning_ARG_class.py : The final results from the previous step was updated, e.g., a new column for corresponding ARG-classification was added
#5. Workflow_5_aggregate_data_by_class.py : All the ARGs with same classification were aggregated to produce a final data matrix.
