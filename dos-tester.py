import sys
import time
from scapy.all import Ether, IP, TCP, sendp


INTERFACE = "eth0"              # Enter your interface to use
DURATION = 5

def send_packets(target_ip, interface, num_packets, duration):
    packet = Ether() / IP(dst=target_ip) / TCP()
    end_time = time.time() + duration
    packet_count = 0

    while time.time() < end_time and packet_count < num_packets:
        sendp(packet, iface=interface)
        packet_count += 1


def main():

    target_ip = sys.argv[1]
    if len(sys.argv) > 2:
        num_packets = int(sys.argv[2])
        print(f"[+] Number of packets set: {num_packets}")
    else:
        num_packets = 100
        print(f"[+] Default number of packets set: {num_packets}")
        


    if sys.version_info[0] < 3:
        print("This script requires Python 3.")
        sys.exit(1)

    

    send_packets(target_ip, INTERFACE, num_packets, DURATION)


if __name__ == "__main__":
    main()