from neo4j import GraphDatabase
import pandas as pd
from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config
import json
import os
import numpy

class GraphDB(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self.path = os.path.join("/home/sefika/ReinforcementLearningForNLP/chatbot_rl/src/model/data/pure/data_train_txt/formated_data_train.txt")

    def close(self):
        self._driver.close()

    def print_convo(self):
        # get text data
        #self.text_data = self.read_data_text()
        path = os.path.join("/home/sefika/ReinforcementLearningForNLP/chatbot_rl/src/model/data/pure/", "dataset_chitchat.py")
        dataset = json.load(open(path))
        
        id_list = []
        for convo_id, convo in dataset.items():
            id_list.append(convo_id)
       
        start_flag = True
        #for index, row in df.iterrows():
        for convo_id, convo in dataset.items():
           
            if start_flag:
                if 'prompt' in convo:
                    prompt = convo['prompt']
                else:
                    prompt = "-"
                if 'start' in convo:
                    start = convo['start']
                else:
                    start = "-"
                if 'ratings' in convo:
                    ratings = convo['ratings']
                else:
                    ratings = "-"
                index = 1
                question_id=0
                for a in convo['messages']:
                    l = list(a)
                    text = ''
                    for m in l:
                        text+= m['text'] +" /"
                        #message_data = dict({'conv_id':convo_id,'prompt':prompt,'start':start,'ratings':ratings,'text': str(text), 'sender': m['sender'], 'timestamp':  m['timestamp']})
                    try:
                        with self._driver.session() as session:
                            session.write_transaction(self._create_and_return_convo,convo_id, prompt,ratings, m['sender'], start, m['timestamp'], text,index,question_id)
                    except:
                        pass
                    question_id = index
                    index +=1
                    

    def read_data_text(self):

        text_data = pd.read_fwf(self.path)
        data_frame = pd.DataFrame(text_data)
        return data_frame  


    @staticmethod
    def _create_and_return_convo(tx, conv_id, prompt, ratings, sender, start, timestamp,text,index,question_id):

        query_new = 'CREATE (n:Message {m_index:"'+str(index)+'", question_id:"'+str(question_id)+'",  conv_id: "'+conv_id+'", start:"'+start+'", sender: "'+sender+ '", original_text:"'+text+'"})'
        #query_conv ='CREATE (n:Conversion { Id: "'+conv_id+'", prompt:"'+prompt+'"})'
        try:
           tx.run(query_new)
           #tx.run(query_conv)
        except:
            pass
    
if __name__ == "__main__":
    graph = GraphDB("bolt://localhost:7687","neo4j","Antalya07-")
    graph.print_convo()
