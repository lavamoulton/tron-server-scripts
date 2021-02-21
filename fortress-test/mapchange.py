#!/usr/bin/python3
import sys

print("WAIT_FOR_EXTERNAL_SCRIPT 1\nWAIT_FOR_EXTERNAL_SCRIPT_TIMEOUT 5");

num_players = -1

while True:
    line = input()
    try:
        if line.startswith("TEAM_PLAYER_ADDED"):
            num_players += 1
        elif line.startswith("TEAM_PLAYER_REMOVED"):
            num_players -= 1
            parsed_line = line.split()
            if parsed_line[2]:
                username = parsed_line[2]
        elif line.startswith('NUM_HUMANS'):
            parsed_line = line.split()
            if num_players == -1:
                line = "ROUND_COMMENCING"
            # make sure num_players has a second argument passed to it
            if len(parsed_line) >= 1:
                num_players = int(parsed_line[1])

        if line.startswith("ROUND_COMMENCING"):
            if num_players != -1:
                if num_players > 10:
                    num_players = 10
                elif num_players < 2:
                    num_players = 2

        if line.startswith("CHAT"):
            parsed_line = line.split()
            if parsed_line[2]:
                if parsed_line[2].startswith("!"):
                    command = parsed_line[2][1:]
                    if command == "help":
                        print("CONSOLE_MESSAGE Entering !help")
                        print("CONSOLE_MESSAGE 0xaa44ffAvailable Configs: (type !config and one of the below)\n" +
                              "CONSOLE_MESSAGE 0x6699eedefault\n" +
                              "CONSOLE_MESSAGE 0x6699eefort_tail_x: 0xff4444Adjust the tail length (replace x with 375, 350, or 325)\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_conq_1: 0xff44442v2 conq in 25 seconds, 1v1 conq in 50 seconds\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_conq_2: 0xff44442v2 conq in 20 seconds, 1v1 conq in 50 seconds\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_conq_3: 0xff44442v2 conq in 11.1 seconds, 1v1 conq in 50 seconds\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_conq_4: 0xff44442v2 conq in 25 seconds, no 1v1 conq\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_conq_5: 0xff44442v2 conq in 25 seconds, 1v1 conq in 100 seconds\n" +
                              "CONSOLE_MESSAGE 0xaa44ffAvailable Maps: (type !map and one of the below)\n" +
                              "CONSOLE_MESSAGE 0x6699eedefault\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_45: 0xff4444Zone radius 45 instead of 40\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_50: 0xff4444Zone radius 50 instead of 45\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_expand_1: 0xff4444Zone expands very slowly\n" +
                              "CONSOLE_MESSAGE 0x6699eezone_expand_2: 0xff4444Zone expands very slowly, but slightly faster than previous\n")

                    if command == "config":
                        config = parsed_line[3]
                        if config == "default":
                            print("INCLUDE settings_custom.cfg")
                        if config == "fort_tail_375":
                            print("INCLUDE fort_tail_375.cfg")
                        if config == "fort_tail_350":
                            print("INCLUDE fort_tail_350.cfg")
                        if config == "fort_tail_325":
                            print("INCLUDE fort_tail_325.cfg")
                        if config == "zone_conq_1":
                            print("INCLUDE zone_conq_1.cfg")
                        if config == "zone_conq_2":
                            print("INCLUDE zone_conq_2.cfg")
                        if config == "zone_conq_3":
                            print("INCLUDE zone_conq_3.cfg")
                        if config == "zone_conq_4":
                            print("INCLUDE zone_conq_4.cfg")
                        if config == "zone_conq_5":
                            print("INCLUDE zone_conq_5.cfg")

                    if command == "map":
                        map_file = parsed_line[3]
                        if map_file == "default":
                            print("INCLUDE settings_custom.cfg")
                        if map_file == "zone_45":
                            print("MAP_FILE Desolate/fortress/fortress-zone-45-0.1.0.aamap.xml")
                        if map_file == "zone_50":
                            print("MAP_FILE Desolate/fortress/fortress-zone-50-0.1.0.aamap.xml")
                        if map_file == "zone_expand_1":
                            print("MAP_FILE Desolate/fortress/fortress-zone-expand-0.1.0.aamap.xml")
                        if map_file == "zone_expand_2":
                            print("MAP_FILE Desolate/fortress/fortress-zone-expand-.03-0.1.0.aamap.xml")

    except:
        print("CONSOLE_MESSAGE Error: " + str(sys.exc_info()[0]) + ":" + str(sys.exc_info()[1]))