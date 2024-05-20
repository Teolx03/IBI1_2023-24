# DOM APIs 
# import nessaccary tools 
import xml.dom.minidom
from datetime import datetime 

# Start a timer
DOM_APIs_start_time = datetime.now() 

# Parse XML file using DOM APIs 
# Find out all the element from xml and collect element with name <term>
DOMTree = xml.dom.minidom.parse("C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 14\\go_obo.xml") # read the xml file 
collection = DOMTree.documentElement    
element = collection.getElementsByTagName("term") 

# Initialise the counters 
molecular_function_count = 0 
biological_process_count = 0 
cellular_component_count = 0
Total_count = 0

# Loop for the collected element and extract content inside <namespace> element 
for name in element:
  namespace = (name.getElementsByTagName("namespace")[0].firstChild.nodeValue)  # extract the first node inside <namespace>
  all_namespace = namespace.strip() 
  Total_count += 1
# Update the different GO count 
  if all_namespace == "molecular_function":
      molecular_function_count += 1 
  elif all_namespace == "biological_process":
      biological_process_count += 1 
  elif all_namespace == "cellular_component":
      cellular_component_count += 1 

# Display all the counts 
print ("molecular_function_count: " + str(molecular_function_count))
print ("biological_process_count: " + str(biological_process_count))
print ("cellular_component: " + str(cellular_component_count))
print (Total_count)

# End the timer and calculate the time required for DOM APIs 
DOM_APIs_end_time = datetime.now()
DOM_used_time = DOM_APIs_end_time - DOM_APIs_start_time
print ("DOM used time: " + str(DOM_used_time))


# SAX APIs
# import nessaccary tools 
import xml.sax
# start timer for SAX APIs 
SAX_APIs_start_time = datetime.now()

# create class for SAX handler 
class NamespaceHandler (xml.sax.ContentHandler):    
 # Initialize the list, variable and boolean   
    def __init__(self):  
        self.namespace = ""
        self.in_term = False    # Track if enter <term> element 
        self.in_namespace = False   # Track if enter <namespace> element 
        self.molecular_fucntion_count = 0
        self.biological_process_count = 0 
        self.cellular_component_count = 0 

 # Find the specific start element 
    def startElement(self, name, attrs): 
        if name == "term":  
           self.in_term = True   # when starting tag name is <term> = True, parser inside the <term> element 
        if self.in_term and name == "namespace":
            self.in_namespace = True  # when inside the <term> element, and the starting tag name is <namespace>(inside <namespace> element)= True 
 # Find specific end element 
    def endElement (self, name):  
        if self.in_namespace:  # if inside <term> and <namespace> element 
            if self.namespace == "molecular_function":
                self.molecular_fucntion_count += 1 
            elif self.namespace == "biological_process":
                self.biological_process_count += 1 
            elif self.namespace == "cellular_component":
              self.cellular_component_count += 1
            self.namespace = ""  # empty for next element enter 
            self.in_namespace = False # when exit <namespace>
            self.in_term = False  # when exit <term> 
 # Extract the value in the specific element 
    def characters(self, content):
        if self.in_namespace :   # if inside <term> and <namespace> element 
           self.namespace += content.strip()    
        
# Parse the xml file using SAX APIs 
parser = xml.sax.make_parser ()
Handler = NamespaceHandler()
parser.setContentHandler(Handler)
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
parser.parse ("C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 14\\go_obo.xml")

# Display all the counter 
print ("Molecular fucntion count: " + str(Handler.molecular_fucntion_count))
print ("Biological process count: " + str(Handler.biological_process_count))
print ("Cellular component count: " + str(Handler.cellular_component_count))

# End the timer and calculate the time take for SAX APIs 
SAX_APIs_end_time = datetime.now()
SAX_APIs_used_time = SAX_APIs_end_time - SAX_APIs_start_time
print ("SAX APIs used time: " + str(SAX_APIs_used_time))

# Plot a graph for the data 
# Import nessaccary tools 
import numpy as np 
import matplotlib.pyplot as plt 

# plot graph for DOM APIs
GO_terms = ["Molecular Function", "Biological Process", "Cellular Component"]
Go_terms_score = [molecular_function_count, biological_process_count, cellular_component_count]
width = 0.5
plt.subplot(2,1,1)
plt.bar (GO_terms, Go_terms_score, width)
plt.ylabel ("Number of GO terms")
plt.title ("Frequency of GO terms in three ontologies(DOM)")


# plot graph for SAX APIs 

GO_terms = ["Molecular Function", "Biological Process", "Cellular Component"]
Go_terms_score = [Handler.molecular_fucntion_count, Handler.biological_process_count, Handler.cellular_component_count]
width = 0.5
plt.subplot(2,1,2)
plt.bar (GO_terms, Go_terms_score, width)
plt.ylabel ("Number of GO terms")
plt.title ("Frequency of GO terms in three ontologies(SAX)")


# let 2 different graph locate in one figure 
plt.tight_layout()
plt.show()
plt.clf()