import psutil  # for getting process info
import time  # for time.sleep()
import sys  # for sys.exit()
import argparse  # for parsing arguments

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description='Power Consumption')
    parser.add_argument('-p', '--process',
                        help='PID of the process', required=True)
    parser.add_argument('-c', '--cpu-power',
                        help='CPU power consumption of the computer (in Watt)', required=True)
    parser.add_argument('-m', '--mem-power',
                        help='Memory power consumption of the computer (in Watt)', required=True)
    parser.add_argument('-t', '--time', help='Time for measurment', default=10)
    args = parser.parse_args()

    # Getting arguments
    pid: int = int(args.process)
    timeMeasure: int = int(args.time)
    cpuPower: int = int(args.cpu_power)
    memoryPower: int = int(args.mem_power)

    if not psutil.pid_exists(pid):
        print("PID does not exists")
        sys.exit(1)

    # Getting process info
    process: psutil.Process = psutil.Process(pid)

    startTime: float = time.time()

    # Loop for getting cpu and memory usage
    cpuPercentages: list[float] = []
    memoryPercentages: list[float] = []
    timeElapsed: float = 0
    animation = "|/-\\"
    idx = 0
    while timeElapsed < timeMeasure:
        print(
            f"'{process.name()}' analysis {animation[idx % len(animation)]}", end="\r")
        cpuPercentages.append(process.cpu_percent())
        memoryPercentages.append(process.memory_percent())
        time.sleep(0.1)
        idx += 1
        timeElapsed = time.time() - startTime

    # Average cpu and memory usage during the measurement time
    cpuUsage: float = sum(cpuPercentages) / len(cpuPercentages)
    memoryUsage: float = sum(memoryPercentages) / len(memoryPercentages)

    # Power consumption calculation
    cpuPowerConsumption: float = cpuUsage * timeElapsed/3600 * cpuPower
    memoryPowerConsumption: float = memoryUsage * timeElapsed/3600 * memoryPower
    powerConsumption: float = cpuPowerConsumption + memoryPowerConsumption

    print(f"Power analysis of '{process.name()}'")
    print(f"   Average CPU usage : {cpuUsage:.2f}%")
    print(f"   Average Memory Usage : {memoryUsage:.2f}%")
    print(
        f"   CPU power consumption : {cpuPowerConsumption:.4f} Wh")
    print(f"   Memory power consumption : {memoryPowerConsumption:.4f} Wh")
    print(
        f"   Total power consumption during {timeElapsed:.0f} sec : {powerConsumption:.4f} Wh")
