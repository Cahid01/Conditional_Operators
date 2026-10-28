#Düzgün email və şifrəni dəyişənlərdə saxlayın. İstifadəçidən email və şifrə soruşun.

#Email səhvdirsə: “Hesab tapılmadı”
#Şifrə səhvdirsə: “Şifrə yanlışdır”
#Hər ikisi düzdürsə: “Xoş gəldiniz!”



email_1 = "python.3.15.2@gmail.com"
password_1 = "Python123"
email = input("Emali daxil edin: ")
password = input("Şifrəni daxil edin: ")
if email_1 == email and password_1 == password:
    print("Xoş gəldiniz! ")
elif email_1 != email:
    print("Hesab tapılmadı!")
else:
     print("Şifrə yalnışdır!")