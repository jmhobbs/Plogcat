import subprocess
import re

VERSION="0.0.1"

# TODO: Curses - http://www.tuxradar.com/content/code-project-build-ncurses-ui-python
# TODO: getopt - http://docs.python.org/library/getopt.html

class term:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

class plogcat:

	def __init__ ( self ):
		self.levels = {
			"V": term.OKBLUE,
			"D": term.OKBLUE,
			"I": term.OKGREEN,
			"W": term.WARNING,
			"E": term.FAIL
		}

		self.bufsize = 1024
		self.bans = []
		self.highlights = []

	def loadBanFile ( self, ban_file, verbose = True ):
		with open( ban_file, 'r' ) as bans:
			for regex in bans:
				self.addBan( regex, verbose )

	def addBan ( self, regex, verbose = False ):
		self.bans.append( re.compile( regex[:-1] ) )
		if verbose:
			print term.WARNING + regex[:-1] + term.ENDC

	def loadHighlightFile ( self, highlight_file, verbose = True ):
		with open( highlight_file, 'r' ) as highlights:
			for regex in highlights:
				self.addHighlight( regex, verbose )

	def addHighlight ( self, regex, verbose = False ):
		self.highlights.append( re.compile( regex[:-1] ) )
		if verbose:
			print term.WARNING + regex[:-1] + term.ENDC

	def isBanned ( self, line ):
		for ban in self.bans:
			if ban.search( line ):
				return True
		return False

	def isHighlighted ( self, line ):
		for highlight in self.highlights:
			if highlight.search( line ):
				return True
		return False

	def run ( self ):
		pipe = subprocess.Popen("adb logcat -v brief", shell=True, stdout=subprocess.PIPE).stdout

		try:

			while True:
				line = pipe.readline()
				if not line:
					print "NO LINE!"
					break
				if self.isHighlighted( line ):
					print term.HEADER + line + term.ENDC,
				elif not self.isBanned( line ):
					level = term.OKBLUE
					try:
						level = self.levels[line[0]]
					except:
						pass
					print level + line + term.ENDC,
		finally:
			pipe.close()
			print "Closed"

def main ():

	pc = plogcat()
	print
	print term.HEADER + "Loading Bans..." + term.ENDC
	print
	pc.loadBanFile('banfile.txt')
	print
	print term.HEADER + "Loading Highlights..." + term.ENDC
	print
	pc.loadHighlightFile('highlightfile.txt')
	print
	print
	print term.OKGREEN + "= Any Key To Continue = " + term.ENDC

	raw_input()
	print

	pc.run()


if __name__ == "__main__":
	main()


