import numpy as np
from itertools import groupby

with open("day_2/input.txt", "r") as file:
    data = file.read()

data_list = []
diff_list = []
for row in data.splitlines():
    report = []
    for i in row.split(" "):
        if i.isdigit():
            report.append(int(i))
    report = np.array(report)
    data_list.append(report)
    diff_list.append(np.diff(report))

data_list = data_list
diff_list = diff_list

correct_reports = 0
distance_reports = np.array([np.sum(np.where((np.abs(diff_report) > 3) | (np.abs(diff_report) < 1), 1, 0)) for diff_report in diff_list])
sign_reports = np.array([np.where(len(np.unique(np.sign(diff_report), return_counts=True)[1]) == 1, 0, 1) for diff_report in diff_list])

report_results = distance_reports + sign_reports

print("Correct reports: ", np.sum(report_results == 0))

#### Part 2

report_results_2 = 0
def check_violations(report):
    diff_report = np.diff(report)
    distance_mismatch = np.where((np.abs(diff_report) > 3) | (np.abs(diff_report) < 1), 1, 0)
    signs = np.sign(diff_report)
    unique, counts = np.unique(np.sign(diff_report), return_counts=True)
    sign_mismatch = np.abs(signs - unique[unique != 0][np.argmax(counts[unique != 0])])
    violation_count = np.sum(np.where((distance_mismatch + sign_mismatch) > 0, 1, 0))

    return violation_count

for i, data_report in enumerate(data_list):
    for j in range(len(data_report)):
        new_report = np.delete(data_report, j)
        violation_count = check_violations(new_report)
        if violation_count == 0:
            report_results_2 += 1
            break


print("Correct reports: ", report_results_2)
