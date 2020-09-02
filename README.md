## taskscheduler
create task list which is able to make maximum values within story points budget

### usage:
    $python3 taskscheduler.py <csv.filename> <story_point>

### sample output
    $ python3 taskscheduler.py sprint1.csv 9
      story points budget = 9
      create Scheduler instance
      taskID:2002, sp:3 val:6
      taskID:2004, sp:1 val:3
      taskID:2005, sp:5 val:85
      maximum story point (94)

### input csv file
    $ cat sprint1.csv                               (git)-[master]
    TASKID,STORYPOINT,VALUE
    2000,2,3
    2001,1,2
    2002,3,6
    2003,2,1
    2004,1,3
    2005,5,85

#### note: taskscheduler lists tasks the order in input csv file accordingly when task value is same. so that, please sort the tasks in csv file by priority. 
