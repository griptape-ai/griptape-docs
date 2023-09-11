# FileManager

This tool enables LLMs to save and load files.

```python
from griptape.structures import Agent
from griptape.tools import FileManager

# Set up an agent using the FileManager tool
file_manager_tool = FileManager(dir='/path/to/files')
agent = Agent(
    tools=[file_manager_tool]
)

# Load files from disk
agent.run("Can you get me the sample1.txt file?")
```
```
[09/08/23 15:43:19] INFO     Task e93f7ba59d15491f814280324d46eaa3              
                             Input: Can you get me the sample1.txt file?        
[09/08/23 15:43:26] INFO     Subtask 8779d4c533eb4ea99cd0415aebaf6ab6           
                             Thought: The user wants the content of the file    
                             named "sample1.txt". I can use the FileManager tool
                             with the "load_files_from_disk" activity to load   
                             the file from the disk.                            
                                                                                
                             Action: {"type": "tool", "name": "FileManager",    
                             "activity": "load_files_from_disk", "input":       
                             {"values": {"paths": ["sample1.txt"]}}}            
                    INFO     Subtask 8779d4c533eb4ea99cd0415aebaf6ab6           
                             Observation:                                       
                             [BlobArtifact(id='0ebc80c707634a51af04cb9535f22aac'
                             , name='sample1.txt', type='BlobArtifact',         
                             value=b'Utilitatis causa amicitia est              
                             quaesita.\nLorem ipsum dolor sit amet, consectetur 
                             adipiscing elit. Collatio igitur ista te nihil     
                             iuvat. Honesta oratio, Socratica, Platonis etiam.  
                             Primum in nostrane potestate est, quid meminerimus?
                             Duo Reges: constructio interrete. Quid, si etiam   
                             iucunda memoria est praeteritorum malorum? Si      
                             quidem, inquit, tollerem, sed relinquo. An nisi    
                             populari fama?\n\nQuamquam id quidem licebit iis   
                             existimare, qui legerint. Summum a vobis bonum     
                             voluptas dicitur. At hoc in eo M. Refert tamen, quo
                             modo. Quid sequatur, quid repugnet, vident. Iam id 
                             ipsum absurdum, maximum malum neglegi.', dir='')]  
[09/08/23 15:43:45] INFO     Task e93f7ba59d15491f814280324d46eaa3              
                             Output: The content of the file "sample1.txt" is:  
                                                                                
                             "Utilitatis causa amicitia est quaesita.           
                             Lorem ipsum dolor sit amet, consectetur adipiscing 
                             elit. Collatio igitur ista te nihil iuvat. Honesta 
                             oratio, Socratica, Platonis etiam. Primum in       
                             nostrane potestate est, quid meminerimus? Duo      
                             Reges: constructio interrete. Quid, si etiam       
                             iucunda memoria est praeteritorum malorum? Si      
                             quidem, inquit, tollerem, sed relinquo. An nisi    
                             populari fama?                                     
                                                                                
                             Quamquam id quidem licebit iis existimare, qui     
                             legerint. Summum a vobis bonum voluptas dicitur. At
                             hoc in eo M. Refert tamen, quo modo. Quid sequatur,
                             quid repugnet, vident. Iam id ipsum absurdum,      
                             maximum malum neglegi."  
```