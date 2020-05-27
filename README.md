# individual-app-volume

Simple python script to change the volume of an individual application in pulseaudio.

Hopefully it is useful to someone.


## Requirements

* Pulseaudio
* Python 3
* I've only tested this in ubuntu, but if you have the `pactl` command available, it should work.

## Usage

```
python3 ./appvolume.py <appname> <volume>
```

Volume supports the same volume values as `pactl`




## Examples

Set plexamp volume to 50%:

```
python3 ./appvolume.py plexamp 50%
```


Set firefox volume to 7%:

```
python3 ./appvolume.py firefox 7%
```

Reduce plexamp volume by 10%


```
python3 ./appvolume.py firefox -10%
```

Find out what application name to use (run when the app is active and playing sound):

```
pactl list sink-inputs | grep  application.process.binary
```

## Note

I am just sharing the script. I don't intend this to become a real command or app. But I guess nothing stops you from forking into it (aside of the GPLv3's terms)