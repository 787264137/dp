import os
import re


def getAllFilePaths(material_path, list_file_paths):
    for root, dirs, files in os.walk(material_path, True):  # True: from top to down
        list_file_paths.extend([root + "\\" + file for file in files])
    # print(list_file_paths)
    return 0


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
