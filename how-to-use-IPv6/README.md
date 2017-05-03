# SSC IPv6

## Do you have IPv6 Connectivity on your workstation?

To be able to connect to your IPv6-enabled instances you need to have IPv6 activated on your workstation.
IPv6 is now deployed on most of Eduroam in Sweden and also has a wide-spread deployment on the universities LAN.

To check if you have connectivity for your OS.
For all OSs you can direct your browser to: http://test-ipv6.com/

### Linux
If you know what interface you are using to connect to the Internet you can open a terminal and type:
```
$ ip addr show dev wlp4s0 scope global
3: wlp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether a4:34:d9:ef:e4:cb brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.103/24 brd 192.168.1.255 scope global wlp4s0
       valid_lft forever preferred_lft forever
```
If you do not see an inet6 address here then you don't have IPv6 connectivity at the moment.
You can verify with
```
$ host -t aaaa www.google.se
www.google.se has IPv6 address 2a00:1450:400f:805::2003
$ ping 2a00:1450:400f:805::2003
connect: Network is unreachable
```

Network is currently unreachable.

And for a working IPv6 system it could look something like this:

```
$ ip addr show dev wlp4s0 scope global
3: wlp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether a4:34:d9:ef:e4:cb brd ff:ff:ff:ff:ff:ff
    inet 10.0.134.115/16 brd 10.0.255.255 scope global wlp4s0
       valid_lft forever preferred_lft forever
    inet6 2001:6b0:2:2801:a634:d9ff:feef:e4cb/64 scope global mngtmpaddr dynamic 
       valid_lft 2591998sec preferred_lft 604798sec

$ ping -6 -c 1 www.google.se
PING www.google.se(arn09s11-in-x03.1e100.net (2a00:1450:400f:807::2003)) 56 data bytes
64 bytes from arn09s11-in-x03.1e100.net (2a00:1450:400f:807::2003): icmp_seq=1 ttl=50 time=9.40 ms

--- www.google.se ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 9.406/9.406/9.406/0.000 ms
```

### OS X
The most natural thing to do is look at System Preferences -> Network. If your Mac detects that your ISP and router are offering IPv6 service, (through a router notification called an "advertisement,") you'll see a single address there.

Make sure to look at all devices, both Wireless and wired.

You can check with from the shell aswell
```
c3se:~ user$ ifconfig en0
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
    options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
    ether 38:c9:86:1a:6a:e8
    inet6 fe80::183f:484d:a39c:4b08%en0 prefixlen 64 secured scopeid 0x4
    inet 129.16.111.111 netmask 0xffff0000 broadcast 129.16.255.255
    nd6 options=201<PERFORMNUD,DAD>
    media: autoselect (1000baseT <full-duplex>)
    status: active
```
Here we see that there is no public IPv6 address available (only local fe80)
But if you are connected to an IPv6 network it could look something like this:

```
MacBook-Pro:~ user$ ifconfig en0
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
    ether 14:10:9f:e5:9d:1b
    inet6 fe80::493:eb90:d47c:3e1d%en0 prefixlen 64 secured scopeid 0x4
    inet6 2001:6b0:2:2801:ec:8620:a859:104a prefixlen 64 autoconf secured
    inet6 2001:6b0:2:2801:890c:da8e:e4db:7d60 prefixlen 64 autoconf temporary
    inet 10.0.177.60 netmask 0xffff0000 broadcast 10.0.255.255
    nd6 options=201<PERFORMNUD,DAD>
    media: autoselect
    status: active
```

### Windows
Open a cmd (win+r, cmd). type ipconfig /all. Check for a IPv6 address...

```
ipconfig /all:

Wireless LAN adapter Wi-Fi 2:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) Dual Band Wireless-AC 7260
   Physical Address. . . . . . . . . : 4C-EB-42-F8-AB-B0
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::7428:6b87:7d7:88ff%10(Preferred)
   IPv4 Address. . . . . . . . . . . : 83.218.77.99(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.248
   Lease Obtained. . . . . . . . . . : den 27 april 2017 13:50:59
   Lease Expires . . . . . . . . . . : den 27 april 2017 17:12:12
   Default Gateway . . . . . . . . . : 83.218.77.97
   DHCP Server . . . . . . . . . . . : 83.218.77.98
   DHCPv6 IAID . . . . . . . . . . . : 122481474
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-20-93-6B-E8-9C-EB-E8-09-85-79

   DNS Servers . . . . . . . . . . . : 46.246.46.46
                                       194.132.32.23
   NetBIOS over Tcpip. . . . . . . . : Enabled

```

