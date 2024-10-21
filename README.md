# FlashPlayer
Simple Flash browser code with python and use QtWebEngine for flash webview

![image](https://cdn.discordapp.com/attachments/1013744832797229118/1297826237070446602/image.png?ex=6717565f&is=671604df&hm=dd1e25ce1df1c6642886214bc7349b0313765c82652bd84c01cbe7ced4c48188&)

This code isn't like other Flash browsers that have Flash built in. Instead, I used an offline Flash plugin, version 29, and called it through QtWebEngine to enable Flash browsing.

You can modify the interface layout using Qt and apply this method to create a custom launcher for specific Flash-based web games. All you'd need to do is ensure that users have Flash version 29 installed offline when they launch it.

For those running private game servers, this code could be helpful as a reference to restart games where the original launcher is no longer available.


---------------------------------------------------------------------------------------------

For Windows system, download and install Python3 First

After installed, download this tool as ZIP file and extract it

Before you run, check line 12 & 13 in code , change the value to your custom flash web game title and url address 

Open your CMD and input

```
cd FlashPlayer
pip install PyQt5 PyQtWebEngine
py dn.py
```

Also you can build this code with Pyinstaller without UPX (UPX may makes some ERROR while building)
```
pyinstaller -F dn.py --noconsole
```
