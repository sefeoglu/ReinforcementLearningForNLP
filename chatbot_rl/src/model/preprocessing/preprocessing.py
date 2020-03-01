
import pandas as pd
import json
import os
import numpy
"""
Data Preprocessing
"""
class Preprocess:

    def __init__(self):
        self.path = os.path.join("../data/pure/", "dataset_chitchat.py")

    def format_data(self):
        """
            Data Formater from json to csv
            Format each conversion
        """
        
        output = pd.DataFrame()
        dataset = json.load(open(self.path))

        for convo_id, convo in dataset.items():
            
            if 'prompt' in convo:
                prompt = convo['prompt']
            else:
                prompt = ""
            if 'start' in convo:
                start = convo['start']
            else:
                start = ""
            if 'ratings' in convo:
                ratings = convo['ratings']
            else:
                ratings = ""
            for a in convo['messages']:
                l = list(a)
                text = ''
                for m in l:
                    text += m['text']
                    text = text +" / "
                message_data = dict({'conv_id':convo_id,'prompt':prompt,'start':start,'ratings':ratings,'text': text, 'sender': m['sender'], 'timestamp':  m['timestamp']})
                output = output.append(message_data, ignore_index=True)   

        output.to_csv (r'../data/pure/formated_data.csv', sep='\t',index = False, header=True) 

# if __name__ == "__main__":
#     process = Preprocess()
#     process.format_data()
