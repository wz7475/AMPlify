from typing import Tuple
import os
import pandas as pd


def get_confusion_matrix(df_positives: pd.DataFrame, df_negatives: pd.DataFrame, pred_col_name: str,
                         postives_value: str, negatives_value: str) -> \
        Tuple[int, int, int, int, int]:
    all_actual_positives = len(df_positives)
    all_actual_negatives = len(df_negatives)
    print(f"all_pos: {all_actual_positives}, all_neg: {all_actual_negatives}")

    true_positives = len(df_positives[df_positives[pred_col_name] == postives_value])
    false_negatives = len(df_positives[df_positives[pred_col_name] == negatives_value])

    false_positives = len(df_negatives[df_negatives[pred_col_name] == postives_value])
    true_negatives = len(df_negatives[df_negatives[pred_col_name] == negatives_value])

    failed_num = all_actual_positives + all_actual_negatives - (
            true_negatives + false_negatives + false_negatives + true_positives)

    return true_negatives, false_positives, false_negatives, true_positives, failed_num


def get_metrics(tn, fp, fn, tp):
    acc = (tp + tn) / (tn + fp + fn + tp)
    tpr = tp / (tp + fn)
    fpr = fp / (tn + fp)
    return acc, fpr, tpr


def analyze_experiment(positives_path, negatives_path):
    df_positives = pd.read_csv(positives_path, delimiter="\t")
    df_negatives = pd.read_csv(negatives_path, delimiter="\t")

    tn, fp, fn, tp, err = get_confusion_matrix(df_positives, df_negatives, "Prediction", "AMP", "non-AMP")
    print(f"tn: {tn}, fp: {fp}, fn: {fn}, tp: {tp}, err: {err}")

    acc, fpr, tpr = get_metrics(tn, fp, fn, tp)
    print(f"acc {acc}, fpr {fpr} tpr {tpr}")


def get_outputs_pairs(output_dir: str):
    pairs = []
    allowed_suffixes = ["active_32.tsv", "inactive_128.tsv"]
    all_paths_for_pairs = set()
    for root, _, files in os.walk(output_dir):
        for file in files:
            fullpath = os.path.join(root, file)
            for allowed_suf in allowed_suffixes:
                if fullpath.endswith(allowed_suf):
                    all_paths_for_pairs.add(fullpath)
            # print(root, file)
    print(all_paths_for_pairs)

if __name__ == "__main__":
    positives_path = "all_out/experiments_data/data/dbaasp/activity/active_32.tsv"
    negatives_path = "all_out/experiments_data/data/dbaasp/activity/inactive_128.tsv"

    # analyze_experiment(positives_path, negatives_path)
    get_outputs_pairs("all_out")