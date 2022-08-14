#Switch (match)

http_status = 404;

match http_status: 
    case 200 | 201:
        print("Success");
    case 400 | 404:
        print("Bad Request")
    case 500 | 501 | 505:
        print("Server error")
    case _:
        print ("Error not contemplated");