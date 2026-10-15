import json

Lecture = {
    "title" : "Introduction to AI",
    "subject" : "Artificial intelligence",
    "filename": "Lecture.txt" ,
    "pages" : 12 ,
    "keywords" : ["Ai" , "Python" , "Machine Learning"]
}


with open("Lecture_info.json" , "w" ) as file:
    json.dump(Lecture , file , indent  = 4 )


with open ("Lecture_info.json" , "r") as file:
    loaded_file = json.load(file)


print("Lecture Title: " , loaded_file["title"])
print("Suject: " , loaded_file["subject"])
print("Number of Pages: " , loaded_file["pages"])
print("Keywords: " , ", ".join(loaded_file["keywords"]) )