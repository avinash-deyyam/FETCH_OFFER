from fastapi import FastAPI
import uvicorn
from model import prompt, scores


app = FastAPI()

@app.post("/offers")
async def offer_route(text: str=''):
    if not text:
        return {"text" :"please enter text"}
    else:
        offers = prompt(text)
        score = scores(offers,text)
        if type(score) == str:
            return {"text":'No offers found'}
        else:
            return score.to_json(orient="records")
    
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)