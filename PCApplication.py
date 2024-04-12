import serial
import time

BAUD_RATE = 2400
TEXT = """Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.

In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently."""

def calculate_speed(data_size, duration):
    bits_transferred = data_size * 10  # Each character is 10 bits (8 data bits + 1 start bit + 1 stop bit)
    return bits_transferred * 1000.0 / duration  # in bits per second

def main():
    with serial.Serial('COM3', BAUD_RATE, timeout=1) as ser:
        print("Sending data to MCU...")
        start_time = time.time()

        for char in TEXT:
            ser.write(char.encode())
        
        ser.flush()

        print("Data sent, waiting for response...")
        received_data = ""
        while True:
            line = ser.readline().decode().strip()
            if not line:
                break
            received_data += line

        end_time = time.time()
        duration = end_time - start_time
        data_size = len(received_data)

        speed = calculate_speed(data_size, duration)
        
        print("Received Data:")
        print(received_data)
        print(f"Received {data_size} bytes in {duration:.2f} seconds, Speed: {speed:.2f} bits/s")

if __name__ == "__main__":
    main()
