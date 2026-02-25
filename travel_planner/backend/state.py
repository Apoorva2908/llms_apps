'''
This file contains the code to maintain memory for each session using sessions id.
'''

##saves history
sessions = {}

def get_messages(session_id, system_prompt):
    '''
    This function contains unique conversation and
    allows the backend to fetch the chat history 
    '''
    if session_id not in sessions:
        sessions[session_id] = [{"role":"system", "content":system_prompt}]
    return sessions[session_id]

def update_messages(session_id, role, content):
    '''
    Function to add messages to session id,
    adds users message and systems reply under 'assistant' role
    '''
    sessions[session_id].append({"role":role, "content":content})