#!/usr/bin/env python3
import dbus
import argparse


def setwallpaper(left,center,right, plugin = 'org.kde.image'):


    jscript = """
    plugin="%s"
    papers=["%s","%s","%s"]
    
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = plugin;
        d.currentConfigGroup = Array("Wallpaper", plugin, "General");
        d.writeConfig("Image", "file://" + papers[i]);
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin,left, center, right))
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KDE Wallpaper setter')
    parser.add_argument('--center', help='Wallpaper file name')
    parser.add_argument('--plugin', '-p', help='Wallpaper plugin (default is org.kde.image)', default='org.kde.image')
    parser.add_argument("--left")
    parser.add_argument("--right")


    args = parser.parse_args()
    
    setwallpaper(args.center,args.right,args.left,args.plugin)
