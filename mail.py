# Importing libraries 
import imaplib, email 
  
user = 'nitikeshpro@gmail.com'
password = '*****************' #Get this app password from https://myaccount.google.com/security 
imap_url = 'imap.gmail.com'
class mail:
    def __init__(self):
        pass
    # Function to get email content part i.e its body part 
    def get_body(self,msg): 
        if msg.is_multipart(): 
            return self.get_body(msg.get_payload(0)) 
        else: 
            return msg.get_payload(None, True) 
  
    # Function to search for a key value pair  
    def search(self,key, value, con):  
        result, data = con.search(None, key, '"{}"'.format(value)) 
        return data 
  
    # Function to get the list of emails under this label 
    def get_emails(self,result_bytes,con): 
        msgs = [] # all the email data are pushed inside an array 
        for num in result_bytes[0].split(): 
            typ, data = con.fetch(num, '(RFC822)') 
            msgs.append(data) 
      
        return msgs 
    def getCode(self):
        con = imaplib.IMAP4_SSL(imap_url)  
        con.login(user, password)  
        con.select('Inbox')  
        msgs = self.get_emails(self.search('FROM', 'security-noreply@linkedin.com', con),con) 

        for sent in msgs[-1]: #this will get the latest email in your gmail
            if type(sent) is tuple:  
                content = str(sent[1], 'utf-8')  
                #content=content.split('Please use this verification code to complete your sign in: ')[1]  #this is for getting linkedin passcode
                #code=content[0]+content[1]+content[2]+content[3]+content[4]+content[5]
                return content
        return 0
        
#mail().getCode()

