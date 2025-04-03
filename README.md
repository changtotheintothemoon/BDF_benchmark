# Table Comparison and Evaluation Tool

This tool compares AI-annotated tables with ground truth tables and calculates evaluation metrics including precision, recall, and F1-score for each column and overall performance.

## Features

- Column-wise evaluation metrics (Precision, Recall, F1-score)
- Overall performance metrics
- Support for CSV file inputs
- Detailed output formatting
- Error handling for mismatched columns

## Requirements

- Python 3.6 or higher
- Required Python packages (see requirements.txt):
  - pandas
  - scikit-learn
  - numpy

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with two CSV files as arguments:
```bash
python evaluate_tables.py <ai_table_path> <ground_truth_path>
```

### Example

```bash
python evaluate_tables.py data/ai_annotated.csv data/ground_truth.csv
```

### Input Format

Both input files should be in CSV format with matching column headers. For example:

**AI Annotated Table (ai_annotated.csv)**:
```csv
id,diagnosis,assay,tumorType
syn17774134,Neurofibromatosis type 1,whole exome sequencing,Plexiform Neurofibroma
syn21296150,Neurofibromatosis type 1,whole exome sequencing,Malignant Peripheral Nerve Sheath Tumor
syn53204725,Neurofibromatosis type 1,whole genome sequencing,Malignant Peripheral Nerve Sheath Tumor
syn20705381,Neurofibromatosis type 1,MRI,Unknown
syn26067698,Not Available,immunohistochemistry,Cutaneous Neurofibroma
```

**Ground Truth Table (ground_truth.csv)**:
```csv
id,diagnosis,assay,tumorType
syn17774134,Neurofibromatosis type 1,whole exome sequencing,Plexiform Neurofibroma
syn21296150,Neurofibromatosis type 1,whole exome sequencing,Malignant Peripheral Nerve Sheath Tumor
syn53204725,Neurofibromatosis type 1,whole genome sequencing,Malignant Peripheral Nerve Sheath Tumor
syn20705381,Neurofibromatosis type 1,conventional MRI,Unknown
syn26067698,Not Applicable,immunohistochemistry,Cutaneous Neurofibroma
```

### Output Format

The script will output metrics for each column and overall performance. Key differences in the example above include:
- Different assay names ("MRI" vs "conventional MRI")
- Different diagnosis values ("Not Available" vs "Not Applicable")

Example output:

```
Column-wise Metrics:
--------------------------------------------------

Column: id
Precision: 1.0000
Recall: 1.0000
F1-score: 1.0000

Column: diagnosis
Precision: 0.8000
Recall: 0.8000
F1-score: 0.8000

Column: assay
Precision: 0.8000
Recall: 0.7000
F1-score: 0.7333

Column: tumorType
Precision: 1.0000
Recall: 0.9000
F1-score: 0.9400

Overall Performance:
--------------------------------------------------
Precision: 0.9000
Recall: 0.8500
F1-score: 0.8683
```

The metrics show:
- Perfect matching for `id` and `tumorType` columns
- Lower scores for `diagnosis` and `assay` columns due to text variations
- Overall high performance (0.9) across all columns

## User challenges for each errors

User will now try to use their own AI model to handle error for various settings:
- Correction of typos
- Synonyms semantic matching
- etc...
