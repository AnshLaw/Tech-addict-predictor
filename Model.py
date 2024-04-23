import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("C:\\Users\\anshr\\Desktop\\HOSA\\dataset.csv")
df[['Act1','Act2','Act3','Act4','Act5','Act6']] = df.Activities.str.split(',',expand=True)
df[['App1','App2','App3','App4','App5','App6','App7','App8','App9','App10','App11','App12','App13','App14','App15']] = df.Apps.str.split(',',expand=True)

df["Act1"][df["Act1"].notnull()] = 1
act1 = df["Act1"]
act1.fillna(value = "0", inplace=True)

df["Act2"][df["Act2"].notnull()] = 1
act2 = df["Act2"]
act2.fillna(value = "0", inplace=True)

df["Act3"][df["Act3"].notnull()] = 1
act3 = df["Act3"]
act3.fillna(value = "0", inplace=True)

df["Act4"][df["Act4"].notnull()] = 1
act4 = df["Act4"]
act4.fillna(value = "0", inplace=True)

df["Act5"][df["Act5"].notnull()] = 1
act5 = df["Act5"]
act5.fillna(value = "0", inplace=True)

df["Act6"][df["Act6"].notnull()] = 1
act6 = df["Act6"]
act6.fillna(value = "0", inplace=True)

df["App1"][df["App1"].notnull()] = 1
app1 = df["App1"]
app1.fillna(value = "0", inplace=True)

df["App2"][df["App2"].notnull()] = 1
app2 = df["App2"]
app2.fillna(value = "0", inplace=True)

df["App3"][df["App3"].notnull()] = 1
app3 = df["App3"]
app3.fillna(value = "0", inplace=True)

df["App4"][df["App4"].notnull()] = 1
app4 = df["App4"]
app4.fillna(value = "0", inplace=True)

df["App5"][df["App5"].notnull()] = 1
app5 = df["App5"]
app5.fillna(value = "0", inplace=True)

df["App6"][df["App6"].notnull()] = 1
app6 = df["App6"]
app6.fillna(value = "0", inplace=True)

df["App7"][df["App7"].notnull()] = 1
app7 = df["App7"]
app7.fillna(value = "0", inplace=True)

df["App8"][df["App8"].notnull()] = 1
app8 = df["App8"]
app8.fillna(value = "0", inplace=True)

df["App9"][df["App9"].notnull()] = 1
app9 = df["App9"]
app9.fillna(value = "0", inplace=True)

df["App10"][df["App10"].notnull()] = 1
app10 = df["App10"]
app10.fillna(value = "0", inplace=True)

df["App11"][df["App11"].notnull()] = 1
app11 = df["App11"]
app11.fillna(value = "0", inplace=True)

df["App12"][df["App12"].notnull()] = 1
app12 = df["App12"]
app12.fillna(value = "0", inplace=True)

df["App13"][df["App13"].notnull()] = 1
app13 = df["App13"]
app13.fillna(value = "0", inplace=True)

df["App14"][df["App14"].notnull()] = 1
app14 = df["App14"]
app14.fillna(value = "0", inplace=True)

df["App15"][df["App15"].notnull()] = 1
app15 = df["App15"]
app15.fillna(value = "0", inplace=True)

df = df.drop(columns = ["Activities","Apps"])

ovrScore = []

for idx in df.index:
    score = 0
    if df["Age"][idx] == 0:
        score += 10
    if df["Act1"][idx] == 1:
        score += 10
    if df["Act2"][idx] == 1:
        score += 10
    if df["Act3"][idx] == 1:
        score += 10
    if df["Act4"][idx] == 1:
        score += 10
    if df["Act5"][idx] == 1:
        score += 10 
    if df["Act6"][idx] == 1:
        score += 10
    if df["App1"][idx] == 1:
        score += 10
    if df["App2"][idx] == 1:
        score += 10  
    if df["App3"][idx] == 1:
        score += 10  
    if df["App4"][idx] == 1:
        score += 10  
    if df["App5"][idx] == 1:
        score += 10  
    if df["App6"][idx] == 1:
        score += 10  
    if df["App7"][idx] == 1:
        score += 10  
    if df["App8"][idx] == 1:
        score += 10  
    if df["App9"][idx] == 1:
        score += 10  
    if df["App10"][idx] == 1:
        score += 10  
    if df["App11"][idx] == 1:
        score += 10  
    if df["App12"][idx] == 1:
        score += 10  
    if df["App13"][idx] == 1:
        score += 10  
    if df["App14"][idx] == 1:
        score += 10  
    if df["App15"][idx] == 1:
        score += 10 
    if df["Screen Time"][idx] == 1:
        score += 10
    if df["Screen Time"][idx] == 2:
        score += 20
    if df["Screen Time"][idx] == 3:
        score += 30
    if df["Screen Time"][idx] == 4:
        score += 40
    if df["Technology affect"][idx] == 1:
        score += 5
    if df["Technology affect"][idx] == 0:
        score -= 5
    if df["Improve Addiction"][idx] == 0:
        score += 5
    if df["Improve Addiction"][idx] == 1:
        score -= 5
        
    ovrScore.append(score)
    

df["Target"] = 0
df["Overall_score"] = ovrScore
for idx in df.index:
    if ovrScore[idx] >= 105:
        df["Target"][idx] = 1
    if ovrScore[idx] < 105:
        df["Target"][idx] = 0
        
df = df.drop(columns = ["Overall_score"])

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:25],df.iloc[:,25], random_state = 42,test_size=0.20, shuffle= True)

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

pickle.dump(knn, open("knn.pkl", "ab"))





           


    
    
    
    