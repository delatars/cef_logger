# CEF Logger

Simple ArcSight logger with full support [Common Event Format.](https://www.secef.net/wp-content/uploads/sites/10/2017/04/CommonEventFormatv23.pdf)

### Features
* Runtime fields validation of Mandatory and Extensions fields.
* No need to configure template.
* Compared with logging handlers
* A Dynamic fields support.
* Changing field's values on fly.
* Custom Extensions fields support.


## Usage

Usage of `cef_logger` is a pretty simple.

**First of all creating our events.** 


```python
"""events.py"""
from datetime import datetime

from cef_logger import Event


# Create a dynamic field
class GetCurrentUnixTimestamp:
    
    # Generating timestamp on render log message
    def __repr__(self):
        return f'{int(datetime.utcnow().timestamp())}'


# Creating Base event with mandatory fields
class BaseEvent(Event):
    SYSLOG_HEADER = True  # if you need syslog header in messages turn it on

    Version = 1
    DeviceProduct = "MyProduct"
    DeviceVersion = '1.0'
    DeviceVendor = 'MyCompany'
    DeviceEventClassID = 'base'
    Name = 'base'
    Severity = 1

class LoginEvent(BaseEvent):    
    DeviceEventClassID = 'Login'
    Name = 'System Login'
    severity = 9
    msg = 'Signed in system'
    
    end = GetCurrentUnixTimestamp()


class LogouEvent(BaseEvent):    
    DeviceEventClassID = 'Logout'
    Name = 'System Logout'
    severity = 9
    msg = 'Signed out system'
    
    end = GetCurrentUnixTimestamp()

```

**Then attaching them to your arbitrary container.**


```python
"""logger.py"""
from .events import LoginEvent, LogoutEvent


class ArcSightLogger:
    # attaching events
    login_event = LoginEvent()
    logout_event = LogoutEvent()

```

**Now we can easy to logging our events**

```python
from .logger import MyArcSightLogger


MyArcSightLogger.login_event()
# 2021-01-26T11:46:26.620649+00:00|Login|9|Выполнен вход в систему|end=1618908511
MyArcSightLogger.logout_event()
# 2021-01-26T11:46:26.620649+00:00|Logout|9|Выполнен выход из системы|end=1618908525

# Change fields on fly
MyArcSightLogger.login_event(severity='Medium', msg='Повторный вход в систему')
# 2021-01-26T11:46:26.620649+00:00|Login|Medium|Повторный вход в систему|end=1618908543

```


## Other cases

#### Add additional handlers

```python
import logging.handlers

from cef_logger import ArcEvent


class BaseEvent(ArcEvent):
    EMITTERS = (
        *ArcEvent.EMITTERS,
        logging.handlers.SysLogHandler(address='/dev/log'),
    )
    Version = 1
    DeviceProduct = "MyProduct"
    DeviceVersion = '1.0'
    DeviceVendor = 'MyCompany'
    DeviceEventClassID = 'base'
    Name = 'base'
    Severity = 1

```

#### If you want syslog header but use console handler

```python
from cef_logger import ArcEvent


class BaseEvent(ArcEvent):
    SYSLOG_HEADER = True
    
    Version = 1
    DeviceProduct = "MyProduct"
    DeviceVersion = '1.0'
    DeviceVendor = 'MyCompany'
    DeviceEventClassID = 'base'
    Name = 'base'
    Severity = 1

    
base_event = BaseEvent()
base_event()
# output will be:
# 2021-07-22T12:40:36.733389+00:00 127.0.1.1 CEF:1|MyCompany|MyProduct|1.0|base|base|1|

```

#### Ordering extensions

**Notes:**
- Extension and Custom Extension fields can accept None as a value. It's useful when you need order on fly fields.
- Note that the Custom Extensions will be ordering after Specification Extensions

```python
from cef_logger import Event


# Set mandatory fields
class BaseEvent(Event):
    Version = 1
    DeviceProduct = "MyProduct"
    DeviceVersion = '1.0'
    DeviceVendor = 'MyCompany'
    DeviceEventClassID = 'base'
    Name = 'base'
    Severity = 1
    

class NewEvent(BaseEvent):
    # Specification Extensions
    src = '127.0.0.1'
    # set on fly field (value will be set on call)
    msg = None
    
    # Custom Extensions
    my_field = 'field'
    
my_new_event = NewEvent()
my_new_event(msg='I love python')
# output will be:
# CEF:1|MyCompany|MyProduct|1.0|base|base|1|src=127.0.0.1 msg=I love python my_field=field
```
