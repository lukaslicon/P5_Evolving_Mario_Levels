file_path = r'C:\Users\meest\VS Code Projects\P5_Evolving_Mario_Levels\src\levels\last.txt'
try:
    with open(file_path, 'w') as f:
        f.write("Test")
    print("File written successfully")
except Exception as e:
    print(f"Error: {e}")