```
ipconfig /all:

Ethernet adapter Ethernet:   
Connection-specific DNS Suffix  . :   
Description . . . . . . . . . . . : Intel(R) 82579LM Gigabit Network Connection   
Physical Address. . . . . . . . . : 3C-D9-2B-57-8F-5C   
DHCP Enabled. . . . . . . . . . . : No   
Autoconfiguration Enabled . . . . : Yes   
IPv6 Address. . . . . . . . . . . : 2a02:760:1000:6:acf2:acef:abfe:76ce(Preferred)   
Temporary IPv6 Address. . . . . . : 2a02:760:1000:6:1d10:92c9:c5e4:a544(Deprecated)   
Temporary IPv6 Address. . . . . . : 2a02:760:1000:6:4d49:efb:66d:41f1(Deprecated)   
Temporary IPv6 Address. . . . . . : 2a02:760:1000:6:6c61:aa73:4da:b054(Preferred)   
Temporary IPv6 Address. . . . . . : 2a02:760:1000:6:f867:8fbd:cd0e:351e(Deprecated)   
Link-local IPv6 Address . . . . . : fe80::acf2:acef:abfe:76ce%4(Preferred)   
IPv4 Address. . . . . . . . . . . : 10.10.0.241(Preferred)   
Subnet Mask . . . . . . . . . . . : 255.255.255.0   
IPv4 Address. . . . . . . . . . . : 172.18.0.203(Preferred)   
Subnet Mask . . . . . . . . . . . : 255.255.255.0   
IPv4 Address. . . . . . . . . . . : 192.168.10.182(Preferred)   
Subnet Mask . . . . . . . . . . . : 255.255.255.0   
IPv4 Address. . . . . . . . . . . : 192.168.66.246(Preferred)   
Subnet Mask . . . . . . . . . . . : 255.255.255.0   
Default Gateway . . . . . . . . . : fe80::b2b2:dcff:fe33:8273%4    
                                    192.168.10.1   
DHCPv6 IAID . . . . . . . . . . . : 255645995   
DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-19-C3-73-5F-3C-D9-2B-57-8F-5C   
DNS Servers . . . . . . . . . . . : 89.189.220.100   
                                    81.93.131.5   
NetBIOS over Tcpip. . . . . . . . : Enabled
```

This looks good, so try to ping www.google.se over IPv6.
First we have to look up the IPv6 address:

```
C:\WINDOWS\system32>nslookup www.google.se
Server: resolv3.pin.se
Address: 89.189.220.100

Non-authoritative answer:
Name: www.google.se
Addresses: 2a00:1450:400f:808::2003
216.58.211.131
```

Then we can ping:
```
C:\WINDOWS\system32>ping 2a00:1450:400f:808::2003
Pinging 2a00:1450:400f:808::2003 with 32 bytes of data:
Reply from 2a00:1450:400f:808::2003: time=16ms
Reply from 2a00:1450:400f:808::2003: time=29ms
Reply from 2a00:1450:400f:808::2003: time=14ms

Ping statistics for 2a00:1450:400f:808::2003:    
   Packets: Sent = 3, Received = 3, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:    
   Minimum = 14ms, Maximum = 29ms, Average = 19ms

C:\WINDOWS\system32>
```

## Assigning an IPv6 interface and address to your instance in Horizon

The IPv6 network doesn't use floating IPs but instead uses directly connected interfaces to your instance.
This means that you will have to add another interface to your instance.

From the action drop-down on your instance choose "Attach Interface".
Select the "Public IPv6 Network" and click "Attach Interface".
Now you will be assigned an IPv6 address from the router based upon your MAC-address of the instance.
You are not able to choose an address freely from the IPv6 address pool.

Then on the overview of your instance you will see an additional address that looks like:
2001:6b0:2:2800:f816:3eff:fe41:6068

## Making use of that IPv6 address within your instance

Once we've assigned an IPv6 address to the instance we need to actually configure it within the instance OS.

### CentOS

We've attached a new interface to the instance.
Create an interface config in /etc/sysconfig/network-scripts/ifcg-eth1 and add:
```
DEVICE="eth1"
ONBOOT="yes"
TYPE="Ethernet"
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
```

Then you can do an ifup eth1 and the IPv6 address gets assigned to your interface.

### Ubuntu / Debian
We've attached the a new interface to the instance, to get the name of the interface check: dmesg | tail -2

Create an interface config in /etc/network/interfaces.d/20-ifcfg-ipv6.cfg and add:
```
auto ens6
iface ens6 inet6 auto
```

Then you can do an ifup ens6 and the IPv6 address gets assigned to your interface.

### CoreOS
CoreOS automaticaly sets up your additional interface and enables IPv6 on it. So you do not have to do anything.

## IPv6 Security Groups
You will have to open up for your IPv6 traffic in the security groups, you will see that the "Ether type" will differ among the rules for IPv4 and IPv6 rules.

So if you've previously opened a rule for SSH over IPv4 we will need to add another rule for SSH over IPv6.

## Connecting to your instace
Once all the above steps has been verified and configured you should now be able to connect to your instance through i.e. SSH.

```
$ ssh core@2001:6b0:2:2800:f816:3eff:fed6:f73e
Enter passphrase for key '/home/demov6/.ssh/id_rsa': 
Container Linux by CoreOS stable (1298.7.0)
core@demo-v6 ~ $ ip addr show dev eth1 scope global
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether fa:16:3e:d6:f7:3e brd ff:ff:ff:ff:ff:ff
    inet6 2001:6b0:2:2800:f816:3eff:fed6:f73e/64 scope global mngtmpaddr noprefixroute dynamic 
       valid_lft 2591892sec preferred_lft 604692sec
```