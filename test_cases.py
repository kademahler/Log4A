import os

results_path = f"{os.path.dirname(os.path.realpath(__file__))}/results"
if not os.path.isdir(results_path):
    print("Collectors have not been run. Please run collectors and check again.")
    exit(0)

x = 0

for filename in os.listdir(results_path):
    if filename != "general.txt":
        with open(os.path.join(results_path, filename), 'r') as f:  # open in readonly mode
            x = x + len(f.readlines())

if x == 0 : print("No logs were collected. Please collect some and try again")
else: print (f"{x} lines of logs have been collected.")

