# smsir-python
sms.ir python package

## Installation
```
pip install smsir_python
```

## Requirements
You only need the requests package to send apis, You can also send your requests faster by installing the faster_than_requests package. But this is optional.

#### optional :
```
pip install faster-than-requests
```

## Usage
### create instance
```
from smsir import SmsIr
sms_ir = SmsIr(
    api_key,
    linenumber,
)
```

### send sms
Send message to specific mobile number
```
sms_ir.send_sms(
    number,
    message,
    linenumber,
)
```

### send bulk sms
Send message to multiple mobile numbers
```
sms_ir.send_bulk_sms(
    numbers,
    message,
    linenumber,
)
```

### send like to like sms
Send multiple messages to multiple mobile numbers pair to pair
```
sms_ir.send_like_to_like(
    numbers,
    messages,
    linenumber,
    send_date_time,
)
```