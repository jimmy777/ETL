'''
Created on Nov 2, 2012

@author: marek
'''
import re
from sre_parse import Pattern
from datetime import datetime
from compiler.pycodegen import EXCEPT
from xml.etree import ElementTree
class Util(object):
    
    def __init__(self):
        '''
        '''
    
    def isInteger(self,value):
        return isinstance(value, int)
    
    def canBeCastedToInteger(self, value):
        ex = re.compile("^\d+$|^[-+]\d+$" )
        return re.match(ex, value)
    
    def castToInteger(self,value):
        return int(value)
    
    def isPositive(self,value):
        return value>0
    
    def isBoolean(self,value):
        if isinstance(value, bool):
            return True
        else:
            ex = re.compile("True|False")
            if re.match(ex, value): return True
            else: return False
    
    def castStringToBoolean(self,value):
        exTrue = re.compile("true",re.IGNORECASE)
        exFalse = re.compile("false", re.IGNORECASE)
        exAno = re.compile("ano", re.IGNORECASE)
        exNie = re.compile("nie", re.IGNORECASE)
        if re.match(exTrue, value): return True
        elif re.match(exFalse, value): return False
        elif re.match(exAno, value): return True
        elif re.match(exNie, value): return False
        else: return None
    
    def canCastStringToBoolean(self,value):
        ex = re.compile("true|false|ano|nie", re.IGNORECASE)
        res = re.match(ex,value)
        if res != None:
            return res
        else : return False
        
         
    def castStringIntegerToBoolean(self,value):
        val = self.castToInteger(value)
        if val == 0:
            return False
        if val == 1:
            return True
        else:
            return None
    
    def isPrevzatie(self,values):
        pattern = re.compile("osobny odber|kurier|posta")
        ret = pattern.match(values)
        if ret !=None:
            return values == ret.group()
        else : return False
        
    def valitedPrevzatie(self, values):
        pat1 = re.compile("osobny odber", re.IGNORECASE)
        pat2 = re.compile("kurier",re.IGNORECASE)
        pat3 = re.compile("posta", re.IGNORECASE)
        
        if re.match(pat1, values):
            return "osobny odber"
        if re.match(pat2, values):
            return "kurier"
        if re.match(pat3, values):
            return "posta"
        else:
            return None
    
    def isPlatba(self,values):
        pattern = re.compile("hotovost|prevod|online")
        ret = pattern.match(values)
        if ret !=None:
            return values == ret.group()
        else: return False
    
    def validatePlatba(self,values):
        pat1 = re.compile("hotovost", re.IGNORECASE)
        pat2= re.compile("prevod", re.IGNORECASE)
        pat3 = re.compile("online", re.IGNORECASE)
        
        if re.match(pat1, values):
            return "hotovost"
        if re.match(pat2, values):
            return "prevod"
        if re.match(pat3, values):
            return "online"
        return None
    def isStavObjednavky(self,values):
        pattern = re.compile("vybavena|pripravena na expediciu|pripravuje sa|zrusena|prijata")
        ret = pattern.match(values)
        if ret !=None:
            return values == ret.group()
        else: return False
        
    def validateStavObjednavky(self,value):
        pat1 = re.compile("vybavena", re.IGNORECASE)
        pat2= re.compile("pripravena na expediciu", re.IGNORECASE)
        pat3 = re.compile("pripravuje sa", re.IGNORECASE)
        pat4 = re.compile("zrusena", re.IGNORECASE)
        pat5 = re.compile("prijata", re.IGNORECASE)
        
        if pat1.match(value):
            return "vybavena"
        if pat2.match(value):
            return "pripravena na expediciu"
        if pat3.match(value):
            return "pripravuje sa"
        if pat4.match(value):
            return "zrusena"
        if pat5.match(value):
            return "prijata"
        return None
            
    def isValidName(self,value):
        pat = re.compile("^[A-Z][a-z]+$")
        ret = pat.match(value)
        if ret!=None:
            return ret.group()==value
        else: return False
        
    def validateName(self,value):
        pat = re.compile("^[a-z]+$",re.IGNORECASE)
        if pat.match(value):
            val = value.lower()
            return val.capitalize()
        else : return None
        
    def isMailValid(self,mail):
        pat = re.compile("^[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$",re.IGNORECASE)
        ret = pat.match(mail)
        if ret!=None:
            return ret.group() == mail
        else : return False
    def isTextValid(self,text):
        if len(text)<250:
            return True
        else : return False
        
    def castToBoolean(self,valueToValidate):
        if self.canBeCastedToInteger(valueToValidate): 
            val = self.castToInteger(valueToValidate)
            if val == 0:
                return False
            if val == 1:
                return True
        elif self.canCastStringToBoolean(valueToValidate):
            return self.castStringToBoolean(valueToValidate)
        else: return None
    
    def isValidInteger(self,value):
        if self.isInteger(value) and self.isPositive(value):
            return True
        elif self.canBeCastedToInteger(value) and self.isPositive(self.castToInteger(value)):
            return True
        else : return False
        
    def validateInteger(self,valueToValidate):
        if  self.isInteger(valueToValidate) and not self.isPositive(valueToValidate):
            return valueToValidate *(-1)
        elif self.canBeCastedToInteger(valueToValidate) and not self.isPositive(self.castToInteger(valueToValidate)):
            return self.castToInteger(valueToValidate) * (-1)
        elif self.canBeCastedToInteger(valueToValidate):
            return self.castToInteger(valueToValidate)
        else: return None
        
    def isValidAdress(self,adress):
        pat = re.compile("^[A-Z][a-z ]* \d{1,4}$")
        ret = pat.match(adress)
        if ret!=None:
            return ret.group()==adress
        else: return False
    def isValidCisloUctu(self,cUctu):
        pat = re.compile("^[0-9]{10}/\d{4}$")
        ret = pat.match(cUctu)
        if ret!=None:
            return ret.group()==cUctu
        else: return False
    def isValidICO(self,value):
        pat = re.compile("^\d{8}$")
        ret = pat.match(value)
        if ret !=None:
            return value == ret.group()
        else: return False
    def isDostupnostTovaru(self,value):
        pat = re.compile("dostupne|nedostupne|na objednavku")
        ret = pat.match(value)
        if ret!=None:
            return ret.group() == value
        else : return False
        
    def validateDostupnost(self,valueToValidate):
        pat1 = re.compile("dostupne", re.IGNORECASE)
        pat2 = re.compile("nedostupne", re.IGNORECASE)
        pat3 = re.compile("na objednavku", re.IGNORECASE)
        
        if re.match(pat1,valueToValidate):
            return "dostupne"
        if re.match(pat2,valueToValidate):
            return "nedostupne"
        if re.match(pat3,valueToValidate):
            return "na objednavku"
        else: return None
        
    def isMutacia(self,value):
        pattern = re.compile("^[A-Z]{3}$")
        match = pattern.match(value)
        if match!=None:
            return match.group() == value
        else: return False
    def validateMutacia(self,value):
        pattern = re.compile("^[A-Z]{3}$",re.IGNORECASE)
        match = pattern.match(value)
        if match!=None:
            return value.upper()
        else: return None
        
    def isValidDate(self,date):
        dt = datetime.strptime(str(date), "%y-%m-%d %H:%M:%S.%f")
        return (dt is not None)
    
    def validateDate(self,value):
        posibleValues = []
        replaced = value
        posibleValues.append(replaced.replace(".","-"))
        replaced = value
        posibleValues.append(replaced.replace("/","-"))
        for val in posibleValues:
            pattern = re.compile("[0-9]{1,2}\-[0-9]{1,2}\-[0-9]{4}")
            var = pattern.match(val)
            if var is not None:
                if var.group() == val and self.isValidDate(val):
                    return val
        return None
    
    def isISBN(self,value):
        pattern = re.compile("[0-9]{13}")
        val = pattern.match(value)
        if val is not None:
            return val.group() == value
        else: return False
    def isFloat(self,value):
        pattern = re.compile("^[0-9]+,[0-9]+$")
        val = pattern.match(value)
        if val is not None:
            return val.group() == value
        else : return False
    
    def validateFloat(self,value):
        value.strip()
        val = value.replace(" ","")
        val = val.replace("'","")
        val = val.replace(".",",")
        pattern = re.compile("^[0-9]+,[0-9]+$")
        ret = pattern.match(val)
        if ret is not None:
            if ret.group() == val:
                return val
            else: return None
        else: return None
    def isValidVekovaDostupnost(self,value):
        return self.isValidInteger(value) and self.castToInteger(value)<200
    
    def isValidXML(self,xmlBody):
        try:
            item = ElementTree.fromstring(xmlBody)
            
        except Exception:
            return False
        
        return True
    
    def validateXML(self,xmlBody):
        return None
    
    def isValidDenVTyzdni(self,den):
        pattern = re.compile("Pondelok|Utorok|Streda|Stvrtok|Piatok|Sobota|Nedela")
        ret = pattern.match(den)
        if ret is not None:
            return ret.group()==den
        else: return False
    
    def validateValidDenVTyzdni(self,den):
        alteredDen = den.lower().capitalize()
        pattern = re.compile("Pondelok|Utorok|Streda|Stvrtok|Piatok|Sobota|Nedela")
        ret = pattern.match(alteredDen)
        if ret is not None:
            return alteredDen
        else: return None
        
    def isValidDic(self,dic):
        pattern = re.compile("^\d{10}$")
    
    def isValidLength(self,string,length):
        return len(string)<=length
                     

        
        