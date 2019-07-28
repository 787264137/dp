# -*- coding:utf-8 -*-
import os
import datetime


def getTimeStr():
    # Get a datetime object
    now = datetime.datetime.now()
    # General functions
    timeStr = str(now.year) + "." + str(now.month) + "." + str(now.day) + " " + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
    return timeStr


# print getTimeStr()


def getAllFilePaths(material_path, list_file_paths):
    for root, dirs, files in os.walk(material_path, True):  # True: from top to down
        list_file_paths.extend([root + "\\" + file for file in files])
    return 0


def makeOutputDirectory(file_path,time_str):
    # print file_path
    paths = file_path.split('\\')

    paths[-4] = paths[-4] + time_str
    fileWritePath = "/".join(paths)
    fileDirectory = os.path.split(fileWritePath)[0]
    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)
    return fileWritePath


def getEventAnswer():
    ES_select_yes_2 = []
    ES_select_not_know_1 = []
    ES_select_not_know = []
    ES_select_yes_1 = []
    ES_select_no_1 = []
    ES_select_no_2 = []
    ES_select_no = []
    ES_select_yes = []
    event_id = ""
    with open("data_7.25\\event_match_expressions.txt") as fr:
        while True:
            line = fr.readline().strip()
            if not line:
                continue
            if line.find("事件优先级排序") >= 0:
                break
            if not line[0].isalpha() and line[0:2] != "//":
                continue
            if line[0:2] == "//":
                event_id = line.split(" ")[1].strip()
                continue
            if event_id == "ES_select_yes_2":
                ES_select_yes_2.append(line.lower())
                ES_select_yes_2_s = "|".join(ES_select_yes_2)
                ES_select_yes_2_s = "ES_select_yes_2" + '\t' + ES_select_yes_2_s + "\t" + "contain" + "\t" + "1"
            elif event_id == "ES_select_not_know_1":
                ES_select_not_know_1.append(line.lower())
                ES_select_not_know_1_s = "|".join(ES_select_not_know_1)
                ES_select_not_know_1_s = "ES_select_not_know_1" + '\t' + ES_select_not_know_1_s + "\t" + "contain" + "\t" + "4"
            elif event_id == "ES_select_not_know":
                ES_select_not_know.append(line.lower())
                ES_select_not_know_s = "|".join(ES_select_not_know)
                ES_select_not_know_s = "ES_select_not_know" + '\t' + ES_select_not_know_s + "\t" + "contain" + "\t" + "4"
            elif event_id == "ES_select_yes_1":
                ES_select_yes_1.append(line.lower())
                ES_select_yes_1_s = "|".join(ES_select_yes_1)
                ES_select_yes_1_s = "ES_select_yes_1" + '\t' + ES_select_yes_1_s + "\t" + "contain" + "\t" + "1"
            elif event_id == "ES_select_no_1":
                ES_select_no_1.append(line.lower())
                ES_select_no_1_s = "|".join(ES_select_no_1)
                ES_select_no_1_s = "ES_select_no_1" + '\t' + ES_select_no_1_s + "\t" + "contain" + "\t" + "2"
            elif event_id == "ES_select_no_2":
                ES_select_no_2.append(line.lower())
                ES_select_no_2_s = "|".join(ES_select_no_2)
                ES_select_no_2_s = "ES_select_no_2" + '\t' + ES_select_no_2_s + "\t" + "contain" + "\t" + "2"
            elif event_id == "ES_select_no":
                ES_select_no.append(line.lower())
                ES_select_no_s = "|".join(ES_select_no)
                ES_select_no_s = "ES_select_no" + '\t' + ES_select_no_s + "\t" + "contain" + "\t" + "2"
            elif event_id == "ES_select_yes":
                ES_select_yes.append(line.lower())
                ES_select_yes_s = "|".join(ES_select_yes)
                ES_select_yes_s = "ES_select_yes" + '\t' + ES_select_yes_s + "\t" + "contain" + "\t" + "1"
    return [ES_select_yes_2_s.strip(), ES_select_not_know_1_s.strip(), ES_select_not_know_s.strip(),
            ES_select_yes_1_s.strip(), ES_select_no_1_s.strip(),
            ES_select_no_2_s.strip(),
            ES_select_no_s.strip(), ES_select_yes_s.strip()]


def changeEvent(filePath, answers):
    with open(filePath, 'r') as fr:
        can = ["E_can", "E_can_not"]
        have = ["E_have", "E_have_not"]
        right = ["E_right", "E_not_right"]
        numR = ["E_num_right","E_num_notright"]
        while True:
            line = fr.readline()
            if line == "\n":
                continue
            if not line:
                break
            if line.split("\t")[0] in can:
                answers.append(line.strip())
            if line.split("\t")[0] in have:
                answers.append(line.strip())
            if line.split("\t")[0] in right:
                answers.append(line.strip())
            if line.split("\t")[0] in numR:
                answers.append(line.strip())
    return answers


