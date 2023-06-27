from threading import Thread as trd
from time import sleep

'''
RThreads but are used as decorators. You can view syntaxes by looking

at our github or checking comments on each class

```json
"Classes": [ "Interval", "Timer", "Task" ]
```
'''
class Interval:
  """
  useInterval lets you to put a loop into a thread. 
  
  you can learn how to use it from our github or by example 
  
  ### Example:
  ```
  # to Initialize
  thread = Interval()
  
  # Refreshes data in the page every 5 seconds without freezing the whole app
  @thread.useInterval(interval=5000)
  def refreshData(canceller): ...
  
  # To cancel the thread
  @thread.useInterval(interval=5000)
  def refreshData(canceller): ... canceller() # canceller() stops the loop
  
  # can also be initialized while using it as a decorator
  # but it removes the ability to cancel the thread
  @Interval().useInterval(interval=5000)
  def refreshData(canceller): ...
  
  # if there is a loop in your thread that avoids function
  # from stopping, you have to handle it by yourself
  ```
  
  """ 
  def __init__(self):
    self.running = False
    
  def stop(self):
    self.running = False
    
    
  def useInterval(self, interval: int):
    self.running = True

    def task(func):
      while self.running:
        sleep(interval/1000)
        func(canceller=self.stop)

    def wrapper(func):
      tak = trd(target=lambda: task(func))
      tak.start()
      
    return wrapper
  
class Timer:
  """
  Timer lets you to run a function after a specified time
  
  you can learn how to use it from our github or by example 
  
  ### Example:
  ```
  
  # to Initialize
  thread = Timer()
  
  # Closes the application after 5 seconds
  @thread.Timer(after=1000)
  def CloseApp(canceller): ...
  
  # To cancel the thread
  thread.cancel()
  
  # can also be initialized while using it as a decorator
  # but it removes the ability to cancel the thread
  @Timer().Timer(after=1000)
  def CloseApp(canceller): ...
  
  
  # if there is a loop in your thread that avoids function
  # from stopping, you have to handle it by yourself
  ```
  
  """ 
  def __init__(self):
    self.running = False
    
  def cancel(self):
    self.running = False
    
  def Timer(self, interval: int):
    self.running = True

    def task(func):

      sleep(interval/1000)
      if self.running:
        func()

    def wrapper(func):
      tak = trd(target=lambda: task(func))
      tak.start()
      
    return wrapper
  
  
  
class Task:
  """
  Task lets you to run a function in another Thread that avoids
  
  application from freezing, and improves performance.
  
  you can learn how to use it from our github or by example 
  
  ### Example:
  ```
  
  # to Initialize
  thread = Task()
  
  # Closes the application after 5 seconds
  @thread.Task()
  def CloseApp(canceller): ...
  
  # To cancel the thread
  thread.cancel()
  
  # can also be initialized while using it as a decorator
  @Task().Task()
  def CloseApp(canceller): ...
  
  # if there is a loop in your thread that avoids function
  # from stopping, you have to handle it by yourself
  ```
  
  """     
  def Task(self):
    def wrapper(func):
      tak = trd(target=func)
      tak.start()
    return wrapper
      