import requests
import json 
import time
import datetime



headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
url = 'https://api.telegram.org/bot1911454791:AAGY8plE9jCxjoB8frQW4CU4GyNA9ZXdiiI/sendMessage'
myobj = {
    "chat_id": '@mannurvaccineupdates',
    "text": "Please use the below link to book your slot. PLEASE BOOK YOUR SLOTS WITHIN A MINUTE AFTER RECEIVING THE ALERTS",
    "parse_mode": "markdown",
    "reply_markup": {
        "inline_keyboard" : [
            [
                {
                    "text" : "Book Now",
                    "url" : "https://selfregistration.cowin.gov.in"
                }
            ]
        ]
   }
}
datetime=datetime.datetime.now() + datetime.timedelta(days=0)
datetime=datetime.strftime('%d-%m-%Y')
session_list=["null"]
pin="682025"
while(1):
    for i in range(306,308):
        x="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pin+"&date="+datetime
        data=requests.get(x,headers=headers)
        results=json.loads(data.text)
        count=results["sessions"]
        
        if(len(count)>0):
            cc=0
            for session in count:
                if session_list[0]=="null":
                    msg=[]
                    msg.append({'Center':session["name"],'Pincode':session["pincode"],'Date':session["date"],'Dose1':session["available_capacity_dose1"],'Dose2':session["available_capacity_dose2"]})
                    msg.append({"Type":session["fee_type"],"Vaccine":session["vaccine"],"Fee":session["fee"]})
                    parse_data=json.dumps(msg)
                    parse_data=parse_data.replace("{","")
                    parse_data=parse_data.replace("}","\n\n")
                    parse_data=parse_data.replace("[","")
                    parse_data=parse_data.replace("]","")                        
                    parse_data=parse_data.replace(",","\n")
                    nd_url="https://api.telegram.org/bot1911454791:AAGY8plE9jCxjoB8frQW4CU4GyNA9ZXdiiI/sendMessage?chat_id=@mannurvaccineupdates&text="+parse_data
                    requests.get(nd_url)
                    requests.post(url, json= myobj, headers=headers)
                    print(parse_data)
                    print(session_list)
                    session_list.pop(0)
                    session_list.append(session["session_id"])     
                    print(session_list) 
                else:
                    for i in session_list:
                        if session["session_id"]==i :
                            print(session["session_id"]==i)
                            cc=cc+1
                    if cc==0:
                        msg=[]
                        msg.append({'Center':session["name"],'Pincode':session["pincode"],'Date':session["date"],'Dose1':session["available_capacity_dose1"],'Dose2':session["available_capacity_dose2"]})
                        msg.append({"Type":session["fee_type"],"Vaccine":session["vaccine"],"Fee":session["fee"]})
                        parse_data=json.dumps(msg)
                        parse_data=parse_data.replace("{","")
                        parse_data=parse_data.replace("}","\n\n")
                        parse_data=parse_data.replace("[","")
                        parse_data=parse_data.replace("]","")                        
                        parse_data=parse_data.replace(",","\n")
                        nd_url="https://api.telegram.org/bot1911454791:AAGY8plE9jCxjoB8frQW4CU4GyNA9ZXdiiI/sendMessage?chat_id=@mannurvaccineupdates&text="+parse_data                            
                        requests.get(nd_url)
                        requests.post(url, json= myobj, headers=headers)
                        print(parse_data)
                        print(session_list)
                        session_list.append(session["session_id"])
                        print(session_list) 
        time.sleep(15)
