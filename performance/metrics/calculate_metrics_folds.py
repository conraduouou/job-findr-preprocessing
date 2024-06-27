import csv
import os
import pandas as pd
import time

#### CONSTANTS ####

# replace with actual file name
TEST_CSV = "performance/tests/test-developed.csv"
PREDICT_CSV = "performance/predictions/predictions-developed.csv"

METRICS_PATH = "metrics-developed.csv"
METRICS_DIR = "performance/test"

CLASSIFICATIONS = [
    "accountant",
    "application developer",
    "auditor",
    "bookkeeper",
    "chef",
    "clerk",
    "college professor",
    "customer service representative",
    "database administrator",
    "event planner",
    "financial advisor",
    "financial manager",
    "graphic designer",
    "hotel and restaurant staff",
    "hr manager",
    "illustrator",
    "medical assistant",
    "medical doctor",
    "medical laboratory technologist",
    "office manager",
    "pharmacist",
    "project coordinator",
    "public relations",
    "recruiter",
    "registered nurse",
    "researcher",
    "software engineer",
    "sped teacher",
    "system analyst",
    "tutor",
    "web developer",
]

#### START OF PROCESS ####
start = time.perf_counter()

df = pd.read_csv(TEST_CSV)
df_list = df.apply(lambda x: x.to_dict(), axis=1).tolist()

predicted_df = pd.read_csv(PREDICT_CSV)
predicted_list = predicted_df.apply(lambda x: x.to_dict(), axis=1).tolist()

# matrix
confusion_matrix = [ [ 0 for _ in range(len(CLASSIFICATIONS)) ] for _ in range(len(CLASSIFICATIONS)) ]

# performance metrics
metrics_per_fold = {}

count = 0

# prediction phase of test set
for resume_data, prediction_data in zip(df_list, predicted_list):
    # track prediction count
    count += 1

    # target value
    target = resume_data["job_position"]
    prediction = prediction_data["prediction"]
            
    # increment prediction in confusion matrix
    target_index = CLASSIFICATIONS.index(target)
    prediction_index = CLASSIFICATIONS.index(prediction)
    confusion_matrix[target_index][prediction_index] += 1

    # calculate metrics for each fold
    if count % 40 == 0 or count == len(df_list):
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for index in range(len(confusion_matrix)):
            tp += confusion_matrix[index][index]
            fn += sum([ confusion_matrix[index][i] for i in range(len(confusion_matrix)) if i != index ])
            fp += sum([ confusion_matrix[i][index] for i in range(len(confusion_matrix)) if i != index ])
            tn += sum(
                [ sum([ confusion_matrix[i][j] for j in range(len(confusion_matrix)) if j != index ]) for i in range(len(confusion_matrix)) if i != index ]
            )

        print(tp, tn, fp, fn)

        # calculate metrics
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        if precision == 0 or recall == 0:
            f1_score = 0
        else:
            f1_score = 2 * (precision * recall / (precision + recall))

        # prepare fold update
        fold = count // 40

        if fold in metrics_per_fold.keys():
            fold += 1

        metrics_per_fold[fold] = {
            "TP": tp,
            "TN": tn,
            "FP": fp,
            "FN": fn,
            "Precision": precision,
            "Recall": recall,
            "F1-Score": f1_score
        }
        
        # reset confusion matrix for each fold
        for i in range(len(confusion_matrix)):
            for j in range(len(confusion_matrix)):
                confusion_matrix[i][j] = 0

# create results csv
if not os.path.exists(METRICS_DIR):
    os.mkdir(METRICS_DIR)

path = os.path.join(METRICS_DIR, METRICS_PATH)
with open(path, "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    total_metrics = [ "TOTAL", 0, 0, 0, 0, 0.0, 0.0, 0.0 ]
    for metric in metrics_per_fold.values():
        total_metrics[1] += metric["TP"]
        total_metrics[2] += metric["TN"]
        total_metrics[3] += metric["FP"]
        total_metrics[4] += metric["FN"]
        total_metrics[5] += metric["Precision"]
        total_metrics[6] += metric["Recall"]
        total_metrics[7] += metric["F1-Score"]
    
    total_metrics[5] = total_metrics[5] / len(metrics_per_fold)
    total_metrics[6] = total_metrics[6] / len(metrics_per_fold)
    total_metrics[7] = total_metrics[7] / len(metrics_per_fold)

    csv_writer.writerow(["fold", *metrics_per_fold[1].keys()])

    for index, fold in metrics_per_fold.items():
        row = [ index, *[ *[v for _, v in fold.items()] ] ]
        csv_writer.writerow(row)

    csv_writer.writerow(total_metrics)

# END OF PROCESS
elapsed = time.perf_counter() - start
minutes = int(elapsed // 60)
seconds = int(elapsed % 60)

print(f"Done! Took {minutes}m {seconds}s!")