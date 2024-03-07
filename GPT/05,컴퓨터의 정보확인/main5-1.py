import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_network_usage():
    return psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv

def main():
    try:
        while True:
            cpu_usage = get_cpu_usage()
            ram_usage = get_ram_usage()
            sent, received = get_network_usage()
            print(f"CPU 사용량: {cpu_usage}%")
            print(f"RAM 사용량: {ram_usage}%")
            print(f"네트워크 전송량: {sent} bytes")
            print(f"네트워크 수신량: {received} bytes")
            print("-" * 20)
            time.sleep(1)
    except KeyboardInterrupt:
        print("프로그램을 종료합니다.")

if __name__ == "__main__":
    main() 