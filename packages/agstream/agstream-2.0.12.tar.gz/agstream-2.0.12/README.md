AgspStream
==============
   
Agriscope data interface for python


This module allows to get data from yours Agribases programmatically
Data are retreived as an Pandas Datagrams

The development map will introduce data computing capabilities, to enhance
data analysis comming from agricultural field.


  
  
What's New
===========
- (2023/05) v2.0.12 : - syntax error correction when something dirty is coming
- (2022/09) v2.0.10 : - add excluded_virtual_types_pattern to exclude some virtual
                        on demand
					  - Add some robust thing agains dirty event (DST switch, sensor id move)
- (2022/09) v2.0.9  : Use Https
- (2022/01) v2.0.8  : Bug correction in logger
- (2022/01) v2.0.7  : Add a retry API when something wrong seems to be there
- (2022/01) v2.0.6  : Improve capabilities to select virtual datasources to update
- (2022/01) v2.0.0  : Add capabilities to get virtual datasources
- (2021/06) v1.0.4  : Again optimize exception reporting when server is not joinable
- (2021/06) v1.0.3  : Optimize exception reporting when server is not joinable
- (2021/03) v1.0.2  : Optimize sensor data retrieving
- (2020/09) v0.0.13 : Better support of module and sensor position
- (2020/01) v0.0.12 : export some internals methods
- (2019/09) v0.0.10 : solve some display problems
- (2019/08) Porting to python 3
- (2018/05) Add functionnal information on Agribases (type, sampling)
- (2018/05) Solve bug on from, to date 
- (2018/02) First version 

Dependencies
=============

Agstream is written to be use with  python 3
It requires Pandas  (>= 0.12.0)::

    pip install pandas

Installations
=============

    pip install agstream
    

Uses cases
==========
code :

	from agstream.session import AgspSession
	session = AgspSession()
	session.login("masnumeriqueAgStream", "1AgStream", updateAgribaseInfo=True)
	session.describe()
	for abs in session.agribases :
	    print ("****************************************")
	    print (abs)
	    df = session.getAgribaseDataframe(abs)
	    print (df.tail())
    print("Fin du programme")

Output :

	**************************************************
	* Example 1 :  simplest way to get data
	* get the data, and feed an xlsfile
	**************************************************
	****************************************
	Compteur Mourvedre Rang 9(2301) AGRIBASE3S_STC SIGFOX containing 3 sensors
	Récuperation de 864 données
							compteur d'eau  alimentation #4  humectation foliaire
	2021-03-28 14:18:28+02:00             0.0            3.312                   0.0
	2021-03-28 14:33:29+02:00             0.0            3.316                   0.0
	2021-03-28 14:48:29+02:00             0.0            3.318                   0.0
	2021-03-28 15:03:29+02:00             0.0            3.314                   0.0
	2021-03-28 15:18:29+02:00             0.0            3.310                   0.0
	Ecriture des  données dans le fichier Compteur Mourvedre Rang 9.xlsx
	****************************************
	Debitmetre Grenache Rang 10(2299) AGRIBASE3S_STC SIGFOX containing 3 sensors
	Récuperation de 39 données
							humectation foliaire  compteur d'eau  alimentation #4
	2021-03-31 11:07:31+02:00                   0.0             0.0            0.000
	2021-03-31 11:22:20+02:00                   0.0             0.0            3.298
	2021-03-31 11:37:20+02:00                   0.0             0.0            3.299
	2021-03-31 11:52:20+02:00                   0.0             0.0            3.298
	2021-03-31 12:07:20+02:00                   0.0             0.0            3.301
	Ecriture des  données dans le fichier Debitmetre Grenache Rang 10.xlsx	

Code for UTC:

	from agstream.session import AgspSession
	session = AgspSession(timezoneName='UTC')
	session.login("masnumeriqueAgStream", "1AgStream", updateAgribaseInfo=True)
	session.describe()
	for abs in session.agribases :
	    print ("****************************************")
	    print (abs)
	    df = session.getAgribaseDataframe(abs)
	    print (df.tail())
    print("Fin du programme")

Output :

	**************************************************
	* Example 1 :  simplest way to get data
	* get the data, and feed an xlsfile
	**************************************************
	****************************************
	Compteur Mourvedre Rang 9(2301) AGRIBASE3S_STC SIGFOX containing 3 sensors
	Récuperation de 864 données
							compteur d'eau  alimentation #4  humectation foliaire
	2021-03-28 12:18:28+00:00             0.0            3.312                   0.0
	2021-03-28 12:33:29+00:00             0.0            3.316                   0.0
	2021-03-28 12:48:29+00:00             0.0            3.318                   0.0
	2021-03-28 13:03:29+00:00             0.0            3.314                   0.0
	2021-03-28 13:18:29+00:00             0.0            3.310                   0.0
	Ecriture des  données dans le fichier Compteur Mourvedre Rang 9.xlsx
	****************************************
	Debitmetre Grenache Rang 10(2299) AGRIBASE3S_STC SIGFOX containing 3 sensors
	Récuperation de 39 données
							humectation foliaire  compteur d'eau  alimentation #4
	2021-03-31 09:07:31+00:00                   0.0             0.0            0.000
	2021-03-31 09:22:20+00:00                   0.0             0.0            3.298
	2021-03-31 09:37:20+00:00                   0.0             0.0            3.299
	2021-03-31 09:52:20+00:00                   0.0             0.0            3.298
	2021-03-31 10:07:20+00:00                   0.0             0.0            3.301
	Ecriture des  données dans le fichier Debitmetre Grenache Rang 10.xlsx	

