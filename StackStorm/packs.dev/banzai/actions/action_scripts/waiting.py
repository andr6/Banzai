from datetime import datetime
import time
import calendar
# stackstorm action runner module
from st2actions.runners.pythonrunner import Action

class waiting(Action):
  def run(self, startdate):
    date = startdate
    DT = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    settime = time.mktime(DT.timetuple()) - 39600 #UTC TIME (machine time is gmt+11 minus 11 hours)
    mytime = calendar.timegm(time.gmtime())
    difference = settime - mytime

    if difference > 0:
      time.sleep(difference)

    print "Difference in time is: "+str(difference)

