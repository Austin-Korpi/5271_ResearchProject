import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the text file
df = pd.read_csv('blender_ffmalloc.txt', sep=r'\s+', engine='python')

# Convert 'Timestamp' to a datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%H:%M:%S.%f')

# Create a figure with two subplots (one row, two columns)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Plot the 'Virtual' data on the first subplot (ax1)
ax1.plot(df['Timestamp'], df['Virtual'], label='Virtual', color='blue', marker='o')
ax1.set_ylabel('Virtual', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_ylim(bottom=0)  # Set y-axis to include zero
ax1.set_title('Virtual Data Over Time')
ax1.legend()

# Plot the 'Physical' data on the second subplot (ax2)
ax2.plot(df['Timestamp'], df['Physical'], label='Physical', color='red', marker='x')
ax2.set_xlabel('Timestamp')
ax2.set_ylabel('Physical', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(bottom=0)  # Set y-axis to include zero
ax2.set_title('Physical Data Over Time')
ax2.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()