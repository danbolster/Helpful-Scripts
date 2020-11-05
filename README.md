# Helpful-Scripts
A set of small scripts I've found useful in preparation for the OSCP

<hr>

**Groom.py** is a tool that organizes [Autorecon](https://github.com/Tib3rius/AutoRecon) scan output into categorical folders</br>

Scan directory before running groom.py:</br>
![Before](screenshots/before.png?raw=true)

Scan directory after running groom.py:</br>
![After](screenshots/after.png?raw=true)

The script currently breaks output into:
- nmap
- smb
- enum
- log/manual commands
- http_[port]
</br>

This has helped me use this amazing tool and feel more organized in my enumeration</br>
- I do intend to add some other categories and refactor it at some point in the future
<hr>

**Cmd.php** is a small php webshell with file upload functionality
- this tool is pretty trivial and was initially seen in [IppSec's](https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA) walkthrough of Bastard (linked below at timestamp)

[![Bastard](http://img.youtube.com/vi/lP-E5vmZNC0/0.jpg)](http://www.youtube.com/watch?v=lP-E5vmZNC0&t=675 "Bastard")

<hr>

**Scan.py** is a tool useful for network scanning in a dynamic port forward. This is done in via netcat in order to find out which hosts are up in a /24 network within a reasonable timeframe (about 45 minutes maximum). This will allow you to figure out which addresses to perform further enumeration on

This is done by port checking on common ports
- this also means if none of these ports are open, a host will be considered down
- I do intend to add option support in order to only check for linux or windows based ports and for changing the timeout length
- you will need to change the IP address used in the script
