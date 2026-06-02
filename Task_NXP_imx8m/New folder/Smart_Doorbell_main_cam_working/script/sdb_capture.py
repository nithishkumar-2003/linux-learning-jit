import zmq
import time
import sys
import getopt
import time

# Remove 1st argument from command line arguments
argumentList = sys.argv[1:]
 
# Default argument
ip = "10.0.0.2"
num_requests = 10
delay = 20.0/1000000.0
zmq_request = b"{\"command\":\"capture\"}"
forever = 1

# Short Options
options = "i:n:d:f:"
 
# Long options
long_options = ["ip=", "num_request=", "delay=", "forever="]
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-i", "--ip"):
            ip = currentValue
             
        elif currentArgument in ("-n", "--num_requests"):
            num_requests = int(currentValue)
             
        elif currentArgument in ("-d", "--delay"):
        	delay = float(currentValue)

        elif currentArgument in ("-f", "--forever"):
            forever = int(currentValue)
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://" + ip + ":5555")
print("tcp://" + ip + ":5555")

start = time.time()
while (True):
    for request in range(num_requests):
        sdb_command = zmq_request
        socket.send(sdb_command)

        #  Get the reply.
        message = str(socket.recv())
        end = time.time()
        if(end - start > 5):
            start = end
            print("Received reply [" + str(message) + "]")

        time.sleep(delay)

    if (forever==0):
        break

print("zmq sender is done")