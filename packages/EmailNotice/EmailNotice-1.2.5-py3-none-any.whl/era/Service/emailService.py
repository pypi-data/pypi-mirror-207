from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from era.Database.Model.emailTemplateModel import EmailTemplateModel
from era.Database.Model.recipientModel import RecipientModel
from era.Utility.ConfigUtility import GetConfigSingletion
from era.Logger.logger import Logger
import smtplib, ssl
import os

class EmailService:

    # 0 - EMail Matching
    # 1 - Attachment
    # 2 - CC
    # 3 - BCC
    # 4 - Subject (To override template value)
    # 5 - All customer data
    __CUSTOMER_DATA_START_IDX = 5


    def __init__(self) -> None:
        self.config_obj = GetConfigSingletion()
        self.logger = Logger()
        self.emailServer = None
        self.emailContext = ssl.create_default_context()
        self.isLogin = False
        pass


    #DB operation
    def GetAllEmailAccountList(self):
        pass

    def AddNewEmailAccount(self):
        pass

    def UpdateEmailAccount(self):
        pass

    def DeleteEmailAccount(self):
        pass

    def IsLogin(self) -> bool:
        return self.isLogin


    #Email Service
    def ConnectEmailAccount(self)->bool:
        try:
            self.emailServer = smtplib.SMTP(self.config_obj.ReadConfig('email','smtpServer'),self.config_obj.ReadConfig('email','port'))
            self.emailServer.starttls(context=self.emailContext) # Secure the connection
            self.emailServer.login(self.config_obj.ReadConfig('email','emailAc'), self.config_obj.ReadConfig('email','emailPw'))
            self.isLogin = True
        except:
            self.isLogin = False
        finally:
            return self.isLogin
        
    def DisconnectEmailAccount(self):
        pass

    def SendEmail(self,emailList:list[RecipientModel], template:EmailTemplateModel, attachmentData:list) -> list[str]:
        sendError = []

        for recipient in emailList:
            try:
                mimemsg = MIMEMultipart()

                mimemsg['From']=self.config_obj.ReadConfig('email','emailAc')
                mimemsg['To']=recipient.GetRecipientEMail()
                mimemsg['Subject']=template.GetSubject()

                # file = open(template.GetPath(),encoding="utf-8")#append mode 
                # templateData = file.read()
                # file.close()
                if attachmentData != None:
                    templateData = self.FormatEmailTemplateWithData(recipient.GetRecipientEMail(),attachData=attachmentData,emailTemplate=template)
                    mimemsg = self.__AddSelfAttachment(recipient.GetRecipientEMail(),attachData=attachmentData,emailTemplate=template,emailObject=mimemsg)
                    mimemsg = self.__AddCCandBCC(recipient.GetRecipientEMail(),emailObject=mimemsg,attachData=attachmentData)
                else:
                    file = open(template.GetPath(),encoding="utf-8")#append mode 
                    templateData = file.read()
                    file.close()
                mimemsg.attach(MIMEText(templateData, 'html' if self.CheckIsHtmlFormat(templateData) else 'plain'))
                self.ConnectEmailAccount()
                self.emailServer.send_message(mimemsg)
            except Exception as ex:
                sendError.append(recipient.GetRecipientEMail())
        
        return sendError
    

    def GetEmailAccount(self)->str:
        try:
            return self.config_obj.ReadConfig('email','emailAc')
        except:
            return ""

    def FormatEmailTemplateWithData(self,email:str, attachData:list ,emailTemplate: EmailTemplateModel) -> str:

        if attachData == None:
            if emailTemplate != None:
                file = open(emailTemplate.GetPath(),encoding="utf-8")#append mode 
                sample = file.read()
                file.close()
                return sample
            else:
                return None

        headerData = attachData[0]
        matchData = None
        for data in attachData:
            try:
                data.index(email)
                matchData = data
                break
            except ValueError:
                continue 
        
        if matchData == None:
            return None

        mapData = {}
        for idx,header in enumerate(headerData[self.__CUSTOMER_DATA_START_IDX:],start=self.__CUSTOMER_DATA_START_IDX):
            mapData[headerData[idx]] = matchData[idx]

        if emailTemplate != None:
            file = open(emailTemplate.GetPath(),encoding="utf-8")#append mode 
            sample = Template(file.read()).substitute(mapData)
            file.close()
            return sample
        else:
            return None

    def __AddSelfAttachment(self,email:str, attachData:list ,emailTemplate: EmailTemplateModel, emailObject:MIMEMultipart) ->MIMEMultipart:

        #No need to attach anything
        if not emailTemplate.GetContainAttachment() and not emailTemplate.GetContainData():
            return emailObject

        matchData = None
        for data in attachData:
            try:
                data.index(email)
                matchData = data
                break
            except ValueError:
                continue 
        
        #Cannot email which email address belongs to
        if matchData == None:
            return emailObject

        totalPath = matchData[1]
        if totalPath == totalPath:
            totalPath = totalPath.split(";")
            for path in totalPath:
                self.__FormAttachmentObject(filePath=path,emailObject=emailObject)
        

        #Check if override subject
        customSubject = matchData[4]
        if customSubject == customSubject:
            emailObject['Subject']=customSubject
        
        return emailObject

    def __FormAttachmentObject(self,filePath:str,emailObject:MIMEMultipart):
        fileName = os.path.basename(filePath)

        name, file_extension = os.path.splitext(filePath)

        if file_extension in ['.png','jpeg','.jpg']:
            with open(filePath, 'rb') as fp:
                img = MIMEImage(fp.read())
                img.add_header('Content-Disposition', 'attachment', filename=fileName)
                emailObject.attach(img)
        else:
            pdf = MIMEApplication(open(filePath, 'rb').read())
            pdf.add_header('Content-Disposition', 'attachment', filename= fileName)
            emailObject.attach(pdf)        

        
        return emailObject
    
    def GetAttachmentListByEmail(self, email:str, attachData:list)->list:
        if attachData == None:
            return None

        headerData = attachData[0]
        matchData = None
        for data in attachData:
            try:
                data.index(email)
                matchData = data
                break
            except ValueError:
                continue 

        return matchData
    
    def __AddCCandBCC(self,email:str,emailObject:MIMEMultipart,attachData:list)->MIMEMultipart:
        if attachData == None:
            return emailObject
        else:
            matchData = None
            for data in attachData:
                try:
                    data.index(email)
                    matchData = data
                    break
                except ValueError:
                    continue 
            
            #Cannot email which email address belongs to
            if matchData == None:
                return emailObject
            
            ccList = matchData[2]
            if ccList == ccList:
                emailObject['Cc']  = ccList

            bccList = matchData[3]
            if bccList == bccList:
                emailObject['Bcc']  = bccList    

            return emailObject
    
    def CheckIsHtmlFormat(self,template:str)->bool:
        if template.startswith('<!DOCTYPE html>') and template.endswith('</html>'):
            return True
        else:
            return False
