#import modules
import os
import csv

#path for file
file_to_load=os.path.join("..", "Resources", "budget_data.csv")

# Output files
file_to_output = os.path.join("Financial_Analysis_Summary.txt")

#set output of text file
text_path="output.txt"

#lists to store data
total_months= 0
total_net= 0
net_change_list = []
greatest_increase= ["", 0]
greatest_decrease= ["", 9999999999999] 
month_of_change = []

#open csv file
with open(file_to_load) as financial_data:
    reader= csv.reader(financial_data)

    #Read header row
    header = next(reader)

    #Extract first row to avoid appending net_change_list
    first_row=next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    #loop through to find total months
    for row in reader:
        #count the total months
        total_months+=1
        total_net += int(row[1])

        #calculate net change
        net_change=int(row[1])-prev_net
        prev_net=int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
    if net_change > greatest_increase[1]:
        greatest_increase[0]=row[0]
        greatest_increase[1]= net_change
    if net_change < greatest_decrease[1]:
        greatest_decrease[0]=row[0]
        greatest_decrease[1]=net_change

#print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {(total_months)}")
print(f"Total: ${(total_net)}")
print(f"Average Change: {round(sum(net_change_list)/len(net_change_list),2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    
#write methods to print to Financial_Analysis_Summary 
with open(file_to_output, 'w') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {(total_months)}")
    file.write("\n")
    file.write(f"Total: ${(total_net)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(net_change_list)/len(net_change_list),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
