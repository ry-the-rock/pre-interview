import os
import subprocess
import time

def task_3(directory_name):
    for file in os.listdir(directory_name):
        file_name = os.fsdecode(file)
        command = "cvc5/bin/./cvc5 " + directory_name + "/"+ file_name + " --tlimit 60000"
        subprocess.run(command)


def task_4(directory_name):
    csv = open("task-4.txt", "a")
    for file in os.listdir(directory_name):
        file_name = os.fsdecode(file)
        command = "cvc5/bin/./cvc5 " + directory_name + "/"+ file_name + " --tlimit 60000"
        start_time = time.perf_counter()
        try:
            output = str(subprocess.check_output(command))
            end_time = time.perf_counter()
            output = output.replace("b'", "")
            output = output.replace(r"\r\n", "")
            output = output.replace("'", "")
        except subprocess.CalledProcessError:
            output = "timeout"
            end_time = time.perf_counter()
        time_elapsed = str(end_time-start_time)
        csv_input = file_name + "," + output + "," + time_elapsed + "\n"
        csv.write(csv_input)
    csv.close()




task_3("queries")
task_4("queries")