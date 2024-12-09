def read_input(file_path):
    with open(file_path, 'r') as file:
        data = [[int(value) for value in line.strip().split()] for line in file]
    return data

def is_report_ordered(report):
    report_sorted = report.copy()
    report_reverse_sorted = report.copy()
    report_sorted.sort()
    report_reverse_sorted.sort(reverse=True)
    if report == report_sorted or report == report_reverse_sorted:
        return True 
    
def is_report_increase_safe(report):
    previous_value = report[0]
    for value in report[1:]:
        if value == previous_value or abs(value - previous_value) > 3:
            return False
        previous_value = value
    return True
        

def safe_count(reports):
    safe_count = 0
    for report in reports:
        if is_report_ordered(report) and is_report_increase_safe(report):
            safe_count+=1
            # print("Safe report: ", report)
        # else:
            # print("Unsafe report: ", report)
    return safe_count


if __name__ == "__main__":
    reports = read_input('input.txt')
    safe_count = safe_count(reports)
    print(f"Safe count is {safe_count}")
