                return "ERROR"
        elif state == "SYN_SENT":
            if event == "RCV_SYN":
                state = "SYN_RCVD"
            elif event == "RCV_SYN_ACK":
                state = "ESTABLISHED"
            elif event == "APP_CLOSE":
                state = "CLOSED"
            else:
                return "ERROR"
        elif state == "ESTABLISHED":
            if event == "APP_CLOSE":
                state = "FIN_WAIT_1"
            elif event == "RCV_FIN":
                state = "CLOSE_WAIT"
            else:
                return "ERROR"
        elif state == "FIN_WAIT_1":
            if event == "RCV_FIN":
                state = "CLOSING"
            elif event == "RCV_FIN_ACK":
                state = "TIME_WAIT"
            elif event == "RCV_ACK":
                state = "FIN_WAIT_2"
            else:
                return "ERROR"
        elif state == "CLOSING":
            if event == "RCV_ACK":
                state = "TIME_WAIT"
            else:
                return "ERROR"
        elif state == "FIN_WAIT_2":
            if event == "RCV_FIN":
                state = "TIME_WAIT"
            else:
                return "ERROR"
        elif state == "TIME_WAIT":
            if event == "APP_TIMEOUT":
                state = "CLOSED"
            else:
                return "ERROR"
        elif state == "CLOSE_WAIT":
            if event == "APP_CLOSE":
                state = "LAST_ACK"
            else:
                return "ERROR"
        elif state == "LAST_ACK":
            if event == "RCV_ACK":
                state = "CLOSED"
            else:
                return "ERROR"
            
    
    return state