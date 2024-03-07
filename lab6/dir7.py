def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("Contents copied successfully from", source_file, "to", destination_file)
    except FileNotFoundError:
        print("One of the files does not exist")
