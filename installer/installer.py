#!/usr/bin/env python3
import subprocess as sbp
import os
import platform
import sys
import json
import tarfile

epkg_path = sys.argv[1]

def check_epkg_file(epkg_path):
	if not epkg_path.endswith(".epkg.tar"):
		print("Invalid package. EPKG packages must have the extension .epkg.tar")
		sys.exit(1)
	try:
		with tarfile.open(epkg_path, 'r:') as tar:
			print("Package seems valid, extracting.")
	except tarfile.ReadError:
		print("Invalid package.")
		sys.exit(1)
def extract_epkg_file(epkg_path):
	os.makedirs("/tmp/epkg/temp/", exist_ok=True)
	with tarfile.open(epkg_path, 'r:') as tar:
		tar.extractall(path="/tmp/epkg/temp/")
	
def read_extracted_epkg():
	if not os.path.exists("/tmp/epkg/temp/proginfo.json"):
		print("Invalid package, missing runtime information.")
		sys.exit(1)
	if not os.path.exists("/tmp/epkg/temp/einfo.json"):
		print("Invalid package, missing metadata.")
		sys.exit(1)
		
	if os.path.exists("/temp/epkg/temp/einfo.json") and os.path.exists("/tmp/epkg/temp/proginfo.json"):
		print("Package seems valid, reading metadata.")
		#to be continued
