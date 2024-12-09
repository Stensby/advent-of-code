def read_input(file_path):
    with open(file_path, 'r') as file:
        data = [[int(value) for value in line.strip().split()] for line in file]
    return data

    
def is_report_safe(report):
    print("Checking report: ", report)
    previous_value = report[0]
    direction_of_change_positive = (report[1] - report[0]) > 0
    for i in range(1, len(report)):
        if report[i] == previous_value:
            print("Failed equality check at index: ", i)
            return False, i
        if report[i] < previous_value and direction_of_change_positive:
            print("Failed increase check at index: ", i)
            return False, i
        if report[i] > previous_value and not direction_of_change_positive:
            print("Failed decrease check at index: ", i)
            return False, i
        if abs(report[i] - previous_value) > 3:
            print("Failed distance check at index: ", i)
            return False, i
        previous_value = report[i]
    return True, None
        

def safe_count(reports):
    safe_count = 0
    for report in reports:
        is_safe, failed_index = is_report_safe(report)
        if is_safe:
            safe_count+=1
            print("Safe report: ", report)
        else:
            prev_failed_index = failed_index
            prev_failed_value = report.pop(failed_index)
            is_safe, failed_index = is_report_safe(report)
            if is_safe:
                safe_count+=1
                print("Safe report: ", report)
            else:
                # reinstate the removed value, and remove the previous value
                report.insert(prev_failed_index, prev_failed_value)
                report.pop(prev_failed_index-1)
                is_safe, failed_index = is_report_safe(report)
                if is_safe:
                    safe_count+=1
                    print("Safe report: ", report)
                else:
                    print("Unsafe report: ", report)
        print("================================")
    return safe_count

def safe_count_brute_force(reports):
    safe_count = 0
    for report in reports:
        is_safe, failed_index = is_report_safe(report)
        if is_safe:
            safe_count+=1
            print("Safe report: ", report)
        else:
            # brute force by trying every possible removal of a single element
            for i in range(len(report)):
                removed_value = report.pop(i)
                is_safe, failed_index = is_report_safe(report)
                if is_safe:
                    safe_count+=1
                    print("Safe report: ", report)
                    break
                else:
                    report.insert(i, removed_value)
                    print("Unsafe report: ", report)
        print("================================")
    return safe_count

if __name__ == "__main__":
    reports = read_input('input.txt')
    count_of_safe_reports = safe_count_brute_force(reports)
    print(f"Safe count is {count_of_safe_reports}")
