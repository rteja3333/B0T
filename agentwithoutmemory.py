from haystack.nodes import PromptNode, PromptTemplate


# google_model = "google/flan-t5-large"
prompt_node = PromptNode("gpt-3.5-turbo", api_key="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",max_length=256,  model_kwargs={"stream":True})

trail_template_1 = PromptTemplate(
    name="trail-1",
    prompt_text="You are a intelligent agent whose goal is to classify the input. "
    "Input: \n{present_input}\n\n"
    "Whenever the input has one of the following keywords, You classify it as a question: What is? , What are, Where is, How to "
    "Else You can classify input into three categories: Q&A, Create Sales Order, Create Purchase Order.\n\n"
    "Only answer with the Final Classification: "   
)

trail_template_working_unintelligent = PromptTemplate(
    name="trail-1",
    prompt_text="You are a intelligent agent whose goal is to classify the input. \n\n"
    "Input: \n{present_input}\n\n"
    "You can classify input into three categories: Create Sales Order, Create Purchase Order, Q&A.\n\n"
    "Only respond with the Final Classification you decided on: "
)
      
        
        
def classify_input(input_text):
   
    answer = prompt_node.prompt(prompt_template=trail_template_1, present_input=input_text)

    return answer

# Test the function
# while(True):
#     test_input = input("Test Question : ")
#     if(test_input=="#"):
#         break
#     else:
#         answer = classify_input(test_input)
#         print(answer)

