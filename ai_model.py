
from sklearn.ensemble import RandomForestClassifier

def predict_trend(df):
    df["return"]=df["Close"].pct_change()
    df["target"]=(df["return"]>0).astype(int)
    df=df.dropna()

    X=df[["Open","High","Low","Volume"]]
    y=df["target"]

    model=RandomForestClassifier()
    model.fit(X,y)

    prob=model.predict_proba([X.iloc[-1]])[0][1]
    return round(prob*100,2)
