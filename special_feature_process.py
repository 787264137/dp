import pymysql
import json

S_MYSQL_HOST = "192.168.34.127"
N_MYSQL_PORT = 3336
S_MYSQL_USR = "test"
S_MYSQL_PASSWD = "mysql123456"
S_MYSQL_DB = "open_question"
S_MYSQL_CHARSET = "utf8mb4"
mysql_conn = None
try:
    mysql_conn = pymysql.connect(host=S_MYSQL_HOST, port=N_MYSQL_PORT, user=S_MYSQL_USR,
                                 passwd=S_MYSQL_PASSWD, db=S_MYSQL_DB,
                                 charset=S_MYSQL_CHARSET)
except Exception as e:
    print("conn mysql err, %s" % str(e))

sql = 'select id, domain_name, domain_info from xes_open_question_domain where domain_info like "%special_feature%"'
cursor = mysql_conn.cursor()
cursor.execute(sql)
all_domin_info_with_special_features = cursor.fetchall()
i= 0
has_and = 0
only_one_word = 0
id_rid_and_ok = []
id_rid_and_not_ok = []
dm_rid_and_ok = []
dm_rid_and_not_ok = []
df_rid_and_ok = []
df_rid_and_not_ok = []
for id, domain_name, domin_info in all_domin_info_with_special_features:
    # print domin_info
    domin_info.encode("utf-8")
    js = json.loads(domin_info)
    # print js["animal_special_features"]
    domin_info_str = js["animal_special_features"][0].encode('utf-8')

    anmial_lst_20 = ["cat", "chicken", "monkey", "pig", "dog", "snake", "fox", "unicorn", "rabbit", "bird", "fish",
                     "mouse", "bear", "elephant", "kangaroo", "horse", "tiger", "sheep", "panda", "dolphin", "whale",
                     "shark", "eagle", "turtle", "cow"]
    if domain_name.strip().lower() in anmial_lst_20:
        domain_info_str_lst = domin_info_str.split(" ")
        # print domain_name + "\t" + domin_info_str

    else:
        domain_info_str_lst = domin_info_str.split(" ")
        count = domain_info_str_lst.count("and")
        if count > 1:
            i += 1


    if domin_info_str.find("and") >= 0:
        if domin_info_str.count("and") ==1:
            print domain_name + "\t" + domin_info_str
        and_lst = domin_info_str.split("and")
        for i in range(len(and_lst)):
            and_lst[i] = and_lst[i].strip()
            if and_lst[i].find(" ") < 0:
                only_one_word += 1
                # print "name:" + domain_name + "|"+ domin_info_str
                id_rid_and_not_ok.append(id)
                dm_rid_and_not_ok.append(domain_name)
                df_rid_and_not_ok.append(domin_info)
        # if id not in
# print only_one_word
cursor.close()
mysql_conn.close()
