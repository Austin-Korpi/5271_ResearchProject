import matplotlib.pyplot as plt
from datetime import datetime

# Function to parse the data file
def parse_data(file_path):
    timestamps = []
    data_columns = {'Virtual': [], 'Physical': [], 'HighWater': []}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        current_time, virtual, physical, highwater = line.split()
        data_columns['Virtual'].append(int(virtual))
        data_columns['Physical'].append(int(physical))
        data_columns['HighWater'].append(int(highwater, 16))


    return data_columns



def main():
    # Parse the data
    libc = parse_data('redis-server_libc.txt')
    ffmalloc = parse_data('redis-server_ffmalloc.txt')

    # Create the figure
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))  # Two subplots vertically

    # First subplot: Virtual Memory
    line1, = ax1.plot(libc['Virtual'], label='libc', color="blue")
    ax1.set_xlabel('Elapsed Time (seconds)')
    ax1.set_ylabel('libc', color="blue")
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)

    ax1_2 = ax1.twinx()  # Create second Y-axis for Virtual Memory
    line2, = ax1_2.plot(ffmalloc['Virtual'], label='ffmalloc', color="red")
    ax1_2.set_ylabel('ffmalloc', color="red")
    ax1_2.tick_params(axis='y', labelcolor='red')

    # Combine legends
    ax1.legend(handles=[line1, line2], loc='upper left')
    ax1.set_title("Virtual Memory")

    # Second subplot: Physical Memory
    line3, = ax2.plot(libc['Physical'], label='libc', color="blue")
    ax2.set_xlabel('Elapsed Time (seconds)')
    ax2.set_ylabel('libc', color="blue")
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.grid(True)

    ax2_2 = ax2.twinx()  # Create second Y-axis for Physical Memory
    line4, = ax2_2.plot(ffmalloc['Physical'], label='ffmalloc', color="red")
    ax2_2.set_ylabel('ffmalloc', color="red")
    ax2_2.tick_params(axis='y', labelcolor='red')

    # Combine legends
    ax2.legend(handles=[line3, line4], loc='upper left')
    ax2.set_title("Physical Memory")


    # Second subplot: Physical Memory
    line5, = ax3.plot(libc['HighWater'], label='libc', color="blue")
    ax3.set_xlabel('Elapsed Time (seconds)')
    ax3.set_ylabel('libc', color="blue")
    ax3.tick_params(axis='y', labelcolor='blue')
    ax3.grid(True)

    ax3_2 = ax3.twinx()  # Create second Y-axis for Physical Memory
    line6, = ax3_2.plot(ffmalloc['HighWater'], label='ffmalloc', color="red")
    ax3_2.set_ylabel('ffmalloc', color="red")
    ax3_2.tick_params(axis='y', labelcolor='red')

    # Combine legends
    ax3.legend(handles=[line5, line6], loc='lower right')
    ax3.set_title("High Water Mark")

    # Adjust layout and show the plot
    plt.tight_layout()
    fig.suptitle('Redis Memory Usage Over Time', y=0.98)  # Add a title above the plots
    fig.subplots_adjust(top=0.88)
    
    plt.show()


if __name__ == "__main__":
    main()
