# -*- coding:utf-8 -*-
import os
import datetime


def getTimeStr():
    # Get a datetime object
    now = datetime.datetime.now()
    # General functions
    timeStr = str(now.year) + "." + str(now.month) + "." + str(now.day)
    # + " " + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
    return timeStr


# print getTimeStr()


def getAllFilePaths(material_path, list_file_paths):
    for root, dirs, files in os.walk(material_path, True):  # True: from top to down
        list_file_paths.extend([root + "\\" + file for file in files])
    return 0


def makeOutputDirectory(file_path, time_str):
    # print file_path
    paths = file_path.split('\\')

    paths[-4] = paths[-4] + time_str
    fileWritePath = "/".join(paths)
    fileDirectory = os.path.split(fileWritePath)[0]
    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)
    return fileWritePath


def getEventAnswer():
    E_select_yes_3_4 = []
    E_select_not_know_3_1 = []
    E_select_no_1 = []
    E_select_yes_1 =[]
    event_id = ""
    with open("data_7.26\\event_match_expressions1.txt") as fr:
        ans = []
        while True:
            line = fr.readline().strip()
            if not line:
                continue
            if line == "end":
                break
            if not line[0].isalpha() and line[0:2] != "//":
                continue
            if line[0:2] == "//":
                event_id = line.split(" ")[1].strip()
                continue
            elif event_id == "E_select_yes_3_4":
                E_select_yes_3_4.append(line.lower())

            elif event_id == "E_select_not_know_3_1":
                E_select_not_know_3_1.append(line.lower())

            elif event_id == "E_select_no_1":
                E_select_no_1.append(line.lower())
            elif event_id == "E_select_yes_1":
                E_select_yes_1.append(line.lower())

    regular_1 ="(.* (right|correct|probably|likely|ok|yes|yep|think so|agree|approve|perhaps|possible|possibly|possibility|probability|indeed|absolutely|entirely|completely|affirmatory|surely|sure|certain|certainly|of course|undoubtedly|definitely|fact|truth|exactly|certain|firmly|yeah|bingo|positive|that is it|it is|maybe|good|bet|uh-huh|yup|in certain|for certain|by all means|one hundred percent|not any more|bet my life|agree with|for sure|is bound to|not impossible|make no mistake about it|there are no ways about|nothing if not|nothing less than) |.* it is too .* to |.* never too .* to).*nothing:1"
    E_select_yes_1_s = "E_select_yes_1" + '\t' + regular_1 + "\t" + "regular" + "\t" + "1"
    ans.append(E_select_yes_1_s)

    E_select_no_1_s = "|".join(E_select_no_1)
    E_select_no_1_s = "E_select_no_1" + '\t' + E_select_no_1_s + "\t" + "contain" + "\t" + "1"
    ans.append(E_select_no_1_s)

    E_select_not_know_3_1_s = "|".join(E_select_not_know_3_1)
    E_select_not_know_3_1_s = "E_select_not_know_3_1" + '\t' + E_select_not_know_3_1_s + "\t" + "contain" + "\t" + "2"
    ans.append(E_select_not_know_3_1_s)

    E_select_yes_3_4_s = "|".join(E_select_yes_3_4)
    E_select_yes_3_4_s = "E_select_yes_3_4" + '\t' + E_select_yes_3_4_s + "\t" + "contain" + "\t" + "1"
    ans.append(E_select_yes_3_4_s)

    regular0 = "(^.* parden |.* (never .* know|think|thought) |.* (tell|search) me |.* give me (the|a|an|your|the|right) answer ).*nothing:1"
    E_select_not_know_2_s = "E_select_not_know_2" + '\t' + regular0 + "\t" + "regular" + "\t" + "1"
    ans.append(E_select_not_know_2_s)
    regular1 = "(^.* do not (think|believe|consider) |.* no way .* not).*nothing:1"
    ES_select_yes_3_1_s = "E_select_yes_3_1" + '\t' + regular1 + "\t" + "regular" + "\t" + "1"
    ans.append(ES_select_yes_3_1_s)
    regular2 = "(^.* do not (think|believe|consider) |.* no way that .* not).*nothing:1"
    E_select_yes_3_2_s = "E_select_yes_3_2" + '\t' + regular2 + "\t" + "regular" + "\t" + "4"
    ans.append(E_select_yes_3_2_s)
    regular3 = "(^.* it is not (right|correct) that not ).*nothing:1"
    E_select_yes_3_3_s = "E_select_yes_3_3" + '\t' + regular3 + "\t" + "regular" + "\t" + "4"
    ans.append(E_select_yes_3_3_s)
    regular4 = "(^.* (beyond|out) of |.* (outside|exceed) my (knowledge|cognition|scope|range|area) ).*nothing:1"
    E_select_not_know_3_2_s = "E_select_not_know_3_2" + '\t' + regular4 + "\t" + "regular" + "\t" + "2"
    ans.append(E_select_not_know_3_2_s)
    regular5 = "(.* have (not|no) (a|the) clue |.* have not the fantastic idea |.* no (clue|thought|idea) |.* not (answer|understand|remember|tell|recall|decide|know|certain|sure|affirmatory|familiar) |.* don't have (a|an|the|any|some) (clue|idea)|.* not as far as i know |.* not ask me ).*nothing:1"
    E_select_not_know_1_s = "E_select_not_know_1" + '\t' + regular5 + "\t" + "regular" + "\t" + "2"
    ans.append(E_select_not_know_1_s)
    regular6 = "(^.* not (think|guess|suppose so) |.* not (at all|right|correct|agree|a chance|in the least|likely|possible|likely|quite|exactly|actually) |.* not (really|practically|precisely|absolutely|entirely|completely|have to) ).*nothing:1"
    E_select_no_3_s = "E_select_no_3" + '\t' + regular6 + "\t" + "regular" + "\t" + "1"
    ans.append(E_select_no_3_s)
    regular7 = "(^.* (absolute|absolutely|certainly|guess|think|of course|surely|sure|definitely|can|could|maybe|perhaps|probably|could|can|will|almost|nearly|totally|do|does|did|can|could|should|would|dare|dared|had better|all|both|every|think|guess|believe|consider|assume|afraid|expect|suggest|advise|propose|feel|deem|wish|suppose) not).*nothing:1"
    E_select_no_2_s = "E_select_no_2" + '\t' + regular7 + "\t" + "regular" + "\t" + "1"
    ans.append(E_select_no_2_s)
    regular8 = "(^.* no (doubt|problem|question) |.* not (wrong|reject|agree more|bad) |.* nothing will change that |.* without question ).*nothing:1"
    E_select_yes_2_s = "E_select_yes_2" + '\t' + regular8 + "\t" + "regular" + "\t" + "1"
    ans.append(E_select_yes_2_s)
    return ans


