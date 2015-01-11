PyMail
========
**Simple python bulk mailer script with sample html mail**

Send bulk html emails from the commandline by specifying recipients in csv form and an html template.


Requirements
------------

* python >= 2.4

Usage
-----
Setup
~~~~~
Edit the files before running the script:

    $ vim config.py
    
    $ vim pymail.py


Commandline
~~~~~~~~~~~
The simplest method of sending out a bulk email.

Send the actual email to all recipients:
    $  cd PyBulkMail
    
    $  python pymail.py -s /home/xyz/PyBulkMail/test.html /home/xyz/PyBulkMail/pymail.csv 'Email Subject'


