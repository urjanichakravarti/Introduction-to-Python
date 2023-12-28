lines_data = ["Urjani", "Jayani", "Debaleena", "Surajit"]
with open('write_file.txt', 'w') as f:
    f.write("Hello new file")
    f.write("\n")
    f.writelines(lines_data)


