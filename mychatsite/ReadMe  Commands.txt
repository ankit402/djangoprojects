Microsoft Windows [Version 10.0.19045.4894]
(c) Microsoft Corporation. All rights reserved.

E:\djangoproject\Djangochat>pip install django
Requirement already satisfied: django in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (5.1)
Requirement already satisfied: asgiref<4,>=3.8.1 in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (from django) (3.8.1)
Requirement already satisfied: sqlparse>=0.3.1 in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (from django) (0.5.1)
Requirement already satisfied: tzdata in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (from django) (2024.1)

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

E:\djangoproject\Djangochat>django-admin startproject mysite

E:\djangoproject\Djangochat>django-admin startproject mychatsite

E:\djangoproject\Djangochat>cd mychatsite

E:\djangoproject\Djangochat\mychatsite>python manage.py startapp chatapp

E:\djangoproject\Djangochat\mychatsite>pip install channel == 3.0
ERROR: Invalid requirement: '=='

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

E:\djangoproject\Djangochat\mychatsite>pip install channels == 3.0
ERROR: Invalid requirement: '=='

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

E:\djangoproject\Djangochat\mychatsite>pip install channels == 3.0.4
ERROR: Invalid requirement: '=='

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

E:\djangoproject\Djangochat\mychatsite>pip install channels==3.0.4
Collecting channels==3.0.4
  Downloading channels-3.0.4-py3-none-any.whl.metadata (1.3 kB)
Requirement already satisfied: Django>=2.2 in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (from channels==3.0.4) (5.1)
Requirement already satisfied: asgiref<4,>=3.3.1 in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (from channels==3.0.4) (3.8.1)
Collecting daphne<4,>=3.0 (from channels==3.0.4)
  Downloading daphne-3.0.2-py3-none-any.whl.metadata (6.4 kB)
