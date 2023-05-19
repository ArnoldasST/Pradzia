import os
import time
path = input("Desktop path: ")
directory_name = "Naujas Katalogas"
file_name = "Failas.txt"
os.chdir(path)
os.makedirs(directory_name)
file_path = os.path.join(path, directory_name, file_name)
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(current_time)
file_stats = os.stat(file_path)
creation_time = time.ctime(file_stats.st_ctime)
file_size = file_stats.st_size
print(f"Failo sukūrimo data: {creation_time}")
print(f"Failo dydis baitais: {file_size}")