import os 
from kafka import KafkaConsumer, KafkaProducer

# from enum import Enum

# # class DType(Enum):
# #     STRING = "string"
# #     INT = "integer"
# #     DOUBLE = "double"
    
#     def to_yaml(dumper, data):
#         return dumper.represent_scalar('!DType', data.value)

class EcidaModule:
    def __init__(self, name, version):
        self._name = name
        self._version = version
        self._inputs = {}
        self._outputs = {}
        self._topics_envVars = {}
        self._topics_names = {}
        self._consumers = {}
        self._directories = {}        
        self._producer = None
        self._initialized = False
    
    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version
    
    @property
    def topics_envVars(self):
        return self._topics_envVars

    @property
    def inputs(self):
        return self._inputs
    
    @property
    def outputs(self):
        return self._outputs
    
    @property
    def directories(self):
        return self._directories
    
    @name.setter
    def name(self, value):
        raise AttributeError("Attribute is read-only")

    @version.setter
    def version(self, value):
        raise AttributeError("Attribute is read-only")
    
    def add_input(self, inp: str, type):
        self._inputs[inp] = type
        self._topics_envVars[inp] = "KAFKA_TOPIC_"+ inp.upper()
        
    def add_output(self, out: str, type):
        self._outputs[out] = type
        self._topics_envVars[out] = "KAFKA_TOPIC_"+ out.upper()
        
    def add_input_directory(self, inp: str):
        self._inputs[inp] = "directory"
        self.directories[inp] = {}
        self.directories[inp]["localPath"] = inp
        
    def add_output_directory(self, out: str):
        self._outputs[out] = "directory"
        self.directories[out] = {}
        self.directories[out]["localPath"] = out
        
    def add_input_from_git(self, name: str, git: str, path: str):
        self.add_input_directory(name)
        self.__add_git_to_directory(name, git,path)
    
    def add_output_to_git(self, name: str, git: str, path: str):
        self.add_output_directory(name)
        self.__add_git_to_directory(name, git,path)
    
    def __add_git_to_directory(self, name: str, git: str, path: str):
        self._directories[name]["source"] = git
        self._directories[name]["folder"] = path
    
    def to_yaml(self) -> str:
        return str(self._inputs) + "\n" + str(self._outputs)
    
    def initialize(self):
        self._KAFKA_BOOTSTRAP_SERVER = os.environ['KAFKA_BOOTSTRAP_SERVER']
        self._KAFKA_SASL_MECHANISM = os.environ['KAFKA_SASL_MECHANISM']
        self._KAFKA_SECURITY_PROTOCOL = os.environ['KAFKA_SECURITY_PROTOCOL']
        self._KAFKA_USERNAME = os.environ['KAFKA_USERNAME']
        self._KAFKA_PASSWORD = os.environ['KAFKA_PASSWORD']
        self._KAFKA_GROUP_ID = os.environ['KAFKA_USERNAME']
        
        for key, value in self._inputs.items():
            if value == "directory":
                continue
            topicName = os.environ[self._topics_envVars[key]]
            self._topics_names[key] = topicName
            consumer = KafkaConsumer(topicName, bootstrap_servers = self._KAFKA_BOOTSTRAP_SERVER, 
                            sasl_plain_username= self._KAFKA_USERNAME,
                            sasl_plain_password= self._KAFKA_PASSWORD,
                            sasl_mechanism=self._KAFKA_SASL_MECHANISM,
                            security_protocol=self._KAFKA_SECURITY_PROTOCOL,
                            group_id= self._KAFKA_GROUP_ID)
            self._consumers[key] = consumer
            
        if len(self._outputs) > 0 :
            self._producer = KafkaProducer(bootstrap_servers = self._KAFKA_BOOTSTRAP_SERVER,
                            sasl_plain_username= self._KAFKA_USERNAME,
                            sasl_plain_password= self._KAFKA_PASSWORD,
                            sasl_mechanism=self._KAFKA_SASL_MECHANISM,
                            security_protocol=self._KAFKA_SECURITY_PROTOCOL)
        
        for key, _ in self._outputs.items() :
            topicName = os.environ[self._topics_envVars[key]]
            self._topics_names[key] = topicName
        
        self._initialized = True
            

            
  
    def push(self, output: str, message) -> bool:
        if output in self._outputs:
            self._producer.send(self._topics_names[output], value= str(message).encode("utf-8"))
            return True
        return False
    
    def pull(self, input: str) -> any:
        if input in self._inputs:
            for msg in self._consumers[input]:
                return msg.value.decode("utf-8")
        return None