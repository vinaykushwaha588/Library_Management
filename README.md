# Library_Management || MobileOTP Verification with JWT Authentication


# PhoneOTP Generation usign Third API - 2Factor -
link 2Factor - https://2factor.in/v3/free-bulk-sms-service-trial/index.php
# Using class based Views (APIView and Viewsets or ModelViewsets)

---------------------------------------------------: MobileOTP Verification with JWT Authentication :---------------------------------------------------


http://127.0.0.1:8000/account/send-otp/ - This url working for register user and otp send for given mobile number. \method - POST\ ||
http://127.0.0.1:8000/account/verify/   - This url working for otp-verification. and given mobile number recieved 6 digit otp. \method - POST\ ||
http://127.0.0.1:8000/account/login/  - This url working for login user and generate jwt  Refresh Token and Access Token . \method - POST\ ||
http://127.0.0.1:8000/account/list/ - This url working for Entry on Library - After HIT - Access Token -- Show Library --- Viewsets link. \method - GET\ ||
--------------------------------------- Viewsets link - "book": "http://127.0.0.1:8000/account/list/book/"  

----------------------------------- After Clicking link Open New Tab -- Access Token Hit is Mendatory ------------------------------------------------

http://127.0.0.1:8000/account/list/book/  - This Url working for show all Library Books Method - GET \\  ['TOken Hit Mendatory']
http://127.0.0.1:8000/account/list/book/  - This Url working for insert book on Library Books Method - POST \\ ['TOken Hit Mendatory']
http://127.0.0.1:8000/account/list/book/2/  - This Url working for Update Books on Library Method - PUT \\ ['TOken Hit Mendatory']
http://127.0.0.1:8000/account/list/book/2/  - This Url working for Delete Books on Library Method - Delete \\ ['TOken Hit Mendatory']



