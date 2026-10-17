import pymupdf
import json

document = pymupdf.open("Lecture.pdf")


Lecture_pages = [

]
for page in document:
    text = page.get_text()
    dic = {
        "page_number" : page.number + 1 , 
        "text" : text
    }
    Lecture_pages.append(dic)

print(len(Lecture_pages))

##print(Lecture_pages[0])
##print(Lecture_pages[0]["text"])
##print(Lecture_pages[2]["page_number"])


with open ("Lecture_data.json" , "w" , encoding="utf-8") as file :
    json.dump(Lecture_pages , file ,indent = 2 , ensure_ascii = False )


with open ("Lecture_data.json" , "r" ) as file :
    A = json.load(file)

print(A[2]["text"])

print("Good")
document.close()
