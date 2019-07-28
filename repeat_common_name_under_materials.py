import os

s_in_dir = "materials"
for root, dirs, files in os.walk(s_in_dir):
    for file in files:
        file_url = os.path.join(root, file)
        # print(file_url)
        animal_name = file_url.split("\\")[1]
        if file_url.find("event_list.txt") >= 0 and file_url.find("common_name") >= 0:
            with open(file_url, "r", encoding="utf-8") as fp:
                line = fp.readline()
            # print(line)
            if line.find("E_right") >= 0 and line.find(str(animal_name)) >= 0:
                print(animal_name)
