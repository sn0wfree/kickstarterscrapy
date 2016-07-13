
import multiprocessing as mp
import sys
import zipfile
import datetime
import time
import threading
import Queue
import gc
from urllib2 import Request, urlopen, URLError
import urllib2
import requests
from lxml import etree
import pickle
import os
import unicodecsv
import csv
import pandas as pd
import smtplib
import mimetypes
import email.mime.text
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email import encoders
from email.utils import parseaddr, formataddr
from email.header import Header
from email.Encoders import encode_base64
from email.utils import COMMASPACE

item_headers = ['Project_ID','project_name','Goal','url',
              'pledged_amount','backers_count','creator_full_name',
              'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
              'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','launched_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']




def readacsv(file):
    with open(file,'r+') as f:
        w=pd.read_csv(file,skip_footer=1,engine='python')
    return w


w=readacsv('/Users/sn0wfree/Dropbox/BitTorrentSync/recollectwrong/Book2.csv')
a=w['url']

print a[2]
