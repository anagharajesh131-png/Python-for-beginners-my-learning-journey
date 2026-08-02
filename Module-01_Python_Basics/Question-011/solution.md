def generate_report_header(experiment_name, date, researcher):
    header = f"""experiment:{experiment_name}
date:{date}
researcher:{researcher}"""
    return header

report = generate_report_header(
    "motion of pendulum",
    "31-07-2026",
    "Anagha"
)
print(report)
