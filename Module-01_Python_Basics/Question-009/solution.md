log_line=input("Enter the log line = ")
parts=log_line.split("|")
measurement_type=parts[1].strip()
value=parts[2].strip().split()[0]
print(f"measurement type ={measurement_type}")
print(f"value= {value}")
