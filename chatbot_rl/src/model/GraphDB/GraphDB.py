from neo4j import GraphDatabase
import pandas as pd

import json
import os
import numpy
class GraphDB:
    def __init__(self):
        self.path = os.path.join("/home/sefika/ReinforcementLearningForNLP/chatbot_rl/src/model/data/pure/data_train_txt/formated_data_train_dataset.txt")
    def convertDataToGraph(self):

        text_data = pd.read_fwf(self.path)
        data_frame = pd.DataFrame(text_data)
        return data_frame
    
    

if __name__ == "__main__":
    graph  = GraphDB()
    data = graph.convertDataToGraph()
    print(data.shape)