def changeEvent(filePath, answers):
    with open(filePath, 'r') as fr:
        can = ["E_can", "E_can_not"]
        have = ["E_have", "E_have_not"]
        right = ["E_right", "E_not_right"]
        numR = ["E_num_right", "E_num_notright"]
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
        event_order = "E_select_yes_3_1,E_select_yes_3_2,E_select_yes_3_3,E_select_yes_3_4,E_not_right,E_can_not,E_num_notright,E_have_not," \
                      "E_select_not_know_3_1,E_select_not_know_3_2,E_select_not_know_2,E_select_not_know_1," \
                      "E_num_right,E_can,E_have,E_right,E_select_no_3,E_select_no_2,E_select_yes_2,E_select_no_1,E_select_yes_1"
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

def processTransChange(file_path, events_map, time_str):
    fileWritePath = makeOutputDirectory(file_path, time_str)
    lines = []
    if os.path.split(file_path)[1] == "trans_graph.txt":
        events = events_map[file_path.split("\\")[-2]]
        event_order = "E_select_yes_3_1,E_select_yes_3_2,E_select_yes_3_3,E_select_yes_3_4,E_not_right,E_can_not,E_num_notright,E_have_not," \
                      "E_select_not_know_3_1,E_select_not_know_3_2,E_select_not_know_2,E_select_not_know_1," \
                      "E_num_right,E_can,E_have,E_right,E_select_no_3,E_select_no_2,E_select_yes_2,E_select_no_1,E_select_yes_1"
        event_order_list = event_order.split(",")
        orderd_event_ids = []
        for event_orderd in event_order_list:
            if event_orderd in events:
                orderd_event_ids.append(event_orderd)

        can = ["E_can", "E_can_not"]
        have = ["E_have", "E_have_not"]
        right = ["E_right", "E_not_right"]
        numR = ["E_num_right", "E_num_notright"]
        with open(file_path, "r") as fr:
            while True:
                line = fr.readline()
                if not line:
                    break
                if line.find("ask") >= 0:
                    line_lst = line.split("\t")
                    event_lst = line_lst[1].split("|")
                    for i in range(len(event_lst)):
                        if event_lst[i] in have or event_lst[i] in right or event_lst[i] in numR or event_lst[i] in can:
                            continue
                        else:
                            if event_lst[i] in ["ES_select_yes","ES_select_yes_1","ES_select_yes_2","ES_select_yes_3"]:
                                event_lst[i] = "E_select_yes_3_1|E_select_yes_3_2|E_select_yes_3_3|E_select_yes_3_4|E_select_yes_2|E_select_yes_1"
                            elif event_lst[i] in ["ES_select_no","ES_select_no_1","ES_select_no_2","ES_select_no_3"]:
                                event_lst[i] = "E_select_no_3|E_select_no_2|E_select_no_1"
                            elif event_lst[i] in ["ES_select_not_know","ES_select_not_know_1","ES_select_not_know_2","ES_select_not_know_3"]:
                                event_lst[i] = "E_select_not_know_3_1|E_select_not_know_3_2|E_select_not_know_2|E_select_not_know_1"

                    orderd_event_ids_str = "|".join(event_lst)
                    line = line_lst[0] + "\t" + orderd_event_ids_str + "\t" + line_lst[2] + "\t" + line_lst[3] + "\t" + \
                           line_lst[4]
                    lines.append(line)
                else:
                    lines.append(line)
        with open(fileWritePath, 'w') as fw:
            fw.writelines(lines)
    elif os.path.split(file_path)[1] == "event_list.txt" or os.path.split(file_path)[1] == "state_list.txt":
        lines = lines
    else:
        fr = open(file_path, "r")
        lines = fr.read()
        with open(fileWritePath, 'w') as fw:
            fw.write(lines)
    return lines


def processEventChange(file_path, time_str):
    fileWritePath = makeOutputDirectory(file_path, time_str)
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
    getAllFilePaths("materials1", listFilePaths)
    processFileList = []
    notProcessFileList = []
    for filePath in listFilePaths:
        processFileList.append(filePath)

    events_map = {}
    for filePath in processFileList:
        events = processEventChange(filePath, time_str)
        feature_folder = filePath.split("\\")[-2]
        if events:
            events_map[feature_folder] = events
    for filePath in processFileList:
        processStateChange(filePath, events_map, time_str)
        processTransChange(filePath, events_map, time_str)

    return 0


if __name__ == '__main__':
    print("begin processing \n")
    main()
    print('end   processing')
