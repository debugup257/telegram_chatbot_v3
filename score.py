import pandas as pd
import numpy as np
from db import GlobalVar
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from ml_models import nlp
import pandas as pd
from itertools import chain

nlp=nlp()

tech_ans_yml=nlp.read_yaml("technical_answers.yaml")
tfidfvectorizer = TfidfVectorizer(analyzer='word')
db = GlobalVar("tiny.db.elephantsql.com", "ljbdoibm", "ljbdoibm", "TQeeYTeq6MXBw1EAnyW-7MrRwK4Qugk7")
df=db.get_data("faq")
applicants=db.get_data("applicants")
question=df["question"].to_list()
answer=df["answer"].to_list()

def tfidf_fit(question,tfidfvectorizer=tfidfvectorizer):
    correct_answers = tech_ans_yml
    tfidf_wm = (tfidfvectorizer.fit_transform(correct_answers))
    feature_names = [None]*len(tfidfvectorizer.vocabulary_)
    for key in tfidfvectorizer.vocabulary_:
        feature_names[tfidfvectorizer.vocabulary_[key]] = key
    df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(),columns = feature_names)
    return df_tfidfvect


def tfidf_transform(input_data,vec=tfidfvectorizer):
    input_data=input_data.lower()
    tfidf_wm_ip = vec.transform([input_data])
    feature_names = [None]*len(vec.vocabulary_)
    for key in vec.vocabulary_:
        feature_names[vec.vocabulary_[key]] = key
    df_tfidfvect_ip = pd.DataFrame(data = tfidf_wm_ip.toarray(),columns = feature_names)
    return(df_tfidfvect_ip)



final_sim=[]
for i in range(len(question)):
    print(i)
    for j in list(tech_ans_yml.keys()):
        if question[i]==j :
            vec1=tfidf_fit(tech_ans_yml[j])
            
            vec2=tfidf_transform(answer[i])
            print(vec1,vec2)
            all_sim=cosine_similarity(vec1, vec2)
            print(all_sim)
            avg_sim=pd.Series(list(chain.from_iterable(all_sim)))
            avg_sim=avg_sim.mean()
            final_sim.append(avg_sim)


df["score"]=final_sim
x=pd.DataFrame(df.groupby(by="id")["score"].sum())
x=x.merge(applicants, on='id', how='left')
x.to_csv("Interview_scores.csv")
df.to_csv("Interview_details.csv")



# send file 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def attatch_file(filename,message):
    filepath = "./" + filename

    with open(filepath, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    return message.attach(part)

sender_email = "hack.acs.drr@gmail.com"
receiver_email = "debugup257@gmail.com"
password = "acs@1234"
app_password='locignbulcnmrezu'

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "candidates interview scores"

body = "Please find the scores file of interviews taken today"
message.attach(MIMEText(body, "plain"))

attatch_file("Interview_scores.csv",message=message)
attatch_file("Interview_details.csv",message=message)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, text)