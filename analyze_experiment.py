from typing import Tuple

import pandas as pd

positives_path = "all_out/experiments_data/data/dbaasp/activity/active_32.tsv"
negatives_path = "all_out/experiments_data/data/dbaasp/activity/inactive_128.tsv"

df_positives = pd.read_csv(positives_path, delimiter="\t")
df_negatives = pd.read_csv(negatives_path, delimiter="\t")


def get_confusion_matrix(df_positives: pd.DataFrame, df_negatives: pd.DataFrame, pred_col_name: str, postives_value) -> \
Tuple[int, int, int, int]:
    all_actual_positives = len(df_positives)
    all_actual_negatives = len(df_negatives)
    print(f"all_pos: {all_actual_positives}, all_neg: {all_actual_negatives}")

    true_positives = len(df_positives[df_positives[pred_col_name] == postives_value])
    false_negatives = all_actual_positives - true_positives

    false_positives = len(df_negatives[df_negatives[pred_col_name] == postives_value])
    true_negatives = all_actual_negatives - false_positives

    return true_negatives, false_positives, false_negatives, true_positives

x = get_confusion_matrix(df_positives, df_negatives, "Prediction", "AMP")
print(x)
