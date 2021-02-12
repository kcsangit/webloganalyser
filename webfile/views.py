from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import media
from os import fdopen 


from django.http import HttpResponse 
import json

def home(request):
    return render(request,'webfile/home.html')


def getlog(request):
    if request.method == "POST":
        uploaded_file = request.FILES['logfile']
        global filename
        filename = uploaded_file.name
        print(filename)

    
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)

        
        def timecheck():
            f = open("/home/dixit/Desktop/webindividual/webserver/media/ecommerce.log","r")
            list1 = []


            for lines in f:
                list1.append(lines) 
            datetimelist = []
            for i in list1:
                text = i
                left = "["
                right = "]"
                # print(text[text.index(left)+len(left):text.index(right)])
                time = text[text.index(left)+len(left):text.index(right)]
                datetimelist.append(time)


            # print(datetimelist)

            timelist = []

            for x in datetimelist:
                tm = x[12:20]
                timelist.append(tm)

            print(timelist)
            return timelist



        def ipcheck():
            import requests
            import json
            f = open("/home/dixit/Desktop/webindividual/webserver/media/ecommerce.log","r")
            list1 = []
            """
            first of all , we all know single line is single log

            list was created to to append each log in list



            """

            for lines in f:
                list1.append(lines) #append each log as single element of list


            """
            here fullip is list of every ip of logs,firstly.

            """


            fullip = []  
            length = len(list1)
            for p  in range(0,length):
                ipstring = []
                for q in list1[p]:
                    ipstring.append(q)
                    if q == " ":
                        break
                
                seperator = ''
                singleip = seperator.join(ipstring)
                fullip.append(singleip)

            print(fullip)
            countries = []
            apiKey = "521c8bf2ec3f4bf8a7535fb8e17b1ad8"
            
            for ip in fullip:
                url = 'https://api.ipgeolocation.io/ipgeo?apiKey=' + apiKey+'&ip='+ip + '&fields=country_name'
                    
                    
                response = requests.get(url)
                a = response.text
                data = json.loads(a)
                # dicta = dict(a)'
                print(data["country_name"])
                
                
                

                countries.append(data["country_name"])
            
            print(countries)
            return countries





        def oscheck():
            f = open("/home/dixit/Desktop/webindividual/webserver/media/ecommerce.log","r")
            list1 = []


            for lines in f:
                list1.append(lines) 
            operating = []
            for os in list1:
                a=os.split()[12]
                operating.append(a)
            
            print(operating)
            return operating

        def browsercheck():
            f = open("/home/dixit/Desktop/webindividual/webserver/media/ecommerce.log","r")
            list1 = []


            for lines in f:
                list1.append(lines) 
            browser = []
            for os in list1:
                a=os.split()[11]
                browser.append(a)
            
            print(browser)
            return browser
            

            

            



                
                



        

        timelist=timecheck()
        countrylist=ipcheck()
        oslist=oscheck()
        browserlist=browsercheck()
        countrynum = {}
        osnum={}
        browsernum = {}

        for cou in countrylist: 

            if cou in countrynum: 

                countrynum[cou] = countrynum[cou]+1 

            else: 

                countrynum[cou] = 1 

 

        for oses in oslist: 

            if oses in osnum: 

                osnum[oses] = osnum[oses]+1 

            else: 

                osnum[oses] = 1 

        

        for browser in browserlist: 

            if browser in browsernum: 

                browsernum[browser] = browsernum[browser]+1 

            else: 

                browsernum[browser] = 1 
            

        print(browsernum.items())
        print(osnum.items())
        print(countrynum.items())

        brname=[]
        brnum=[]

        cname = []
        cnum = []

        oname =[]
        onum=[]

        for x in browsernum.keys():
            brname.append(x)
        for y in browsernum.values():
            brnum.append(y)



        for x in osnum.keys():
            oname.append(x)

        for y in osnum.values():
            onum.append(y)



        for x in countrynum.keys():
            cname.append(x)
        
        for y in countrynum.values():
            cnum.append(y)
            


        
        

        
        return render(request, 'webfile/getlog.html',{
            'browsername':brname,'browsernumber':brnum,
            'c':countrynum,
            'os':osnum,


         'dateTime': timelist})
















    










