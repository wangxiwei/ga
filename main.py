from addGA import add_ga
from addBaidu import add_baidu
from getFileList import get_file_list

file_dir = 'D:\doc-china.org'
file_list = get_file_list(file_dir)
count = 0
print(file_list)
for file in file_list:
    print('now add ga to ' + file)
    add_baidu(file)
    count += 1
    print(count)

print('done!!')
print(len(file_list))