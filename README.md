# RPI-Robotic-arm-2

RPI IOT for ROBOT ARM 2 [ MR-999 ] With battery,Modulable (still can hotplug switch to their remote-controller)


ps. This project is done ^^. 

Recomend for people who already have the Robot arm because in fact the robot arm is have a poor performance (use motor) and can lift only a small and light weight object. 


## Hardware

* [Raspberry Pi 2 model B with Rasbian OS](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/) - Mainboard
* [5V RELAY 8-CH 10A 250VAC GTTH-1015](https://gravitechthai.com/product_detail.php?d=859/) - For Controling motor
* [ROBOT ARM 2 (MR-999)](http://www.elekit.co.jp/en/product/MR-999R) - ARM

## Wiring

RPI

```
[ . ][ x ] >> To Relay VCC
[ . ][ . ]
[ . ][ x ] >> To Relay GND
[ . ][ . ]
[ . ][ . ]
[ x ][ x ] >> To Relay IN1,IN2
[ x ][ . ] >> To Relay IN3
[ x ][ x ] >> To Relay IN4,IN5
[ . ][ x ] >> To Relay IN6
[ x ][ . ] >> To Relay IN7
[ x ][ . ] >> To Relay IN8
```
Relay

```
  ----------
          []
  [+](IN1)[x] >> Bread Board L1
          [+] >> Bread board +
  ----------
          []
  [-](IN2)[x] >> Bread Board L1
          [-] >> Bread board -
  ----------
          []
  [+](IN3)[x] >> Bread Board L2
          [+] >> Bread board +
  ----------
          []
  [-](IN4)[x] >> Bread Board L2
          [-] >> Bread board -
  ----------
          []
  [+](IN5)[x] >> Bread Board L3
          [+] >> Bread board +
  ----------
          []
  [-](IN6)[x] >> Bread Board L3
          [-] >> Bread board -
  ----------
          []
  [+](IN7)[x] >> Bread Board L5
          [+] >> Bread board +
  ----------
          []
  [-](IN8)[x] >> Bread Board L5
          [-] >> Bread board -
  ----------
  
```


Bread Board

```
L1-L4
[Bread board +][Bread board -][L1]
[Bread board +][Bread board -][L2]
[Bread board +][Bread board -][L3]
[Bread board +][Bread board -][L4]
...


```

ROBOT ARM 2

```
Motor
---------------------------------
 Grapper (Hand  - Open, close)
 Joint 1 (base  - cw, ccw)
 Joint 2 (base  - Open, Close)
 Joint 3 (Ankle - Open, Close)
 Joint 4 (Ankle - cw, ccw)
---------------------------------


Robot Pin
----------------------------------
[x] >> Bread Board +
[x] >> Bread Board L1 (Grapper)
[x] >> Bread Board L2 (Joint 3)
[x] >> Bread Board L3 (Joint 1)
[ ]                              >>(this is the other joint but need more ch 2 relay)
[x] >> Bread Board L5 (Joint 2)
[x] >> Bread Board L4 (Joint 4)
[x] >> Bread Board -

----------------------------------

```


### Logic
Give examples
```
+ connect to L1 Grapper open
- connect to L1 Grapper will close
```
*** same as other Joint


### Installing

```
##Install flask
sudo apt-get install python-pip python-flask

##make the dir as you want and put the script in it.
cd /yourdir
sudo python app.py

## now you can access the rpi via web browser Enjoy ><
```



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
