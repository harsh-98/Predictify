import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username='6265b5f4-5fe7-4e53-821e-62dd36aea296',
  password='iXv7R0Np8JRR',
  version='2017-05-26'
)

# Replace with the context obtained from the initial request
context = {}

workspace_id = 'cb56274d-93af-4acd-84d2-f5bfcdab5bac'

response = conversation.message(
  workspace_id=workspace_id,
  message_input={'text': 'I scored 80%'},
  context=context
)

print(json.dumps(response, indent=2)[1])
print response["output"]["text"][0]
