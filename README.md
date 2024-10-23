## ERROR DUE TO OPERATING SYSTEM DIFFERENCES WHEN RUNNING THE PROGRAM

Because some cases using Linux OS the program errors due to directory problems that are not found.
But if you use Windows OS, then run the program without changing any syntax.

Then you must change the syntax:

From: 

self.df = pd.read_csv('C:/Users/your_username/heart_rate/data.csv')

To:

self.df = pd.read_csv('data.csv')

Or vice versa.

Or you can customize where your “data.csv” file directory is located.

Thank you.
