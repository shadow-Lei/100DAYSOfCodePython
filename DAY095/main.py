from fastapi import FastAPI
import requests
from pydantic import BaseModel,Field
import datetime
import pandas as pd
from typing import Optional
import json

docsurl='/covid19vaccinate'
app = FastAPI(docs_url=docsurl,redoc=None)
yesterday=datetime.date.today() - datetime.timedelta(days=1)

class Query(BaseModel):
    date: Optional[datetime.date]=Field(yesterday,title='欲搜尋的日期，預設為昨日')
    vaccine: Optional[str] = Field("ALL",title='如無選擇，顯示全部廠牌的統計，疫苗接種類型可搜尋:Oxford/AstraZeneca、Moderna、BNT、高端、ALL')

class VaccinateData(BaseModel):
    country:str='國家'
    date:datetime.date='統計日期'
    vaccine:str='疫苗廠牌'
    cumulativefirst:int='第一劑累計接種人次'
    cumulativesecond:int='第二劑累計接種人次'
    cumulativeadd:int='追加劑累計接種人次'

def getdata():
    url='https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2004'
    res=requests.get(url)
    resjson=res.json()
    return resjson
    
resjson=None

@app.post("/vaccinatestatistic",tags=['vaccinate'])
async def vaccinate(query: Query):
    date=query.date
    vaccine=query.vaccine if query.vaccine else 'All'
    global resjson
    if not resjson:
        resjson=getdata()
    df = pd.DataFrame.from_dict(resjson)
    
    df.columns=['id','國家','統計日期','疫苗廠牌','第一劑累計接種人次','第二劑累計接種人次','追加劑累計接種人次']
    returndf=df.loc[(df['統計日期']==str(date)) & (df['疫苗廠牌']==vaccine)]
    returndf=returndf.drop('id',axis=1) 
    js = returndf.to_json(orient='records',force_ascii=False)
    
    return json.loads(js)
