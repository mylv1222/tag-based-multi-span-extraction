from data_cleaning.cleaning_objective import CleaningObejective
from allennlp.data.dataset_readers.reading_comprehension.drop import DropReader
from allennlp.data.tokenizers import Token
from data_cleaning.remove_spans_base import RemoveSpansBase

class RemoveNonOrgSpans(RemoveSpansBase):
    '''
    Remove spans that are classified as O for multi span questions where we don't expect O
    '''

    name = "RemoveNonOrgSpans"

    question_prefixes = [
        "which team",
    ]
   
    whitelist = [
        # Team is not tagged as ORG or LOC
        "172dfac9-0d27-41ec-968b-1f1c8ca735b9", 
        "141e8f88-698b-423b-9dc4-95cc8dc69644", 
        "84fd0fe5-4b06-439a-b681-2044be991faa", 
        "64a6b892-8ffb-4e73-8738-5161fd1f1b3c",
        "291db275-c598-4192-ab26-c3f450eea4fd",
        "bf9184dc-73e2-4508-bb80-b51b417fccf1",
        "bed1431c-6f4a-41f7-b04d-c053134552f5",
        "1c9ef579-3ffe-4103-84a6-715ccff40ce4",
        "896e98ac-42e1-46cf-9c81-b5d7654297d6",
        "7919a072-29cd-4b00-a75c-2a56b7621ceb",
        "5f625b65-595a-4657-959c-570d435adce8",
        ]

    def should_remove_span(self, span_tags):
        # LOC improves prediction for teams
        return all(not tag.endswith('ORG') and not tag.endswith('LOC') for tag in span_tags)

    def should_remove_answer(self, answer_text):
        return answer_text.isdigit()
