
import requests
from bs4 import BeautifulSoup


class Client:
    
    def __init__(self, identifiant, password):
        self.identifiant = identifiant
        self.password = password
        
        self.payload = {
            "login-ident": self.identifiant,
            "login-pwd": self.password,
            "bt-login": "1"
        }
        
        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        
        self.urlLogin = "https://mobile.free.fr/account/"
        
        listOfInternetInforamtion = ["conso", "consoMax", "restant", "horsForfait", "emprinteCarbone"]
        listOfAppelInforamtion = ["conso", "consoMax", "appelToMyCountry", "appelToInternational", "horsForfait"]
        listOfSMSInforamtion = ["conso", "consoMax", "maxNbSMS", "nbSMS", "horsForfait"]
        listOfMMSInforamtion = ["conso", "consoMax", "maxNbMMS", "nbMMS", "horsForfait"]

        self.dictOfAllInformation = {
            "internet": listOfInternetInforamtion,
            "appel": listOfAppelInforamtion,
            "SMS": listOfSMSInforamtion,
            "MMS": listOfMMSInforamtion
        }
                    
    

    def getConso(self) -> dict: 
        
        req = self.session.post(self.urlLogin, data=self.payload)

        soup = BeautifulSoup(req.content, "html.parser")

        userInfo = soup.find("div", {"class": "current-user__infos"})


        nameAcount = userInfo.find("div", {"class": "identite_bis"}).text.strip()
        identifiant = userInfo.findAll("div", {"class": "smaller"})[0].text.strip()
        ligne = userInfo.findAll("div", {"class": "smaller"})[1].text.strip()
        
        
        result= {}
        
        for _ in range(2):
            
            place = soup.find("div", {"class": "conso-local"}) if _ == 0 else soup.find("div", {"class": "conso-roaming"})
        
            result[place["class"][1].split("-")[1]] = {}
            
            for key, value in self.dictOfAllInformation.items():
                
                if key == "internet": itteration = 0
                elif key == "appel": itteration = 1
                elif key == "SMS": itteration = 2
                elif key == "MMS": itteration = 3
                
                result[place["class"][1].split("-")[1]][key] = {}
                result[place["class"][1].split("-")[1]][key][value[0]] = place.findAll("div", {"class": "number-circle"})[itteration].find("span").text.strip().replace("*","")
                result[place["class"][1].split("-")[1]][key][value[1]] = place.findAll("div", {"class": "number-circle"})[itteration].find("p").text.replace(result[place["class"][1].split("-")[1]][key][value[0]], "").replace("/", "").strip().replace("*","")
                if result[place["class"][1].split("-")[1]][key][value[1]] == "": 
                    result[place["class"][1].split("-")[1]][key][value[1]] = result[place["class"][1].split("-")[1]][key][value[0]]
                result[place["class"][1].split("-")[1]][key][value[2]] = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")[0].find("span").text.replace("/ ", "").strip().replace("*","")
                thirdInformation = result[place["class"][1].split("-")[1]][key][value[3]] = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")
                lastInternetAppelInformation = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")
                lastSMSMMSInformation = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")[1].text.strip().split(": ")[1].replace("*","")
                if key == "internet":
                    
                    result[place["class"][1].split("-")[1]][key][value[3]] = thirdInformation[1].text.strip().split(": ")[1].replace("*","")
                    
                elif key == "appel":
                    result[place["class"][1].split("-")[1]][key][value[3]] = thirdInformation[1].text.strip().split(": ")[1].replace("*","")
                    result[place["class"][1].split("-")[1]][key][value[4]] = lastInternetAppelInformation[2].text.strip().split(": ")[1].replace("*","")
                    
                else:
                    result[place["class"][1].split("-")[1]][key][value[3]] = thirdInformation[0].text.strip().split(" / ")[0].replace("*","")
                    result[place["class"][1].split("-")[1]][key][value[4]] = lastSMSMMSInformation
                
                if key == "internet" and place["class"][1].split("-")[1] == "local":
                    result[place["class"][1].split("-")[1]][key][value[4]] = lastInternetAppelInformation[2].text.strip().split(": ")[1].replace("*","")
            
        result["totalHorsForfait"] = 0
        for key, value in result.items():
            if key == "local" or key == "roaming":
                for key2, value2 in value.items():
                    for key3, value3 in value2.items():
                        if key3 == "horsForfait":
                            result["totalHorsForfait"] += float(value3.replace("€", ""))
        
        result["totalHorsForfait"] = str(result["totalHorsForfait"]) + "€"
        result["nameAcount"] = nameAcount
        result["identifiant"] = identifiant.split(" : ")[1]
        result["ligne"] = ligne.split(" : ")[1].replace(" ", "")
        
        return result
        
