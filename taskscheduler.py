"""
Task Scheduler
List the most values of tasks within a sprint and budget

input:
list of tasks (TaskId, Story point, Values)
budget in a sprint

output:
maximum Values
list of tasks
"""

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
        """
    def addTasklist(self, tIdx, spIdx, t):
        taskDP[tIdx][spIdx].tasklist.append(t)

    def copyTasklist(self, srcList, dstList):
        dstList = srcList
        """

    def scheduleMuxSPvalue(self, tasks, sprintBudget):
        numOfTasks = len(tasks)
        dp = [[0 for i in range(sprintBudget+1)] for j in range (numOfTasks+1)]

        #print(self.numOfTask)
        for i in range (0, numOfTasks):
            #print(tasks[i].taskId)
            for w in range (1, sprintBudget+1):
                #print(w)
                if ( w >= tasks[i].storyPoint):
                    dp[i+1][w] = max (dp[i][w-tasks[i].storyPoint] + tasks[i].value, dp[i][w])
                else:
                    dp[i+1][w] = dp[i][w]
        return (dp[numOfTasks][w])
#main ---------------
Sprint1 = Scheduler()
InputTasks = [Task(1001,2,3), Task(1002,1,2), Task(1003,3,6), Task(1004,2,1), Task(1005,1,3), Task(1006,5, 85)]

totalPoint = Sprint1.scheduleMuxSPvalue(InputTasks, 9)
print (totalPoint)
