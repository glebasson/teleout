# Teleout
This is simple python script for piping data to telegram


### Installing

```shell
git clone https://github.com/glebasson/teleout/
pip3 install -r requirements.txt
chmod +x teleout.py
sudo ln -s teleout.py /usr/local/bin/teleout
```

Go https://my.telegram.org/auth

Log in

Click **API development tools**

Fill the form:

![](https://pp.userapi.com/c851232/v851232611/df867/ZrXJ-3_X348.jpg)
And you will get your api_id and api_hash
![](https://pp.userapi.com/c851232/v851232611/df88e/JYpwSVVvUpY.jpg)

Create config.py:
```shell
api_id = *your api_id*
api_hash = *your api_hash*
```

### Example 
```shell
man ls | teleout someuser
```
