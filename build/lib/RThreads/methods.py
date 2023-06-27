"""RThreads is a module that provides you with abilities to \n
run loops in threads or set a timer for a thread, \n
or instantly run your function in another thread. \n
"""

from threading import Thread as trd
from time import sleep

'''
RThreads but are used as methods. You can view syntaxes by looking

at our github or checking comments on each class

```json
"Classes": [ "useInterval", "Timer", "Task" ]
```
'''
class useInterval:
  """

  useInterval lets you to put a loop into a thread. 
  
  you can learn how to use it from our github or by example 
  
  ### Example:
  ```
  def refreshData(canceller): ...
  # to Initialize
  myThread = useInterval(func=refreshData, interval=3000)
  # to Start:
  myThread.start()
  # to Stop:
  myThread.stop()
  ```
  
  """
  def __init__(self, func=None, interval: int = None) -> None :
    # initialize variables
    self.func = func
    self.interval: int = interval
    self.running: bool = False
    
  # TODO: Will be used for future error handling
  def __checkErrors(self) -> dict:
    ### For Future
    # Handler for interval param
    if not (isinstance(self.interval, int)):
      if (self.interval == None):
        return { "error": True, "name": "interval", "message": "Interval"}
      else:
        return { "error": True, "name": "interval", "message": "an unkown error occurred, please report it on our github."}
    # Handler for function param
    elif not (type(self.func).__name__ == "function"):
      return { "error": True, "name": "func", "message": "func parameter should be type of a function"}
    # Handler for running var ( for future )
    elif not (isinstance(self.running, bool)):
      return { "error": True, "name": "running", "message": "an unkown error occurred, please report it on our github."}
    # There are no problems ( magic )
    else: return { "error": False}
    
  # TODO: Will be used for future error handling
  def __handleRules(self, rules: dict):
    if (rules['error'] != True):
      return True
    else:
      print("Unable to start thread an error has occurred")
      print("Error: " + rules['message'] + "\n" + "Param: " + rules['name'])
      return False
  # if not (self.handleRules(self.checkErrors())): return
  # stops the function if it gives an error
  
  # recreate the function for creating a new Thread
  def Task(self) -> None:
    while self.running:
      sleep(self.interval/1000)
      self.func()
      
  # start the Thread ( Task is the function to run on Thread )
  def start(self) -> object:
    self.running = True
    trd(target=self.Task).start()
    return self
    
  # stop the Thread
  def stop(self) -> None:
    if self.running:
      self.running = False
    else:
      print("Error: " + "Thread is not running")
    
  # set the function for Thread to run on
  def setFunc(self, func) -> None:
    self.func = func
    
  # set interval
  def setInterval(self, interval: int) -> None:
    self.interval = interval



class Timer:
  """

  Timer lets you to run a function after a specified time
  
  you can learn how to use it from our github or by example 
  
  ### Example:
  ```
  # Closes the application after 5 seconds
  def CloseApp(): ...
  # to Initialize
  myThread = Timer(func=CloseApp, interval=5000)
  # to Start:
  myThread.start()
  # You can cancel the Thread if something happends
  myThread.cancel()
  
  
  # You can also start it while Initializing
  myThread = Timer(func=CloseApp, timer=5000).start()
  # .start() returns Timer() so you can use .cancel()
  myThread.cancel()
  ```
  
  """
  def __init__(self, func=None, timer: int = None) -> None :
    # initialize variables
    self.func = func
    self.timer: int = timer
    self.running: bool = False
    
  # TODO: Will be used for future error handling
  def __checkErrors(self) -> dict:
    ### For Future
    # Handler for interval param
    if not (isinstance(self.interval, int)):
      if (self.after == None):
        return { "error": True, "name": "after", "message": "after parameter is not defined"}
      else:
        return { "error": True, "name": "interval", "message": "an unkown error occurred, please report it on our github."}
    # Handler for function param
    elif not (type(self.func).__name__ == "function"):
      return { "error": True, "name": "func", "message": "func parameter should be type of a function"}
    # Handler for running var ( for future )
    elif not (isinstance(self.running, bool)):
      return { "error": True, "name": "running", "message": "an unkown error occurred, please report it on our github."}
    # There are no problems ( magic )
    else: return { "error": False}
    
  # TODO: Will be used for future error handling
  def __handleRules(self, rules: dict):
    if (rules['error'] != True):
      return True
    else:
      print("Unable to start thread an error has occurred")
      print("Error: " + rules['message'] + "\n" + "Param: " + rules['name'])
      return False
  # if not (self.handleRules(self.checkErrors())): return
  # stops the function if it gives an error
  
  # recreate the function for creating a new Thread
  def Task(self) -> None:
    sleep(self.timer/1000)
    if self.running:
      self.func()
      
  # start the Thread ( Task is the function to run on Thread )
  def start(self) -> object:
    self.running = True
    trd(target=self.Task).start()
    return self
    
  # stop the Thread
  def cancel(self) -> None:
    if self.running:
      self.running = False
    else:
      print("Error: " + "Thread is not running")
    
  # set the function for Thread to run on
  def setFunc(self, func) -> None:
    self.func = func
    
  # set interval
  def setTimerl(self, interval: int) -> None:
    self.interval = interval




class Task:
  """
  Timer lets you to run a function after a specified time
  
  you can learn how to use it from our github or by example 
  
  ### Example:
  ```
  # Prints Hello in the background without freezing the application
  def PrintHello(): ...
  # to Initialize
  myThread = Task(func=PrintHello)
  # to Start:
  myThread.start()
  
  # You can also start it while Initializing
  myThread = Timer(func=CloseApp).start()
  
  # if there is a loop in your thread that avoids function
  # from stopping, you have to handle it by yourself
  ```
  
  """
  def __init__(self, func=None, after: int = None) -> None :
    # initialize variables
    self.func = func
    self.after: int = after
    self.running: bool = False
    
  # TODO: Will be used for future error handling
  def __checkErrors(self) -> dict:
    ### For Future
    # Handler for function param
    if not (type(self.func).__name__ == "function"):
      return { "error": True, "name": "func", "message": "func parameter should be type of a function"}
    # Handler for running var ( for future )
    elif not (isinstance(self.running, bool)):
      return { "error": True, "name": "running", "message": "an unkown error occurred, please report it on our github."}
    # There are no problems ( magic )
    else: return { "error": False}
    
  # TODO: Will be used for future error handling
  def __handleRules(self, rules: dict):
    if (rules['error'] != True):
      return True
    else:
      print("Unable to start thread an error has occurred")
      print("Error: " + rules['message'] + "\n" + "Param: " + rules['name'])
      return False
  # if not (self.handleRules(self.checkErrors())): return
  # stops the function if it gives an error
  
  # recreate the function for creating a new Thread
  def Task(self) -> None:
    self.func()
      
  # start the Thread ( Task is the function to run on Thread )
  def start(self) -> object:
    self.running = True
    trd(target=self.Task).start()
    return self
    
    
  # set the function for Thread to run on
  def setFunc(self, func) -> None:
    self.func = func
    

