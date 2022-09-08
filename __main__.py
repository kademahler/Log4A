import os
from time import strptime
import collector_registry
import collectors

def get_time_input():
    print("You will now enter the time period for which you would like to collect logs.")
    print("Please use the following format: DD/MM/YYYY HH:MM:SS")
    input_begin_time = input("Please enter a START time for log collection: ")
    input_end_time = input("Please enter an END time for log collection: ")
    print()
    try:
        collector_registry.set_begin_time(strptime(input_begin_time, "%d/%m/%Y %H:%M:%S"))
        collector_registry.set_end_time(strptime(input_end_time, "%d/%m/%Y %H:%M:%S"))
    except ValueError as e:
        print("Time was not entered correctly. It should follow the format DD/MM/YYYY HH:MM:SS")
        print("")
        return get_time_input()
    

print("Log4A - Log 4 Aggregation - A basic log collector")
print()

get_time_input()

print("Starting Collectors...")
print("")

results_path = f"{os.path.dirname(os.path.realpath(__file__))}/results"
general_log = open(f"{results_path}/general.txt", 'w')

general_log.write("Starting collections\n\n")
for collector in collector_registry.ALL_COLLECTORS:
    print(f"Getting logs using: {collector.name}")
    general_log.write(f"Getting logs using: {collector.name}\n")
    collector_results = collector()
    hash = collector_results[0]
    file_contents = collector_results[1]
    results_file = open(f"{results_path}/{collector.name}.txt", 'w')
    results_file.write(f"{file_contents}")
    results_file.close()

    check_file = open(f"{results_path}/{collector.name}.txt", 'r')
    check_contents = check_file.read()
    check_hash = collectors.check_content_hash(check_contents);
    if (hash != check_hash):
        print(f"Hash check failed for collector {collector.name}. Quitting")
        general_log.write(f"Hash check failed for collector {collector.name}. {hash} != {check_hash}.\n\n")
        continue
    else:
        general_log.write(f"Hash check passed for collector {collector.name}: {hash} == {check_hash} \n\n")
    



print("")
print("Collections complete. The logs have been placed in the ./results directory")