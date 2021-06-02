from jina import Document, DocumentArray, Flow, Executor, requests

doc1 = Document(
        text = "Just random stuff",
        tags = {
                "reactions": ["laugh", "bowtie"],
                "user": "pradeep"
                }
        )

doc2 = Document(
        text = "Just special andom stuff",
        tags = {
                "reactions": ["laugh", "bowtie"],
                "user": "pradeep"
                }
        )

docs = DocumentArray([doc1, doc2])

print(docs)

#flow = Flow().add(uses=SlackChatProcessor)


class SlackChatProcessor(Executor):
    @requests(on='/trim')
    def trim(self, **kwargs):
        print('Processing chat: trim')

    @requests(on='/index')
    def index(sefl, **kwargs):
        print('Processing chat: index')

f = Flow().add(uses=SlackChatProcessor).plot('flow.svg')

with f:
    f.post(on='/trim', inputs=docs)
    f.post(on='/index', inputs=docs)
