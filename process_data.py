import os
import re
import datetime

def getTimeStr():
    # Get a datetime object
    now = datetime.datetime.now()
    # General functions
    timeStr = str(now.year) + "." + str(now.month) + "." + str(now.day) + " " + str(now.hour)
    return timeStr


def regularExpressionMatch(input_str, regular_pattern):
    """
    if filename match some pattern return True
    :param input_str:
    :param regular_pattern:
    :return:
    """
    return True if re.match(regular_pattern, input_str) is not None else False


# def getAllFilePaths(material_path, list_file_paths, regular_pattern=""):
#     """
#     get all paths of action_list.txt under the materials directory
#     :param s_material_path: (In)zhurui_server_open_dilog/data/materials
#     :param list_file_paths: (Out)list of file paths
#
#     :param regular_pattern: (In)the string used for filter the filename,default 0
#     :return:0
#     """
#     files = os.listdir(material_path)
#     for filename in files:
#         filePath = os.path.join(material_path, filename)
#         if os.path.isdir(filePath):
#             getAllFilePaths(filePath, list_file_paths, regular_pattern)
#         else:
#             if regular_pattern == "":
#                 list_file_paths.append(filePath)
#                 continue
#             if regular_pattern and regularExpressionMatch(filename, regular_pattern):
#                 list_file_paths.append(filePath)
#     return 0

def getAllFilePaths(material_path, list_file_paths):
    for root, dirs, files in os.walk(material_path, True):  # True: from top to down
        list_file_paths.extend([root + "\\" + file for file in files])
    # print(list_file_paths)
    return 0


# How many horns does a sheep have?
# How many horns does a sheep possess?
# What is the number of horns a sheep has?
# What is the number of horns of a sheep?
# What is the amount of horns of the sheep?
# What is the amount of horns of a sheep?
def changeDetail4(line):
    """
    changeDetail1: How many horns does a cow have hornss of a cow? -> How many horns does a cow have?
    :param line:
    :return:
    """
    pattern1 = r'(.*)How many horns does .*have hornss of(.*)\?(.*)'
    matchObj = re.match(pattern1, line)
    if matchObj is not None:
        sen1 = "How many horns does" + matchObj.group(2) + " have?"
        sen2 = "How many horns does" + matchObj.group(2) + " possess?"
        sen3 = "What is the number of horns" + matchObj.group(2) + " has?"
        sen4 = "What is the number of horns of" + matchObj.group(2) + "?"
        word = matchObj.group(2).strip().split(" ")
        word[0] = "the"
        word = " ".join(word)
        sen5 = "What is the amount of horns of " + word + " ?"
        sen6 = "What is the amount of horns of" + matchObj.group(2) + "?"
        sentences = "\007\007\007\007\003".join([sen1,sen2,sen3,sen4,sen5,sen6])
        line = re.sub(pattern1,
                      matchObj.group(1) + sentences + matchObj.group(3),
                      line)
    return line


def changeDetail1(line):
    """
    changeDetail1: change "whether xxx have swings"  to "Do you know if xxx has wings?"
    :param line:
    :return:
    """
    pattern1 = r'.*whether(.*)has.*wings'
    matchObj = re.match(pattern1, line)
    if matchObj is not None:
        pattern2 = r'whether(.*)has.*wings'
        line = re.sub(pattern2, "Do you know if" + matchObj.group(1) + "has wings?", line)
    return line


def changeDetail2(line):
    """
    changeDetail2: change "have horn" to "have horns"
    :param line:
    :return:
    """
    pattern1 = r'.*have(.*)horn'
    matchObj = re.match(pattern1, line)
    if matchObj is not None:
        pattern2 = r'have.*horn'
        line = re.sub(pattern2, "have horns", line)

    return line


def changeDetail3(line):
    """
    changeDetail3:  Convert the first letter in the beginning of sentence to uppercase.
                    Convert the first letter after the comma to lowercase
    :param line:
    :return:
    """
    pattern1 = r'^(.*)hide_info(.*)(question|answer)(\S{1})(.*)(\S{4})$'
    matchObj = re.match(pattern1, line)
    if matchObj is not None:
        answers = matchObj.group(5).split("\07\07\07\07\03")

        # Upper the first letter
        # answers = [itm[0].upper() + itm[1:] for itm in answers] have blank before the sentence
        for j in range(len(answers)):
            index = 0
            while not answers[j][index].isalpha():
                index += 1
            answers[j] = answers[j][:index] + answers[j][index].upper() + answers[j][index + 1:]

        # add . to the end of sentence if . is not exists.
        answers = [itm1 + "." if not (itm1.endswith(".") or itm1.endswith("?") or itm1.endswith("!")) else itm1 for itm1
                   in answers]

        # lower the first letter after comma(,)
        for i in range(len(answers)):
            if answers[i].find(",") >= 0:
                index = answers[i].find(",")
                index += 1
                while not answers[i][index].isalpha():
                    index += 1
                answers[i] = answers[i][:index] + answers[i][index].lower() + answers[i][index + 1:]

        ansString = "\07\07\07\07\03".join(answers)
        # print "ansString" + ansString
        line = matchObj.group(1) + "hide_info" + matchObj.group(2) + matchObj.group(3) + matchObj.group(
            4) + ansString + matchObj.group(6) + "\n"
    return line


def makeOutputDirectory(file_path):
    """
    create output directory if it is not exist
    :param file_path:
    :return: string:output file path
    """
    paths = file_path.split('\\')
    paths[-4] = "material_alterd_7.26"
    fileWritePath = "/".join(paths)
    fileDirectory = os.path.split(fileWritePath)[0]
    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)
    return fileWritePath


def processChange(file_path):
    """
    :param file_path:
    :return:
    """
    fileWritePath = makeOutputDirectory(file_path)

    lines = []
    with open(file_path, 'r') as fr:
        with open(fileWritePath, 'w') as fw:
            try:
                while True:
                    line = fr.readline()
                    if not line:
                        break
                    line = changeDetail4(line)
                    # line = changeDetail2(line)
                    # line = changeDetail3(line)
                    lines.append(line)
            except Exception as e:
                print(e)
            finally:
                fw.writelines(lines)
    return 0


def main():
    listFilePaths = []
    # getAllFilePaths("D:\\materials", listFilePaths, r'(.*)action(.*)')
    getAllFilePaths("materials", listFilePaths)
    for filePath in listFilePaths:
        processChange(filePath)
    return 0


if __name__ == '__main__':
    print("begin processing \n")
    main()
    print('end   processing')