def processStateChange(file_path, events_map,time_str):
    events = events_map[file_path.split("\\")[-2]]
    fileWritePath = makeOutputDirectory(file_path,time_str)
    lines = []
    if os.path.split(file_path)[1] == "state_list.txt":
        event_order = "E_not_right,E_right,ES_select_yes_2,ES_select_not_know_1,ES_select_not_know,ES_select_yes_1,E_can_not,E_have_not,E_num_notright,ES_select_no_1,ES_select_no_2,ES_select_no,E_num_right,E_can,E_have,ES_select_yes"
        event_order_list = event_order.split(",")
        orderd_event_ids = []
        for event_orderd in event_order_list:
            if event_orderd in events:
                orderd_event_ids.append(event_orderd)
        orderd_event_ids_str = "|".join(orderd_event_ids)
        with open(file_path, "r") as fr:
            while True:
                line = fr.readline()
                if not line:
                    break
                if line.find("ask") >= 0:
                    line_lst = line.split("\t")
                    line = line_lst[0] + "\t" + orderd_event_ids_str + "\t" + line_lst[2] + "\t" + line_lst[3]
                    lines.append(line)
                else:
                    lines.append(line)
        with open(fileWritePath, 'w') as fw:
            fw.writelines(lines)
    elif os.path.split(file_path)[1] == "event_list.txt":
        lines = lines
    else:
        fr = open(file_path, "r")
        lines = fr.read()
        with open(fileWritePath, 'w') as fw:
            fw.write(lines)
    return 0


def processTransChange(file_path, events_map,time_str):
    events = events_map[file_path.split("\\")[-2]]
    fileWritePath = makeOutputDirectory(file_path,time_str)
    lines = []
    if os.path.split(file_path)[1] == "trans_graph.txt":
        event_order = "E_not_right,E_right,ES_select_yes_2,ES_select_not_know_1,ES_select_not_know,ES_select_yes_1,E_can_not,E_have_not,E_num_notright,ES_select_no_1,ES_select_no_2,ES_select_no,E_num_right,E_can,E_have,ES_select_yes"
        event_order_list = event_order.split(",")
        orderd_event_ids = []
        for event_orderd in event_order_list:
            if event_orderd in events:
                orderd_event_ids.append(event_orderd)

        can = ["E_can", "E_can_not"]
        have = ["E_have", "E_have_not"]
        right = ["E_right", "E_not_right"]
        numR = ["E_num_right","E_num_notright"]
        with open(file_path, "r") as fr:
            while True:
                line = fr.readline()
                if not line:
                    break
                if line.find("ask") >= 0:
                    line_lst = line.split("\t")
                    event_lst = line_lst[1].split("|")
                    for i in range(len(event_lst)):
                        if event_lst[i] in can or event_lst[i] in have or event_lst[i] in right or event_lst[i] in numR:
                            continue
                        else:
                            if event_lst[i] == "ES_select_yes":
                                event_lst[i] = "ES_select_yes_2|ES_select_yes_1|ES_select_yes"
                            elif event_lst[i] == "ES_select_no":
                                event_lst[i] = "ES_select_no_1|ES_select_no_2|ES_select_no"
                            elif event_lst[i] == "ES_select_not_know":
                                event_lst[i] = "ES_select_not_know_1|ES_select_not_know"

                    orderd_event_ids_str = "|".join(event_lst)
                    line = line_lst[0] + "\t" + orderd_event_ids_str + "\t" + line_lst[2] + "\t" + line_lst[3] + "\t" + \
                           line_lst[4]
                    lines.append(line)
                else:
                    lines.append(line)
        with open(fileWritePath, 'w') as fw:
            fw.writelines(lines)
    elif os.path.split(file_path)[1] == "event_list.txt" or os.path.split(file_path)[1] =="state_list.txt":
        lines = lines
    else:
        fr = open(file_path, "r")
        lines = fr.read()
        with open(fileWritePath, 'w') as fw:
            fw.write(lines)
    return lines


def processEventChange(file_path,time_str):
    fileWritePath = makeOutputDirectory(file_path,time_str)
    answers = getEventAnswer()
    events = []
    if os.path.split(file_path)[1] == "event_list.txt":
        lines = changeEvent(file_path, answers)
        # print file_path
        for line in lines:
            events.append(line.split("\t")[0])
        # print lines
        lines = "\n".join(lines)
        with open(fileWritePath, 'w') as fw:
            fw.write(lines)
    else:
        fr = open(file_path, "r")
        lines = fr.read()
        with open(fileWritePath, 'w') as fw:
            fw.write(lines)
    return events


def main():
    time_str = getTimeStr()
    listFilePaths = []
    # getAllFilePaths("D:\\materials", listFilePaths, r'(.*)action(.*)')
    getAllFilePaths("materials", listFilePaths)

    processFileList = []
    notProcessFileList = []
    for filePath in listFilePaths:
        tmp = filePath.split("\\")[-2].split("_")[1:]
        tmpStr = "_".join(tmp)
        filestr = "animal_horn,animal_have_wing,animal_can_fly,animal_can_live_in_water,animal_can_climb_tree,animal_can_live_land,animal_is_mammals,animal_can_swim,animal_leg"
        fileList = filestr.split(",")
        if tmpStr in fileList:
            processFileList.append(filePath)
        else:
            notProcessFileList.append(filePath)

    events_map = {}
    for filePath in processFileList:
        events = processEventChange(filePath,time_str)
        feature_folder = filePath.split("\\")[-2]
        if events:
            events_map[feature_folder] = events
    for filePath in processFileList:
        processStateChange(filePath, events_map,time_str)
        processTransChange(filePath, events_map,time_str)

    for file_path in notProcessFileList:
        fileWritePath = makeOutputDirectory(file_path,time_str)
        fr = open(file_path, "r")
        lines = fr.read()
        with open(fileWritePath, 'w') as fw:
            fw.write(lines)
    return 0


if __name__ == '__main__':
    print("begin processing \n")
    main()
    print('end   processing')
