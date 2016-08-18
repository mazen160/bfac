#!/usr/bin/env python
############################################################################################################
##BFAC: Backup File Artifacts Checker
###Description:
#An automated tool that checks for backup artifacts that may discloses the web-application's source code.
###Version:
#v1.0
###Homepage:
#https://github.com/mazen160/bfac
##Author:
#Mazin Ahmed <Mazin AT MazinAhmed DOT net>
############################################################################################################

def main():

	version='v1.0'

	from sys import argv,version_info,stdout
	import random
	import argparse
	try:
		from urllib import parse as urlparse
	except ImportError:
		import urlparse
	try:
		import requests
	except ImportError:
		print('[!] Error: requests module does not seem to be installed.')
		print('Use the following command to install requests module.')
		if ( version_info[0] == 2):
			print('$ pip install requests')
		else:
			print('$ pip3 install requests');exit('\nExiting...')

	class tcolor:
		endcolor = '\033[0m'
		red = '\033[31m'
		green = '\033[32m'
		purple = '\033[35m'
		yellow = '\033[93m'
		light_blue = '\033[96m'


	def logo(colored_logo):
		if (colored_logo == 0):
			logo = """
	\t\t\t\t  _____   _______  _______  _______
	\t\t\t\t(  ___ \ (  ____ \(  ___  )(  ____ \\
	\t\t\t\t| (   ) )| (    \/| (   ) || (    \/
	\t\t\t\t| (__/ / | (__    | (___) || |
	\t\t\t\t|  __ (  |  __)   |  ___  || |
	\t\t\t\t| (  \ \ | (      | (   ) || |
	\t\t\t\t| )___) )| )      | )   ( || (____/\\
	\t\t\t\t|/ \___/ |/       |/     \|(_______/
	\t\t\t\t
	\t\t\t-:::Backup File Artifacts Checker:::-\tversion: """+str(version)+"""
	___An automated tool that checks for backup artifacts that may discloses the web-application\'s source code___
	\t\t\tAuthor: Mazin Ahmed | <mazin AT mazinahmed DOT net> | @mazen160\n\n\n"""

		if (colored_logo == 1):
			logo = tcolor.light_blue+"""
	\t\t\t\t  _____   _______  _______  _______
	\t\t\t\t(  ___ \ (  ____ \(  ___  )(  ____ \\
	\t\t\t\t| (   ) )| (    \/| (   ) || (    \/
	\t\t\t\t| (__/ / | (__    | (___) || |
	\t\t\t\t|  __ (  |  __)   |  ___  || |
	\t\t\t\t| (  \ \ | (      | (   ) || |
	\t\t\t\t| )___) )| )      | )   ( || (____/\\
	\t\t\t\t|/ \___/ |/       |/     \|(_______/
	\t\t\t\t"""+tcolor.yellow+"""
	\t\t\t-:::Backup File Artifacts Checker:::-\tversion: """+str(version)+"""
	___An automated tool that checks for backup artifacts that may discloses the web-application\'s source code___
	\t\t\tAuthor: Mazin Ahmed | <mazin AT mazinahmed DOT net> | @mazen160\n\n\n"""+tcolor.endcolor
		return logo

	def instructions():
		print("""
		Arguments:-
	-h, --help           			Show this help message and exit.
	-u URL, --url URL    			Check a single URL.
	-l LIST, --list LIST 		 	Check a list of URLs.
	-level LEVEL, --level LEVEL		Set testing level [0-4] (Default: 0).
	-dvcs-test, --dvcs_test 		Performs only DVCS testing, which is also available by default on Level 4.	
	-vsc VALID_STATUS_CODES,		Specify valid status codes for checks, seperated by commas.(Default: 200).
	--valid-status-codes VALID_STATUS_CODES	
	-isc INVALID_STATUS_CODES, 		Specify invalid status codes for checks, seperated by commas.(Default: 403,404).
	--invalid-status-codes INVALID_STATUS_CODES	 
	-verify-file VERIFY_FILE_AVAILABILITY,  Method to verify the availability of the file. (Options: status_code,content_length,both) (Default: both)
	--verify-file-availability VERIFY_FILE_AVAILABILITY
	-xsc EXCLUDE_STATUS_CODES,		Specify status codes to exclude, seperated by commas.
	--exclude-status-codes EXCLUDE_STATUS_CODES
	-ra, --random-agent   			Enable random user-agent.
	-no-text, --no-text 			Prints and writes a clean output with only results.
	-v, --verbose        			Enable verbosity.
	-o OUTPUT, --output OUTPUT		Save output into a file.
	-V, --version				Show current vesion and exit.
	""")

	#Handling custom messages
	if ( not( '--no-text'  in argv) and not( '-no-text' in argv ) ):
		
		if ( ( '-h' in argv ) or ( '--help' in argv )  or ( len(argv) <= 1 ) or ( '-help' in argv) or ( '--h' in argv)):
			print(logo(1));instructions()
			exit()
		else:
			print(logo(1))


	##Handling arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--url", dest="url",help="Check a single URL.", action='store')
	parser.add_argument("-l","--list", dest="usedlist",help="Check a list of URLs.", action='store')
	parser.add_argument("-level","--level", dest="level",help="Set testing level [0-4](Default: 0).", action='store')
	parser.add_argument("-dvcs-test","--dvcs-test", dest="dvcs_test",help="Performs only testing for DVCS, which is available by default on Level 4.", action='store_true')
	parser.add_argument("-vsc","--valid-status-codes", dest="valid_status_codes",help="Specify valid status codes for checks, seperated by commas.(Default: 200).", action='store')
	parser.add_argument("-isc","--invalid-status-codes", dest="invalid_status_codes",help="Specify invalid status codes for checks, seperated by commas.(Default: 403,404).", action='store')
	parser.add_argument("-verify-file","--verify-file-availability", dest="verify_file_availability",help="Method to verify the availability of the file. (Options: status_code,content_length,both) (Default: both)", action='store',default='both')
	parser.add_argument("-xsc","--exclude-status-codes", dest="exclude_status_codes",help="Specify status codes to exclude, seperated by commas.", action='store')
	parser.add_argument("-o","--output", dest='output',help="Save output into a file.", action='store')
	parser.add_argument("-ra","--random-agent", dest='random_agent',help="Enable random user-agent.", action='store_true')
	parser.add_argument("-no-text","--no-text", dest='notext',help="Prints and writes a clean output with only results.", action='store_true')
	parser.add_argument("-v","--verbose", dest='verbosity',help="Enable verbosity.", action='store_true')
	parser.add_argument("-V","--version", dest='version',help="Show current vesion and exit.", action='store_true')
	args = parser.parse_args()

	if ( args.version ):
		print("Version: "+version)
		exit()

	if not ( (args.url) or (args.usedlist) ):
		print(tcolor.red+'[!] Error: Either URL or List should be supplied.'+tcolor.endcolor);exit('\nExiting...')

	if ( args.usedlist and args.url ):
		print(tcolor.red+'[!] Error: Both URL and List options are chosen.'+tcolor.endcolor);exit('\nExiting...')
		
	levels = ['0','1','2','3','4']
	if (args.level) and (args.level not in levels):
		print(tcolor.red+'[!]Error: Chosen level is invalid.'+tcolor.endcolor);exit('\nExiting...')
	
	if (args.level) and (args.dvcs_test):
		print(tcolor.red+'[!]Error: Only either DVCS Checks or Levels can be Used.\nLevel 4 performs all tests, including DVCS checks.'+tcolor.endcolor);exit('\nExiting...')

	if (not(args.dvcs_test)) and (not(args.level)):
		args.level = 0 # Setting Default level to 0

	verify_file_availability_options = ['status_code','content_length','both']
	args.verify_file_availability = args.verify_file_availability.lower()
	if ( args.verify_file_availability not in verify_file_availability_options ):
		print(tcolor.red+'[!]Error: Entered Verify File Availability option is invalid.'+tcolor.endcolor);exit('\nExiting...')
		
	def url_clean(url):
		url = url.split('?')[0]
		url = url.replace('#','%23')
		url = url.replace(' ','%20')
		return url
	
	def url_handler(url):
		try:
			scheme = urlparse.urlparse(url).scheme
			domain = urlparse.urlparse(url).netloc
			site = scheme+'://'+domain
			file_path = urlparse.urlparse(url).path
			try:
				filename = url.split('/')[-1]
			except IndexError:
				filename = ''
			file_dir = file_path.rstrip(filename)
			full_path = site+file_dir
			try:
				filename_ext = filename.split('.')[1]
			except IndexError:
				filename_ext = ''
			try:
				filename_without_ext = filename.split('.')[0]
			except IndexError:
				filename_without_ext = ''

		except IndexError:
			pass

		return scheme,domain,site,file_path,filename,file_dir,full_path, filename_ext, filename_without_ext


	def backup_lists(url):
		scheme,domain,site,file_path,filename,file_dir,full_path, filename_ext, filename_without_ext = url_handler(url)
		
		backup_testing_level0 = [
site+file_path+'~',
site+file_path+'%23',
site+file_path+'.save',
site+file_path+'.swp',
site+file_path+'.swo',
full_path+'%23'+filename+'%23',
site+file_path+'.bak'
]

		backup_testing_level1 = [ 
site+file_path+'_',
site+file_path+'_bak',
site+file_path+'-bak',
site+file_path+'.bk',
site+file_path+'.bkp',
full_path+filename+'.bac',
site+file_path+'.old',
site+file_path+'_old',
site+file_path+'.copy',
site+file_path+'.original',
site+file_path+'.orig',
site+file_path+'.org',
site+file_path+'.txt',
site+file_path+'.default',
full_path+filename+'.tpl',
full_path+filename+'.tmp',
full_path+filename+'.temp',
full_path+'.'+filename+".swp",
full_path+'.'+filename+".swo",
full_path+'_'+filename+'.swp',
full_path+'_'+filename+'.swo',
full_path+filename+'.sav',
full_path+filename+'.conf',
full_path+filename_without_ext+'%20%28copy%29.'+filename_ext,
full_path+'Copy%20of%20'+filename,
full_path+'copy%20of%20'+filename,
full_path+filename_without_ext+'%20-%20Copy.'+filename_ext,
full_path+filename_without_ext+'%20copy.'+filename_ext
]

		backup_testing_level2 = [ 
full_path+filename_without_ext+'.txt',
full_path+filename_without_ext+'.bak',
full_path+filename_without_ext+'.bkp',
full_path+filename_without_ext+'.save',
full_path+filename_without_ext+'.old',
full_path+filename_without_ext+'.orig',
full_path+filename_without_ext+'.original',
site+file_path+'%00',
site+file_path+'%01',
full_path+'~'+filename,
full_path+filename_without_ext+'.tpl',
full_path+filename_without_ext+'.tmp',
full_path+filename_without_ext+'.temp',
full_path+filename+'.nsx',
full_path+filename+'.cs',
full_path+filename+'.csproj',
full_path+filename+'.vb',
full_path+filename+'.0',
full_path+filename+'.1',
full_path+filename+'.arc',
full_path+filename+'.inc',
full_path+filename+'.lst',
full_path+'.~lock.'+filename+'%23',
full_path+'.~'+filename,
full_path+'~%24'+filename
]

		backup_testing_level3 = [
site+file_path+'.tar',
site+file_path+'.rar',
site+file_path+'.zip',
site+file_path+'.tar.gz',
full_path+'backup-'+filename,
full_path+filename_without_ext+'-backup.'+filename_ext,
full_path+filename_without_ext+'-bkp.'+filename_ext,
full_path+filename_without_ext+'.tar',
full_path+filename_without_ext+'.rar',
full_path+filename_without_ext+'.zip',
full_path+filename_without_ext+'.tar.gz'
]

		backup_testing_level4 = [
site+'/.git/HEAD',
full_path+'.git/HEAD',
site+'/.git/index',
full_path+'.git/index',
site+'/.gitignore',
full_path+'.gitignore',
site+'/.bzr/README',
full_path+'.bzr/README',
site+'/.hg/requires',
full_path+'.hg/requires',
site+'/.svn/entries',
full_path+'.svn/entries',
site+'/.svnignore',
full_path+'.svnignore',
site+'/CVS/Entries',
full_path+'CVS/Entries',
site+'/.cvsignore',
full_path+'.cvsignore',
site+'/composer.lock',
full_path+'composer.lock'
]
		
		args.level = str(args.level)
		
		if ( args.level == '0' ):
			backup_testing_checks = backup_testing_level0
		if ( args.level == '1' ):
			backup_testing_checks = backup_testing_level0+backup_testing_level1
		if ( args.level == '2' ):
			backup_testing_checks = backup_testing_level0+backup_testing_level1+backup_testing_level2
		if ( args.level == '3' ):
			backup_testing_checks = backup_testing_level0+backup_testing_level1+backup_testing_level2+backup_testing_level3
		if ( args.level == '4' ):
			backup_testing_checks = backup_testing_level0+backup_testing_level1+backup_testing_level2+backup_testing_level3+backup_testing_level4
		if ( args.dvcs_test == True):
			backup_testing_checks = backup_testing_level4
			
		backup_testing_checks = list(backup_testing_checks)
		backup_testing_checks = random.sample(backup_testing_checks, len(backup_testing_checks))
		return backup_testing_checks

	class status_codes:
		if (args.valid_status_codes):
			vsc_list = [vsc_args.strip() for vsc_args in  args.valid_status_codes.split(',')]
			for check_vsc_list in vsc_list:
				if str.isdigit(check_vsc_list) == False:
					print(tcolor.red+'[!] Error: Invalid entered status codes.'+tcolor.endcolor);exit('\nExiting...')
		else:
			vsc_list = ['200']

		if (args.invalid_status_codes):
			isc_list = [isc_args.strip() for isc_args in  args.invalid_status_codes.split(',')]
			for check_isc_list in isc_list:
				if str.isdigit(check_isc_list) == False:
					print(tcolor.red+'[!] Error: Invalid entered status codes.'+tcolor.endcolor);exit('\nExiting...')
					
		else:
			isc_list = ['403','404']

		for check_duplicate in vsc_list:
			if ( check_duplicate in isc_list):
				print(tcolor.red+'[!] Error: Duplicate values in status codes.'+tcolor.endcolor);exit('\nExiting...')
				
	
	def initial_request(link):
		if (args.verify_file_availability != 'status_code'):
			random_ascii_charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
			random_value = ''.join(random.choice(random_ascii_charset) for _ in range(5))
			random_value_ext = ''.join(random.choice(random_ascii_charset) for _ in range(3))
			link = url_handler(link)[2]+url_handler(link)[5]+random_value+'.'+random_value_ext
			request_response_code_initial, response_content_length_initial = requester(link)
			default_content_length_range = 50 #CHANGE THE CONTENT-LENGTH RANGE ON THIS LINE IN CASE OF FACING A FALSE-POSITIVE ISSUE
			default_content_length_range = int(default_content_length_range)
			response_content_length_initial_min = response_content_length_initial-default_content_length_range
			response_content_length_initial_max = response_content_length_initial+default_content_length_range
		else:
			request_response_code_initial = '0'
			response_content_length_initial = '0'
			response_content_length_initial_min = '0'
			response_content_length_initial_max	= '0'
			
		return request_response_code_initial, response_content_length_initial, response_content_length_initial_min, response_content_length_initial_max	
	
	def request_check(request_response_code,request_response_content_length,response_content_length_initial_min, response_content_length_initial_max):				
		request_check_status = False
		
		content_length_test = True
		if ( args.verify_file_availability != 'status_code' ):
			for num in range(response_content_length_initial_min,response_content_length_initial_max+1):
				if ( num == request_response_content_length ):
					content_length_test = False

		if ( args.verify_file_availability == 'both' ):
			if ( not(str(request_response_code) in status_codes.isc_list)) and (str(request_response_code) in status_codes.vsc_list) or (content_length_test == True): 
				request_check_status = True
			else:
				request_check_status = False
		
		if ( args.verify_file_availability == 'status_code' ):
			if ( not(str(request_response_code) in status_codes.isc_list)) and (str(request_response_code) in status_codes.vsc_list):
				request_check_status = True
			else:
				request_check_status = False
				
		if ( args.verify_file_availability == 'content_length' ):
			if ( content_length_test == True ): 
				request_check_status = True
			else:
				request_check_status = False
		
		if (args.exclude_status_codes):
			exclude_status_codes_list = [xsc_args.strip() for xsc_args in  args.exclude_status_codes.split(',')]
			request_response_code = str(request_response_code)
			if ( request_response_code in exclude_status_codes_list):
				request_check_status = False

		return request_check_status

	def choose_agent():
		if args.random_agent:
			agents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.82 Safari/537.36 OPR/29.0.1795.41',
			'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
			'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:39.0) Gecko/20100101 Firefox/42.0',
			'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
			'Mozilla/5.0 (compatible; Googlebot/2.1;  http://www.google.com/bot.html)',
			'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.1916.141 Mobile Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2311.90 Safari/537.36',
			'Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/41.0',
			'Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.01']
			chosen_agent = random.choice(agents)
		else:
			chosen_agent = 'BFAC '+str(version)+' (https://github.com/mazen160/bfac)' # BFAC DEFAULT UA
		return chosen_agent

	def requester(link):
		try:
			headers = { 'User-Agent': choose_agent(),'Accept': '*/*'}
			req = requests.get(link, headers=headers, verify=False, allow_redirects=False)
			request_response_code = req.status_code
			request_response_content_length = len(req.content)
			return request_response_code, request_response_content_length
		except requests.exceptions.SSLError:
			print(tcolor.red+'[!]SSL Error at: '+link+tcolor.endcolor)
		except requests.exceptions.ConnectionError:
			print(tcolor.red+'[!]Connection Error at: '+link+tcolor.endcolor)
		except requests.exceptions.MissingSchema:
			print(tcolor.red+'[!]Error: Invalid URL - Missing Schema at: '+link+tcolor.endcolor);exit('\nExiting...')
		except requests.exceptions.InvalidSchema:
			print(tcolor.red+'[!]Error: Invalid URL - Invalid Schema at: '+link+tcolor.endcolor);exit('\nExiting...')
		except requests.exceptions.InvalidURL:
			print(tcolor.red+'[!]Error: Invalid URL at: '+link+tcolor.endcolor);exit('\nExiting...')

	def disable_ssl_errors():
		#Disabling unwanted SSL errors
		try:
			requests.packages.urllib3.disable_warnings()
		except AttributeError:
			pass #Commented out to avoid the annoyance of showing the message in every execution of the script. #print(tcolor.red+'[!]requests.packages.urllib3.disable_warnings() does not seem to be working. Bogus errors may be shown during the usage of the tool.'+tcolor.endcolor)
		
	def output0(data):
		try:
			if not(args.notext):
				if args.output:
					filename = args.output
					output =  open(filename,'a')
					output.write(data+'\n\n\n')
					output.close()
		except IOError:
			print(tcolor.red+'[!] Error: There was an error in writing into the specified location.'+tcolor.endcolor);exit('\nExiting...')
		except TypeError:
			print(tcolor.red+'[!] Error: There was an error in writing into the specified location.'+tcolor.endcolor);exit('\nExiting...')

	def output1(data,newline):
		try:
			if args.output:
				filename = args.output
				output =  open(filename,'a')
				if (newline == 0):
					output.write(data)
				if (newline == 1):
					output.write(data+'\n')
				output.close()
		except IOError:
			print(tcolor.red+'[!] Error: There was an error in writing into the specified location.'+tcolor.endcolor);exit('\nExiting...')
		except TypeError:
			print(tcolor.red+'[!] Error: There was an error in writing into the specified location.'+tcolor.endcolor);exit('\nExiting...')

	
	if args.output:
		output0(logo(0))

	def verbose_checks_handler(link,verbose_option,request_response_code,request_response_content_length):
		if ( verbose_option == 'testing_path'):
			verbose_message = '[*] Checking ['+link+']'
			if ( version_info[0] == 2):
				print(verbose_message),
			else:
				stdout.write(verbose_message+' ')
			if args.output:
				output1(verbose_message,0)
				output1(' ',0)

		if ( verbose_option == 'response'):
			verbose_message = '(Response-Code: '+str(request_response_code)+' | Content-Length: '+str(request_response_content_length)+')'
			print(verbose_message)
			if args.output:
				output1(verbose_message,1)
	
	def valid_check_handler(link,request_response_code,request_response_content_length):
		message = '[$] Discovered: -> '+'{'+link+'}'+' '+'(Response-Code: '+str(request_response_code)+' | Content-Length: '+str(request_response_content_length)+')'
		if args.output:
			output1(message,1)
		print(tcolor.green+message+tcolor.endcolor)
	
	def notext_valid_check_handler(link):
		message = link
		if args.output:
			output1(message,1)
		print(message)
				
	disable_ssl_errors()
	
	def test_url(url):
		try:
			request_response_code_initial, response_content_length_initial, response_content_length_initial_min, response_content_length_initial_max = initial_request(url)
		except TypeError:
			pass
		for link in backup_lists(url):
			try:
				link = url_clean(link)
				if not(args.notext):
					if args.verbosity:
						verbose_checks_handler(link,'testing_path',0,0)
				request_response_code, request_response_content_length = requester(link)
				if not(args.notext):
					if args.verbosity:
						verbose_checks_handler(link,'response',request_response_code,request_response_content_length)
				if ( request_check(request_response_code,request_response_content_length,response_content_length_initial_min, response_content_length_initial_max) == True ):
					if not(args.notext):
						valid_check_handler(link,request_response_code,request_response_content_length)
					if (args.notext):
						notext_valid_check_handler(link)
			except TypeError:
				pass
					
	def test_list(testing_input_list):
		testing_list = open(testing_input_list).readlines()
		for url in testing_list:
			url = url.rstrip('\n')
			test_url(url)
	
					
	if (args.url):
		test_url(args.url)
	if (args.usedlist):
		test_list(args.usedlist)
	
	if not(args.notext):
		print(tcolor.purple+'\n\n[*%*]Finished.'+tcolor.endcolor)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print('\nKeyboardInterrupt Detected.');exit('\nExiting...')

### END ###
