# Power Consumption Analysis

Python script that allows users to measure the power consumption of a single process on their computer.

## Install and run

To run this program, you need to be on linux and have Python 3 and the psutil library installed on your system. You can install the psutil library using pip:

```bash
pip install psutil
```

After installing the required dependencies, you can run the program using the command line. The program takes the following arguments:

```
-p or --process: PID of the process to be analyzed (required)
-c or --cpu-power: CPU power consumption of the computer (required)
-m or --mem-power: Memory power consumption of the computer (required)
-t or --time: Time duration for measuring the power consumption
```

For example, to measure the power consumption of a process with PID 1234 for 20 seconds on a computer with a CPU power consumption of 50 watts and a memory power consumption of 10 watts, you can run the following command:

```bash
python power_consumption.py -p 1234 -c 50 -m 10 -t 20
```

To know the power consumption you can use a command line program like powerstat in linux. The output of the program gives information about the power consumption of a process running on a computer for a specific time period. The output includes the following information: Process name, Average CPU usage, Average memory usage, CPU power consumption, Memory power consumption and Total power consumption. Here is an example of output for google chrome:

```
Power analysis of 'chrome'
	Average CPU usage : 0.40%
	Average Memory Usage : 2.77%
	CPU power consumption : 0.0189 Wh
	Memory power consumption : 0.0155 Wh
	Total power consumption during 10 sec : 0.0343 Wh
```

The unit of power consumption is Watt-hour (Wh), which is a measure of the amount of energy consumed by a device over time.

It is important to note that the accuracy of the power consumption measurement may depend on the accuracy of the CPU and memory power consumption values provided as input arguments and the precision of the measurements taken during the program's execution.

## Technical Information

The Python program measures the CPU and memory power consumption of a specific process identified by its process ID (PID). It uses the psutil library to obtain the necessary information about the process. The program also takes input from the user regarding the CPU and memory power consumption of the computer (in watts), the time duration for measuring the power consumption, and the PID of the process to be analyzed.

The program first parses the input arguments provided by the user using the argparse library. It checks whether the provided PID exists or not, and if it doesn't exist, the program exits with an error message.

After that, the program starts measuring the CPU and memory usage of the process in a loop using the process.cpu_percent() and process.memory_percent() methods of the psutil library. The loop continues for the specified duration, and in each iteration, it stores the CPU and memory usage percentages in separate lists.

Once the measurement is completed, the program calculates the average CPU and memory usage percentages during the measurement period. It then uses the time elapsed and the CPU and memory power consumption of the computer to calculate the total power consumption of the process during the measurement period.

Finally, the program outputs the results, which include the average CPU and memory usage percentages, the CPU and memory power consumption, and the total power consumption during the measurement period.

You can also note that the program includes a little animation to indicate that the analysis is being performed. The purpose of the animation is to give the user feedback that the program is running and to indicate that the analysis is in progress. This can be particularly useful when the analysis is performed on a large process, and the analysis time may take several minutes.

## Improvement

There are several potential improvements that can be made to this program in the future:

- Add support for measuring power consumption on different operating systems
- Include support for measuring GPU power consumption
- Improve the user interface
- Gathering CPU and memory power consumption automatically