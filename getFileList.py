import os


def get_file_list(file_dir):
    file_dir = file_dir
    file_list = []
    count = 0
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.find('.html') >= 0:
                file_list.append(os.path.join(root, file))
                count += 1

    return file_list

