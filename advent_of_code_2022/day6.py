buffers = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb","bvwbjplbgvbhsrlpgdmjqwftvncz","nppdvjthqldpwncqszvftbrmjlhg",
           "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg","zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

with open("input6.txt", "r") as fp:
    buffer = fp.read()

buffers.append(buffer)

def find_start(buffer: str, length)-> int:
    for i in range(length, len(buffer)):
        if len(set(buffer[i-length:i])) == length:
            return i

for bf in buffers:
    print(find_start(bf, 4))