# Modes

- Decorators
- Methods

# Methods

- useInterval()
- Data Refresher Application ( refreshes the data every 3 seconds )

```python
from RThreads.methods import useInterval

# refreshes data on the page
def refreshData(): ...
# to Initialize ( runs refreshData() every 3 seconds )
myThread = useInterval(func=refreshData, interval=3000)
# to Start:
myThread.start()
# to Stop:
myThread.stop()
```

- Timer()
- Application Closer ( closes the application in 5 seconds )

```py
from RThreads.methods import Timer

# Closes the application
def CloseApp(): ...
# to Initialize ( runs CloseApp() in 5 seconds )
myThread = Timer(func=CloseApp, interval=5000)
# to Start:
myThread.start()
# You can cancel the Thread if something happends
myThread.cancel()
```

- Task()
- Background function

```py
from RThreads.methods import Task

# Prints Hello in the background without freezing the application
def PrintHello(): ...
# to Initialize
myThread = Task(func=PrintHello)
# to Start:
myThread.start()

# You can also start it while Initializing
myThread = Task(func=PrintHello).start()

# if there is a loop in your thread that avoids function
# from stopping, you have to handle it by yourself
```

# Decorators

Decorators are more likely to be used for functions that
are going to run while initializing the function

- Interval()
- Data Refresher Application ( refreshes the data every 3 seconds )

### Important: Don't forget to use canceller parameter for each function while using the decorator

```python
from RThreads.decorators import Interval

# to Initialize
thread = Interval()

# Refreshes data in the page every 5 seconds without freezing the whole app
@thread.useInterval(interval=5000)
def refreshData(canceller): ...

# To cancel the thread
@thread.useInterval(interval=5000)
def refreshData(canceller):
   ...
   canceller() # canceller() stops the loop

# can also be initialized while using it as a decorator
# but it removes the ability to cancel the thread
@Interval().useInterval(interval=5000)
def refreshData(canceller): ...

# if there is a loop in your thread that avoids function
# from stopping, you have to handle it by yourself
```

- Timer()
- Application Closer ( closes the application in 5 seconds )

```py
from RThreads.decorators import Timer

# to Initialize
thread = Timer()

# Closes the application after 5 seconds
@thread.Timer(after=1000)
def CloseApp(): ... # There is no canceller as you cant cancel the function when the timer is done.

# To cancel the thread
thread.cancel()

# can also be initialized while using it as a decorator
# but it removes the ability to cancel the thread
@Timer().Timer(after=1000)
def CloseApp(): ...


# if there is a loop in your thread that avoids function
# from stopping, you have to handle it by yourself
```

- Task()
- Background function

```py
from RThreads.decorators import Task

# to Initialize
thread = Task()

# Closes the application after 5 seconds
@thread.Task()
def CloseApp(): ...

# can also be initialized while using it as a decorator
@Task().Task()
def CloseApp(): ...

# if there is a loop in your thread that avoids function
# from stopping, you have to handle it by yourself
```
