# Python-Challenge

# PyBank

The code reads the 'budget_data.csv' file regarding the monthly profit/loss of a bank. the code start off by defiining the required variables and reading the csv file, initially skipping the first row as there are headings.

The code starts by looping through all the rows performing various tasks and printing the result:
  - Count the number of months starting the counter at zero and adding the one to the counter as it loops through the rows
  - Total profit is calculated by added all the profit/loss values of each month
  - Greatest profit is calculated by assessing the current profit/loss against a stored value, if the current value is greater than the previous value, it stores this and the corresponding date
  - Greatest loss is calculated by assessing the current profit/loss against a stored value, if the current value is less than the previous value, it stores this and the corresponding date
  - Average change is calculated constantly throughout the loop and will already iterate the last value and calculated using the total months - 1

# PyPoll

The code reads the 'election_data.csv' file regarding the votes for an election. the code start off by defiining the required variables and reading the csv file, initially skipping the first row as there are headings.

The code starts by looping through all the rows performing various tasks and printing the results:
  - Count the number of votes starting the counter at zero and adding the one to the counter as it loops through the rows
  - The code extracts names from the third column then as the code loops through the data, it adds a vote if the candidate is in the existing table. If not the code will add the candidate to the index.
  - Once the code has iterated through the rows, the code calculates the number of votes and the percentage aginast the total votes recorded. At the end, searches for the candidate with the greatest number of votes
