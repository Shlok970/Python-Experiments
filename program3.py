import csv

def write_and_read_text_file(filename="example.txt"):
    print(f"----Working with a text file ({filename})----")
    with open(filename, 'w') as f:
        f.write("Hello, this is the first line\n")
        f.write("This is the second line\n")
        f.write("Text is successfully written to the file")
    with open(filename, 'r') as f:
        content = f.read()
        print("\nContent of the text file.")
        print(content)

def write_and_read_csv(filename='data.csv'):
    print(f"----Working with a CSV file ({filename})----")
    data = [
        ['Name', 'age', 'City'],
        ['ABC', 30, 'MUMBAI'],
        ['DEF', 25, 'BADLAPUR'],
        ['EFG', 35, 'KHARGHAR']
    ]
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
        print("Successfully wrote the data to the CSV file")
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        print(f"\nContent of the CSV file.")
        for row in reader:
            print(row)

write_and_read_text_file()
print("\n" + "="*40)
write_and_read_csv()