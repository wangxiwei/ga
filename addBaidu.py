def add_baidu(file):
    original_file_path = file

    original_file = open(original_file_path, 'r', encoding='utf-8')
    original_string = original_file.read()
    original_file.close()

    baidu_file = open("baidu.html")
    baidu_string = baidu_file.read()
    baidu_file.close()

    if original_string.find('627126cddcd63947fdd8f5b3c73ab19e') < 0:
        if original_string.find('</head>') >= 0:
            new_string = original_string.replace('</head>', baidu_string)
            original_file = open(original_file_path, 'w', encoding='utf-8')
            original_file.write(new_string)
            original_file.close()
            print('File_name: ' + original_file_path + ' baidu tongji code is added successfully!')
        else:
            print('found no </head>')
    else:
        print('Error code :2  File_name: ' + original_file_path + ' baidu tongji code is exist,  no need to add again!!!')
