samples_dict = {
    "Sample 1": {
        "Control values": [10.5, 11.2, 10.8],
        "Treatment values": [25.3, 24.7, 26.1]
    },
    "Sample 2": {
        "Control values": [8.2, 8.5, 8.0],
        "Treatment values": [12.1, 11.8, 12.5]
    },
    "Sample 3": {
        "Control values": [15.0, 14.8, 15.2],
        "Treatment values": [18.5, 18.2, 18.8]
    }
}

for sample in samples_dict:
    control_values = samples_dict[sample]["Control values"]
    treatment_values = samples_dict[sample]["Treatment values"]
    
    control_avg = sum(control_values) / len(control_values)
    treatment_avg = sum(treatment_values) / len(treatment_values)

    fold_change = treatment_avg / control_avg
    
    print(f"{sample} - Control Average: {control_avg:.2f}, Treatment Average: {treatment_avg:.2f}")
    print(f"Fold change: {fold_change:.2f}")
    
    if fold_change > 2.0 or fold_change < 0.5:
        print(f"{sample} shows significant change.")