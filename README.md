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


## Ideas from the BioRxiv Semantic‑Matching Paper

https://arxiv.org/pdf/2412.08194

1. **Hybrid SLM + LLM Workflow**  
   - Leverage a small LM for a fast “broad brush” retrieval of candidate column matches (via cosine similarity), then use an LLM to rerank only the top K—cutting down on compute cost while preserving deep semantic understanding.
2. **Self‑Supervised Fine‑Tuning**  
   - Prompt a large model to generate realistic “fake” schema variants (renames, value shuffles, injected noise) and train the small model contrastively. No need for hand‑labeled pairs, yet you still capture domain‑specific quirks.
3. **Scalable, Domain‑Aware Filtering**  
   - The two‑phase design mirrors search engines (coarse recall → fine precision), so you can scale to hundreds of columns without blowing up your LLM bills.
4. **Normalized Similarity Scores → Confidence Scores**  
   - They report match strengths as 0.00–1.00 “similarity scores.” We can extend this idea into **confidence scores** on multiple axes, e.g.:

   | Criterion               | Example Confidence Question                                                         |
   |-------------------------|-------------------------------------------------------------------------------------|
   | Name Consistency        | “How closely do the two column names align in meaning and formatting?”              |
   | Vocabulary Overlap      | “Do the cell values share key domain terms, synonyms, or ontological labels?”       |
   | Distribution Alignment  | “How similar are the value distributions (types, ranges, frequency) between columns?”|
   | Contextual Coherence    | “Do sampled values, when read in context, convey the same semantic category?”       |
   | Noise Robustness        | “Can the model correctly match despite typos, abbreviations, or inconsistent casing?”|

5. **Actionable Takeaway**  
   - This paper offers a proven blueprint if you want to build a semantic‑matching layer atop your table‑evaluation tool—just swap in your own confidence‑criteria questions and you’re set.

## User Challenges for Each Error: _Work in Progress_

Users will now try to use their own AI model to handle errors in various settings:
- **Typo Correction**  
- **Synonym & Semantic Matching**  
- **Abbreviation Expansion**  
- **Value‑Distribution Checking**  
- **Context‑Driven Disambiguation**  
- _…and more to come!_  
