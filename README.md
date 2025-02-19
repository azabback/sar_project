# Search and Rescue (SAR) First Aid Specialist Agent - CSC 581

## Introduction
This is a cloned version of a repository written by Riley Froomin created to support CSC 581 students in developing
intelligent agents for the AI4S&R project.

Amara Zabback wrote an agent to act as the "first aid specialist" who takes in descriptions by the lost individual or
aid teams of medical complaints and provides two pieces of information:
1. First Aid Instructions on the immediate steps to be taken to help the injured or sick individual, and
2. Best Medical Practices which details the types of tests or care that should be taken after immediate care is finished,
often including delivering the patient to emergency services.

This agent queries Gemini with specific systemic instructions on the circumstances it is being used for and how to respond.
The response is then processed and cleaned, and outputted in the form of a dictionary with four keys:
"Message" - This is the message/query passed to the agent
"First Aid Instructions" - This is the first aid instructions collected by the agent
"Best Medical Practices" - This is the further medical steps suggested by the agent
"Full resposne text" - This is the raw string of text returned by the agent to be used
  in the case where the agent doesn't follow instructions or respond correctly, and therefore the response cannot be cleaned
  and parsed into the key-value pairs of the response dictionary.
