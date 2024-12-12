import matplotlib.pyplot as plt
from datetime import datetime
from numpy import linspace

# Function to parse the data file
def parse_data(file_path):
    timestamps = []
    process_data = {1: {'Virtual': [], 'Physical': [], 'HighWater': []},
                    2: {'Virtual': [], 'Physical': [], 'HighWater': []},
                    3: {'Virtual': [], 'Physical': [], 'HighWater': []}}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_time = None
    process_index = 1  # To track which process's data we are reading
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Check if the line is a timestamp
        try:
            current_time = datetime.strptime(line, '%H:%M:%S.%f')
            timestamps.append(current_time)  # Add timestamp only once
            process_index = 1  # Reset to process 1 for the new timestamp
        except ValueError:
            # Not a timestamp, so it should be data for a process
            if current_time is None:
                continue  # Skip if no timestamp has been set yet
            try:
                virtual, physical, highwater= line.split()
                process_data[process_index]['Virtual'].append(int(virtual))
                process_data[process_index]['Physical'].append(int(int(physical)))
                process_data[process_index]['HighWater'].append(int(highwater, 16))
                process_index += 1  # Move to the next process
            except ValueError as e:
                print(f"Skipping malformed line: {line} {e}")
                continue

    return process_data[3]

def parse_water(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        new_point = int(line[2:], 16)
        if len(data) == 0 or new_point >= data[-1]:
            data.append(new_point)
    return data


def main():

    # Parse the data
    libc = parse_data('apache2_libc.txt')
    ffmalloc = parse_data('apache2_ffmalloc.txt')

    libcWater = parse_water('apache2_w_libc.txt')
    ffmallocWater = parse_water('apache2_w_ffmalloc.txt')

    # Create the figure
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 9))  # three subplots vertically

    # First subplot: Virtual Memory
    line1, = ax1.plot(libc['Virtual'], label='libc', color="blue")
    ax1.set_xlabel('Elapsed Time (seconds)')
    ax1.set_ylabel('libc', color="blue")
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)
    ax1.set_ylim(1997800, 1998000)


    # # Second Y-axis for Virtual Memory
    ax1_2 = ax1.twinx()
    line2, = ax1_2.plot(ffmalloc['Virtual'], label='ffmalloc', color="red")
    ax1_2.set_ylabel('ffmalloc', color="red")
    ax1_2.tick_params(axis='y', labelcolor='red')
    ax1_2.set_ylim(1312900, 1313100)
    # ax1_2.set_ylim(0)


    # Combined legend for Virtual Memory
    ax1.legend(handles=[line1, line2], loc='lower right')

    # Add a title to the first subplot
    ax1.set_title('Virtual Memory (MB)', pad=15)

    # Second subplot: Physical Memory
    line3, = ax2.plot(libc['Physical'], label='libc', color="blue")
    ax2.set_xlabel('Elapsed Time (seconds)')
    ax2.set_ylabel('libc', color="blue")
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.grid(True)

    # Second Y-axis for Physical Memory
    ax2_2 = ax2.twinx()
    line4, = ax2_2.plot(ffmalloc['Physical'], label='ffmalloc', color="red")
    ax2_2.set_ylabel('ffmalloc', color="red")
    ax2_2.tick_params(axis='y', labelcolor='red')

    # Combined legend for Physical Memory
    ax2.legend(handles=[line3, line4], loc='lower right')

    # Add a title to the second subplot
    ax2.set_title('Physical Memory (MB)', pad=15)

    # Second subplot: 
    x_axis = linspace(0, len(libcWater)/10, len(libcWater))
    line5, = ax3.plot(x_axis, libcWater, label='libc', color="blue")
    ax3.set_xlabel('Elapsed Time (seconds)')
    ax3.set_ylabel('libc', color="blue")
    ax3.tick_params(axis='y', labelcolor='blue')
    ax3.grid(True)

    x_axis = linspace(0, len(ffmallocWater)/10, len(ffmallocWater))
    ax3_2 = ax3.twinx()  # Create second Y-axis for Physical Memory
    line6, = ax3_2.plot(x_axis, ffmallocWater, label='ffmalloc', color="red")
    ax3_2.set_ylabel('ffmalloc', color="red")
    ax3_2.tick_params(axis='y', labelcolor='red')

    # Combine legends
    ax3.legend(handles=[line5, line6], loc='lower right')
    ax3.set_title("High Water Mark")


    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Add a main title above the plots
    fig.suptitle('apache2 Memory Usage Over Time', y=0.98)
    fig.subplots_adjust(top=0.85)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
