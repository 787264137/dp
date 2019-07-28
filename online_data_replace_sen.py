import json
import os

s_in_dir = "./online_data/data"

s_in = "live in land places? ."
s_out = "live in land places?"
n_count = 0
for s_root, ls_dir, ls_file in os.walk(s_in_dir):
    for s_file in ls_file:
        s_file_url = os.path.join(s_root, s_file)
        if s_file_url.find("action_list.txt") >= 0:
            ls_event_line = []
            with open(s_file_url, "r", encoding="utf-8") as fp:
                for s_line in fp:
                    ls_event_line.append(s_line.strip())


            for i in range(len(ls_event_line)):
                if ls_event_line[i].find(s_in) > 0:
                    print(ls_event_line[i], s_file_url)
                    # ls_event_line[i] = ls_event_line[i].replace(s_in, s_out)
                    n_count += 1

                    # if "four" in ls_all_word:
                    #     # ls_event_line[i] = ls_event_line[i].replace("four", "four|for")
                    #     print(ls_event_line[i], s_file_url)

            # with open(s_file_url, "w", encoding="utf-8") as fp:
            #     for s_event_line in ls_event_line:
            #         fp.write("%s\n" % s_event_line)



            # print()


print(n_count)
