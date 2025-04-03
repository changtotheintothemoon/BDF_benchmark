import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

def compare_tables(ai_table_path, ground_truth_path):
    """
    Compare AI-annotated table with ground truth table and calculate evaluation metrics.
    
    Args:
        ai_table_path (str): Path to the AI-annotated table (CSV file)
        ground_truth_path (str): Path to the ground truth table (CSV file)
    
    Returns:
        dict: Dictionary containing evaluation metrics for each column and overall performance
    """
    # Read the tables
    ai_table = pd.read_csv(ai_table_path)
    ground_truth = pd.read_csv(ground_truth_path)
    
    # Ensure both tables have the same columns
    if not set(ai_table.columns) == set(ground_truth.columns):
        raise ValueError("Tables must have the same columns")
    
    # Initialize results dictionary
    results = {
        'column_metrics': {},
        'overall_metrics': {}
    }
    
    # Calculate metrics for each column
    for column in ai_table.columns:
        # Get the values for this column
        ai_values = ai_table[column].fillna('').astype(str)
        gt_values = ground_truth[column].fillna('').astype(str)
        
        # Calculate metrics
        precision = precision_score(gt_values, ai_values, average='weighted', zero_division=0)
        recall = recall_score(gt_values, ai_values, average='weighted', zero_division=0)
        f1 = f1_score(gt_values, ai_values, average='weighted', zero_division=0)
        
        results['column_metrics'][column] = {
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }
    
    # Calculate overall metrics
    all_ai_values = ai_table.values.flatten()
    all_gt_values = ground_truth.values.flatten()
    
    overall_precision = precision_score(all_gt_values, all_ai_values, average='weighted', zero_division=0)
    overall_recall = recall_score(all_gt_values, all_ai_values, average='weighted', zero_division=0)
    overall_f1 = f1_score(all_gt_values, all_ai_values, average='weighted', zero_division=0)
    
    results['overall_metrics'] = {
        'precision': overall_precision,
        'recall': overall_recall,
        'f1_score': overall_f1
    }
    
    return results

def print_results(results):
    """
    Print the evaluation results in a readable format.
    """
    print("\nColumn-wise Metrics:")
    print("-" * 50)
    for column, metrics in results['column_metrics'].items():
        print(f"\nColumn: {column}")
        print(f"Precision: {metrics['precision']:.4f}")
        print(f"Recall: {metrics['recall']:.4f}")
        print(f"F1-score: {metrics['f1_score']:.4f}")
    
    print("\nOverall Performance:")
    print("-" * 50)
    print(f"Precision: {results['overall_metrics']['precision']:.4f}")
    print(f"Recall: {results['overall_metrics']['recall']:.4f}")
    print(f"F1-score: {results['overall_metrics']['f1_score']:.4f}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python evaluate_tables.py <ai_table_path> <ground_truth_path>")
        sys.exit(1)
    
    ai_table_path = sys.argv[1]
    ground_truth_path = sys.argv[2]
    
    try:
        results = compare_tables(ai_table_path, ground_truth_path)
        print_results(results)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1) 