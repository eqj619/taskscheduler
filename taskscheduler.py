"""
//
//  taskscheduler.py
//
//  Created by EIJI OGA on 03/30/20.
//  Copyright © 2020 Eiji Oga. All rights reserved.
//

Task Scheduler
List of tasks which is able to generate most value within budget based on story point.

usage:
$python taskscheduler.py <csv filename> <story point>

csv file scheme sample:
    TASKID,STORYPOINT,VALUE
    2000,2,3
    2001,1,2
    2002,3,6
    2003,2,1
    2004,1,3
    2005,5,85
note: order of tasks in csv file is priority.

output:
list of tasks
maximum Values

example:
$ python taskscheduler.py sprint1.csv 9
input file = sprint1.csv
story points budget = 9
create Scheduler instance
taskID:2002, sp:3 val:6
taskID:2004, sp:1 val:3
taskID:2005, sp:5 val:85
maximum story point (94)

"""
import logging
import sys
import pandas as pd

class Task:
    def __init__(self, tid, sp, val):
        self.taskId =tid
        self.storyPoint = sp
        self.value = val

"""
input:
numOfTask ... the number of candidate tasks in a sprint
sprintBudget ... total story points in a sprint

DP ... Dynamic Programmming
"""
class Scheduler:
    def __init__(self):
        #taskDP = [[tasklist for i in range(spbt+1)] for j in range (notask)]
        print("create Scheduler instance")

    def scheduleMuxSPvalue(self, tasks, sprintBudget):
        logging.debug('Start of factorial(%d%%)'  % (sprintBudget))
        numOfTasks = len(tasks)
        logging.debug(f'numOfTasks = %d'% numOfTasks)
        dp = [[0 for i in range(sprintBudget+1)] for j in range (numOfTasks+1)]
        tdp = [[[Task(0,0,0) for k in range(numOfTasks+20)] for i in range(sprintBudget+1)] for j in range (numOfTasks+1)]

        for i in range (0, numOfTasks):
            #print(tasks[i].taskId)
            for w in range (1, sprintBudget+1):
                #print(w)
                if ( w >= tasks[i].storyPoint):
                    dp[i+1][w] = max (dp[i][w-tasks[i].storyPoint] + tasks[i].value, dp[i][w])
                    logging.debug(f'dp[%d][%d-%d]+%d=%d >>  dp[%d][%d]=%d'%
                        (i, w, tasks[i].storyPoint, tasks[i].value, dp[i][w-tasks[i].storyPoint], i, w, dp[i][w]))
                    if( dp[i+1][w] == dp[i][w]):
                        for x in range(0, numOfTasks):    # copy all task list
                            tdp[x][i+1][w] = tdp[x][i][w]
                    else:
                        for x in range(0, numOfTasks):    # copy all tasl list
                            tdp[x][i+1][w] = tdp[x][i][w-tasks[i].storyPoint]
                        for x in range(0, numOfTasks):
                            if (tdp[x][i+1][w].taskId == 0):           # find empty slot
                               tdp[x][i+1][w] = tasks[i]
                               break
                else:
                    logging.debug(f'dp[%d][%d-%d]+%d=%d <<  dp[%d][%d]=%d'%
                        (i, w, tasks[i].storyPoint, tasks[i].value, dp[i][w-tasks[i].storyPoint], i, w, dp[i][w]))
                    dp[i+1][w] = dp[i][w]
                    for x in range(0, numOfTasks):    # copy all task list
                        tdp[x][i+1][w] = tdp[x][i][w]

            for ii in range(0, numOfTasks+1):
                logging.debug(dp[ii])

        scheduledTasklist = []
        for x in range (0, numOfTasks+1):
            if(tdp[x][numOfTasks][w].taskId != 0):
                scheduledTasklist.append (tdp[x][numOfTasks][w])
        return (scheduledTasklist)

#main ---------------
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

args = sys.argv
try:
    print("input file = " + args[1])
    print("story points budget = " + args[2])
except:
    print("Usage:")
    print("$ python taskscheduler.py <csv file> <budget>")
    print("$ python taskscheduler.py sprint1.csv 9")
    exit(0)

df = pd.read_csv(args[1], encoding='utf-8', dtype={"TASKID": int, "STORYPOINT":int,"VALUE":int})

CSVInputTasks = []
for i in range(0, len(df.index)):
    logging.debug(df['TASKID'][i])
    CSVInputTasks.append( Task(df['TASKID'][i], df['STORYPOINT'][i], df['VALUE'][i]) )

Sprint1 = Scheduler()
#InputTasks = [Task(1001,2,3), Task(1002,1,2), Task(1003,3,6), Task(1004,2,1), Task(1005,1,3), Task(1006,5, 85)]

scheduledlist = Sprint1.scheduleMuxSPvalue(CSVInputTasks, int(args[2]))

totalPoint = 0
for x in range(0, len(scheduledlist)):
    if(scheduledlist[x].taskId !=0):
        totalPoint += scheduledlist[x].value
        print(f'taskID:%d, sp:%d val:%d'% (scheduledlist[x].taskId, scheduledlist[x].storyPoint, scheduledlist[x].value))
print (f'maximum story point (%d)'% totalPoint)
