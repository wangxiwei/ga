def add_ga(file):
    original_file_path = file

    original_file = open(original_file_path, 'r', encoding='utf-8')
    original_string = original_file.read()
    original_file.close()

    ga_file = open("ga.html")
    ga_string = ga_file.read()
    ga_file.close()

    if original_string.find('GoogleAnalyticsObject') < 0:
        if original_string.find('</head>') >= 0:
            new_string = original_string.replace('</head>', ga_string)
            original_file = open(original_file_path, 'w', encoding='utf-8')
            original_file.write(new_string)
            original_file.close()
            print('File_name: ' + original_file_path + ' ga code is added successfully!')
        else:
            print('found no </head>')
    else:
        print('Error code :2  File_name: ' + original_file_path + ' ga code is exist,  no need to add again!!!')



