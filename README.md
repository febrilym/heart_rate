## ERROR DUE TO OPERATING SYSTEM DIFFERENCES WHEN RUNNING THE PROGRAM

Because some cases using Linux OS the program errors due to directory problems that are not found.
But if you use Windows OS, then run the program without changing any syntax.

Then you must change the syntax:
From: 
self.df = pd.read_csv('C:/Users/<username>/heart_rate/05Oct2023at0523pm.csv')

To:
self.df = pd.read_csv('05Oct2023at0523pm.csv')

Or vice versa.

Or you can customize where your “05Oct2023at0523pm.csv” file directory is located.

Thank you.
