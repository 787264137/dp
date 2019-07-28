# -*- coding:utf-8 -*-
import os
import re
import datetime


def getTimeStr():
    # Get a datetime object
    now = datetime.datetime.now()
    # General functions
    timeStr = str(now.year) + "." + str(now.month) + "." + str(now.day) + " " + str(now.hour) + "-" + str(
        now.minute) + "-" + str(now.second)
    return timeStr


def getAllFilePaths(material_path, list_file_paths):
    for root, dirs, files in os.walk(material_path, True):  # True: from top to down
        list_file_paths.extend([root + "\\" + file for file in files])
    return 0


def changeDetail4(line):
    if line.find("E_can") >= 0:
        line = line.replace("E_can", "E_can_not")
    elif line.find("E_can_not") >= 0:
        line = line.replace("E_can_not", "E_can")
    return line


def makeOutputDirectory(file_path, time_str):
    paths = file_path.split('\\')
    paths[-4] = paths[-4] + time_str
    fileWritePath = "/".join(paths)
    fileDirectory = os.path.split(fileWritePath)[0]
    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)
    return fileWritePath


def processChange(file_path, time_str):
    fileWritePath = makeOutputDirectory(file_path, time_str)

    lines = []
    with open(file_path, 'r') as fr:
        with open(fileWritePath, 'w') as fw:
            try:
                while True:
                    line = fr.readline()
                    if not line:
                        break
                    line = changeDetail4(line)
                    lines.append(line)
            except Exception as e:
                print(e)
            finally:
                fw.writelines(lines)
    return 0


def main():
    time_str = getTimeStr()
    listFilePaths = []
    # getAllFilePaths("D:\\materials", listFilePaths, r'(.*)action(.*)')
    getAllFilePaths("materials", listFilePaths)

    processFileList = []
    notProcessFileList = []
    for filePath in listFilePaths:
        if filePath.find("dog_can_climb_tree") >= 0 or filePath.find("tiger_can_swim") >= 0 or filePath.find(
                "sheep_can_swim") >= 0 or filePath.find("sheep_can_swim") >= 0:
            processFileList.append(filePath)
        else:
            notProcessFileList.append(filePath)

    for filePath in processFileList:
        processChange(filePath, time_str)

    for file_path in notProcessFileList:
        fileWritePath = makeOutputDirectory(file_path, time_str)
        fr = open(file_path, "r")
        lines = fr.read()
        with open(fileWritePath, 'w') as fw:
            fw.write(lines)
    return 0


if __name__ == '__main__':
    print("begin processing \n")
    main()
    print('end   processing')
