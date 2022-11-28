# fastapi--streamlit-hello-world
Sample of Fast API + Streamlit

## 1. Start FastAPI
After you open new terminal, write the following command.
```
$ poetry run uvicorn api:app --reload
``` 
Access to `http://127.0.0.1:8000`.  

It is OK if you can see the following message. 

![Image 1](/images/fastapi.png)

## 2. Start Streamlit
Open another ternimal and write the following command.

```
$ poetry run stereamlit run ui.py
``` 
Access to `http://localhost:8501/`. 

It is OK if you can see the following message. 

![Image 2](/images/streamlit.png)
