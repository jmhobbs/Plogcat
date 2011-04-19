# What is Plogcat?

Plogcat is a frontend to Android's logcat.

It adds regex based colorization, filtering and highlighting.

Watch a quick demo here: <http://www.youtube.com/watch?v=9XWo8o7KXAU>

# What you need

* Python > 2.4
* adb

# Install

    $ git clone git://github.com/jmhobbs/Plogcat.git
    $ cd Plogcat
    $ python setup.py install
    $ plogcat -c config.json

# Options

	Usage: plogcat [options]

	Options:
	  -h, --help            show this help message and exit
	  -c CONFIG, --config=CONFIG
	                        json config options
	  -b BANFILE, --banfile=BANFILE
	                        file of ban regexes
	  -s HIGHLIGHTFILE, --highlightfile=HIGHLIGHTFILE
	                        file of highlight regexes
	  -p, --plain           no color


# Configuration

Plogcat is driven around Python regular expressions.

## JSON Config File

Only two options in the config.json file right now, both are paths to regex files.

    {
        "banfile": "banfile.txt",
        "highlightfile": "highlightfile.txt"
    }

## Ban File

The banfile is just regex's you want to ignore, one to a line, like this:

	^E/BluetoothEventLoop.cpp
	^V/BluetoothEventRedirector
	^I/dun_service
	^D/XLEI-TRACE

## Highlight File

Same format as ban file, but highlights instead of ignoring, like this:

	^V/WifiMonitor
	^V/WifiStateTracker
	^D/NetworkStateTracker
	^D/WifiService

