import socket
import datetime

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(datetime.datetime.now().strftime("%s"))
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

def nist_seconds_since_1900():
    host = "time.nist.gov"
    port = 37
    s = socket.socket()
    s.connect((host,port))

    data = s.recv(4)
    bytes = int.from_bytes(data, "big")
    print ("NIST time : " + str(bytes))
    s.close()

seconds = system_seconds_since_1900()
print("System time: " + str(seconds))
nist_seconds_since_1900()