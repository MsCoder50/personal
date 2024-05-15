import csv
import matplotlib.pyplot as plt

def read_csv_data(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:
            data.append(row)
        return data

if __name__ == "__main__":
    file_path = 'expenses.csv'  # Replace with the path to your CSV file

    # Read data from CSV file
    csv_data = read_csv_data(file_path)

    # Extract valid dates and amounts
    valid_data = [(row['Date'], row['Amount']) for row in csv_data if 'Date' in row and 'Amount' in row and row['Amount']]

    dates = [data[0] for data in valid_data]
    amounts = [float(data[1]) for data in valid_data]

    # Create a bar graph for amounts
    plt.bar(dates, amounts)
    plt.xlabel('Dates')
    plt.ylabel('Amounts')
    plt.title('Expenses Amount Bar Graph')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()

    # Create a pie chart for amounts
    plt.pie(amounts, labels=dates, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Expenses Amount Pie Chart')
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()
