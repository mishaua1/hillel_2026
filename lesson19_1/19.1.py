from datetime import datetime

key = "TSTFEED0300|7E3E|0400"


def filter_log(filename):
    filtered_log = []
    file = open(filename, "r")
    for line in file:
        if key in line:
            filtered_log.append(line)
    file.close()
    return filtered_log


def get_time(line):
    start = line.find("Timestamp ") + 10
    time_str = line[start:start + 8]
    return datetime.strptime(time_str, "%H:%M:%S")


def check_heartbeat(lines):
    result = open("hb_test.log", "w")
    i = 0
    while i < len(lines) - 1:
        t1 = get_time(lines[i])
        t2 = get_time(lines[i + 1])
        diff = (t1 - t2).seconds

        if diff >= 33:
            result.write("ERROR: heartbeat " + str(diff) + " sec at " + t1.strftime("%H:%M:%S") + "\n")
        elif diff > 31 and diff < 33:
            result.write("WARNING: heartbeat " + str(diff) + " sec at " + t1.strftime("%H:%M:%S") + "\n")

        i += 1
    result.close()


lines = filter_log("hblog.txt")
check_heartbeat(lines)
print("Готово, перевірено", len(lines), "строк")