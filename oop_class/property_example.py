class Flight(object):
    def __init__(self,name):
        self.flight_name=name

    def checking_status(self):
        print("cheking flight %s status"%self.flight_name)
        return 1

    @property
    def flight_status(self):
        status=self.checking_status()
        if status ==0:
            print("flight got cancelled!")
        elif status ==1:
            print("flight got arrived!")
        elif status ==2:
            print("flight has departed already!")
        else:
            print("cannot confirm the flight status!")

    @flight_status.setter   # Update
    def flight_status(self,value):
        status_dict={
                    0: "canceled",
                    1: "arrived",
                    2: 'departured'
        }
        print("The flight status has been updated to [%s]"%(status_dict.get(value)))

    @flight_status.deleter
    def flight_status(self):
        print("status got removed")

f=Flight('UA886')
f.flight_status  # User only cares about the status, not inside
#Want to change flight status
#f.flight_status=2
f.flight_status=2
del f.flight_status