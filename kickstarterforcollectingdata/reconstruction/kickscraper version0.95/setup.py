from setuptools import setup, find_packages

setup(
    name = 'spider_for_kickstarterCFP',
    version = '2.3.3.3'
    author='sn0wfree'
    packages=['lxml ','multiprocessing','sys','os','zipfile','datetime','time',
              'threading','Queue','gc','urllib2','requests','pickle','unicodecsv',
              'csv','smtplib','mimetypes','email','pandas','celery',
              ]
    author_email='twocucao@gmail.com',
    keywords = 'python kickstarter crowdfunding spider'
    include_package_data=True,
    zip_safe=True,
    description='this code is for my dissertation',
    long_description='just enjoy',


)