Collecting twisted>=18.7 (from twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading twisted-24.7.0-py3-none-any.whl.metadata (18 kB)
Collecting autobahn>=0.18 (from daphne<4,>=3.0->channels==3.0.4)
  Downloading autobahn-24.4.2-py2.py3-none-any.whl.metadata (18 kB)
Requirement already satisfied: sqlparse>=0.3.1 in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (from Django>=2.2->channels==3.0.4) (0.5.1)
Requirement already satisfied: tzdata in c:\users\ankit\appdata\local\programs\python\python312\lib\site-packages (from Django>=2.2->channels==3.0.4) (2024.1)
Collecting txaio>=21.2.1 (from autobahn>=0.18->daphne<4,>=3.0->channels==3.0.4)
  Downloading txaio-23.1.1-py2.py3-none-any.whl.metadata (5.4 kB)
Collecting cryptography>=3.4.6 (from autobahn>=0.18->daphne<4,>=3.0->channels==3.0.4)
  Downloading cryptography-43.0.1-cp39-abi3-win_amd64.whl.metadata (5.4 kB)
Collecting hyperlink>=21.0.0 (from autobahn>=0.18->daphne<4,>=3.0->channels==3.0.4)
  Downloading hyperlink-21.0.0-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting setuptools (from autobahn>=0.18->daphne<4,>=3.0->channels==3.0.4)
  Downloading setuptools-75.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting attrs>=21.3.0 (from twisted>=18.7->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading attrs-24.2.0-py3-none-any.whl.metadata (11 kB)
Collecting automat>=0.8.0 (from twisted>=18.7->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading Automat-24.8.1-py3-none-any.whl.metadata (8.4 kB)
Collecting constantly>=15.1 (from twisted>=18.7->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading constantly-23.10.4-py3-none-any.whl.metadata (1.8 kB)
Collecting incremental>=24.7.0 (from twisted>=18.7->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading incremental-24.7.2-py3-none-any.whl.metadata (8.1 kB)
Collecting typing-extensions>=4.2.0 (from twisted>=18.7->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting zope-interface>=5 (from twisted>=18.7->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading zope.interface-7.0.3-cp312-cp312-win_amd64.whl.metadata (44 kB)
     ---------------------------------------- 44.8/44.8 kB 2.2 MB/s eta 0:00:00
Collecting idna>=2.4 (from twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading idna-3.9-py3-none-any.whl.metadata (10 kB)
Collecting pyopenssl>=21.0.0 (from twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading pyOpenSSL-24.2.1-py3-none-any.whl.metadata (13 kB)
Collecting service-identity>=18.1.0 (from twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading service_identity-24.1.0-py3-none-any.whl.metadata (4.8 kB)
Collecting cffi>=1.12 (from cryptography>=3.4.6->autobahn>=0.18->daphne<4,>=3.0->channels==3.0.4)
  Downloading cffi-1.17.1-cp312-cp312-win_amd64.whl.metadata (1.6 kB)
Collecting pyasn1 (from service-identity>=18.1.0->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
Collecting pyasn1-modules (from service-identity>=18.1.0->twisted[tls]>=18.7->daphne<4,>=3.0->channels==3.0.4)
  Downloading pyasn1_modules-0.4.1-py3-none-any.whl.metadata (3.5 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=3.4.6->autobahn>=0.18->daphne<4,>=3.0->channels==3.0.4)
  Downloading pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Downloading channels-3.0.4-py3-none-any.whl (38 kB)
Downloading daphne-3.0.2-py3-none-any.whl (26 kB)
Downloading autobahn-24.4.2-py2.py3-none-any.whl (666 kB)
   ---------------------------------------- 667.0/667.0 kB 2.8 MB/s eta 0:00:00
Downloading twisted-24.7.0-py3-none-any.whl (3.2 MB)
   ---------------------------------------- 3.2/3.2 MB 4.3 MB/s eta 0:00:00
Downloading attrs-24.2.0-py3-none-any.whl (63 kB)
   ---------------------------------------- 63.0/63.0 kB 1.1 MB/s eta 0:00:00
Downloading Automat-24.8.1-py3-none-any.whl (42 kB)
   ---------------------------------------- 42.6/42.6 kB 1.0 MB/s eta 0:00:00
Downloading constantly-23.10.4-py3-none-any.whl (13 kB)
Downloading cryptography-43.0.1-cp39-abi3-win_amd64.whl (3.1 MB)
   ---------------------------------------- 3.1/3.1 MB 5.2 MB/s eta 0:00:00
Downloading hyperlink-21.0.0-py2.py3-none-any.whl (74 kB)
   ---------------------------------------- 74.6/74.6 kB 4.3 MB/s eta 0:00:00
Downloading idna-3.9-py3-none-any.whl (71 kB)
   ---------------------------------------- 71.7/71.7 kB 1.3 MB/s eta 0:00:00
Downloading incremental-24.7.2-py3-none-any.whl (20 kB)
Downloading pyOpenSSL-24.2.1-py3-none-any.whl (58 kB)
   ---------------------------------------- 58.4/58.4 kB 1.6 MB/s eta 0:00:00
Downloading service_identity-24.1.0-py3-none-any.whl (12 kB)
Downloading setuptools-75.0.0-py3-none-any.whl (1.2 MB)
   ---------------------------------------- 1.2/1.2 MB 5.3 MB/s eta 0:00:00
Downloading txaio-23.1.1-py2.py3-none-any.whl (30 kB)
Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Downloading zope.interface-7.0.3-cp312-cp312-win_amd64.whl (212 kB)
   ---------------------------------------- 212.1/212.1 kB 3.3 MB/s eta 0:00:00
Downloading cffi-1.17.1-cp312-cp312-win_amd64.whl (181 kB)
   ---------------------------------------- 182.0/182.0 kB 3.7 MB/s eta 0:00:00
Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
   ---------------------------------------- 83.1/83.1 kB 2.4 MB/s eta 0:00:00
Downloading pyasn1_modules-0.4.1-py3-none-any.whl (181 kB)
   ---------------------------------------- 181.5/181.5 kB 3.6 MB/s eta 0:00:00
Downloading pycparser-2.22-py3-none-any.whl (117 kB)
   ---------------------------------------- 117.6/117.6 kB 2.3 MB/s eta 0:00:00
Installing collected packages: typing-extensions, txaio, setuptools, pycparser, pyasn1, idna, constantly, automat, attrs, zope-interface, pyasn1-modules, incremental, hyperlink, cffi, twisted, cryptography, service-identity, pyopenssl, autobahn, daphne, channels
