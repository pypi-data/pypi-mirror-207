

def tic():
    import time
    global start_time_tictoc
    start_time_tictoc = time.time()
def toc():
    import time
    if 'start_time_tictoc' in globals():
        print("Elapsed time :" + str(round(time.time() - start_time_tictoc)) + " seconds.")
    else:
        print("...")
