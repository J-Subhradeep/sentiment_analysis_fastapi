import requests

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": "Bearer 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"}


    
def analysis(output):
    ans=[	{'label': 'admiration', 'score': 0},
         {'label': 'happiness', 'score': 0}, 
         {'label': 'fear', 'score': 0}, 
         {'label': 'sadness', 'score': 0}, 
         {'label': 'disappointment', 'score': 0}, 
         {'label': 'anger', 'score': 0}, 
         {'label': 'curiosity', 'score': 0}, 
         {'label': 'neutral', 'score': 0},
         {'label': 'disapproval', 'score': 0}, 
         {'label': 'surprise', 'score': 0} 
    ]
    for i in output[0]:
          if i['label'] in ['admiration', 'approval', 'optimism','amusement','pride','gratitude']:
               ans[0]['score'] = max(ans[0]['score'],i['score'])
          elif i['label'] in ['joy', 'excitement','love','caring','relief','desire']:
                 ans[1]['score'] = max(ans[1]['score'],i['score'])
          elif i['label'] in ['fear','nervousness']:
                 ans[2]['score'] = max(ans[2]['score'],i['score'])
          elif i['label'] in ['sadness','remorse','grief']:
                ans[3]['score'] = max(ans[3]['score'],i['score'])
          elif i['label'] in  ['disappointment','embarrassment','disgust']:
                ans[4]['score'] = max(ans[4]['score'],i['score'])
          elif i['label'] in ['anger','annoyance']:
                ans[5]['score'] = max(ans[5]['score'],i['score'])
          elif i['label'] in ['curiosity', 'confusion']:
                ans[6]['score'] = max(ans[6]['score'],i['score'])
          elif i['label'] in ['neutral','realization']:
               ans[7]['score'] = max(ans[7]['score'],i['score'])
          elif i['label'] == 'disapproval':
               ans[8]['score']= max(ans[8]['score'],i['score'])
          elif i['label'] == 'surprise':
               ans[9]['score'] = max(ans[9]['score'],i['score'])
    return ans

def get_ten_var(input):
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    output = query({
	"inputs": input
    })
    # print("output",output)
    ans = analysis(output)
    # print(ans)
    return ans

def get_sentiment(input):
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    output = query({
	"inputs": input
    })
    ans = analysis(output)

    def get_highest():
        m=0
        sentiment=''
        for i in range(10):
            if ans[i]['score']>m:
                m=ans[i]['score']
                sentiment=ans[i]['label']
        return sentiment
    return get_highest()

# print(output)
