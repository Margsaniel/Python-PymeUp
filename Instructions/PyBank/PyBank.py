import os, csv

file_to_load = os.path.join("Resources/budget_data.csv")

month_count = 0
month_of_change = []
net_change_list = []
total_net = 0
increase = ["", 0]
decrease = ["", 0]

# Open and read csv
with open(file_to_load) as budget_data:
    csv_reader = csv.reader(budget_data)
    # Read the header row first (skip this part if there is no header)
    data = next(csv_reader)

    
    first_row = next(csv_reader)
    
    month_count = month_count + 1
    
    total_net = total_net + int(first_row[1])
    
    prev_net = int(first_row[1])

    for row in csv_reader:

        month_count = month_count + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        if net_change > increase[1]:
            increase[0] = row[0]
            increase[1] = net_change


        if net_change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_change


net_monthly_avg = sum(net_change_list) / len(net_change_list)


data_output = (
    f"\nFinancial Analysis\n"
    f"----------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n")

print(data_output)

