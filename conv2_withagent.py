from haystack.nodes import PromptNode, PromptTemplate


# google_model = "google/flan-t5-large"
prompt_node = PromptNode("gpt-3.5-turbo", api_key="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",max_length=256,  model_kwargs={"stream":True})


command_classifier = PromptTemplate(
    name="Classify_Initial_question",
    prompt_text="Given the categories: Create sales order, Create purchase order, Question ; Classify the Input: {input}; Ignore indentation and spelling errors while categorizing. Only pick a category from the list, otherwise say: no suitable category",
)

trail_template_1 = PromptTemplate(
    name="trail-1",
    prompt_text="You are a conversational agent with classification capabilities. "
    "You can classify inputs into different categories.\n\n"
    "Whenever the input has a keyword : Help me in creating ; You will classify the input into one of the 3 following categories\n"
    "1. Create sales order\n"
    "2. Create purchase order\n"
    "3. I cannot help you in this regard\n\n"
    "If the input doesnt have the keyword: Help me creating; You will classify it as a question"
    "Input: {input}\n",
)


trail_template_2 = PromptTemplate(
    name="trail-2",
    prompt_text="""
    You are an intelligent AI assistant. Your task is to classify the input into the following categories: Create sales order, Create purchase order, General Q&A, Other Q&A
    You will first anayze the present input :\n
    present_input: {present_input}\n\n
    If the present_input has one of the following keywords it must be classifed as a Question:
    Keywords: "how to", "what is","what", "which", "where"
    otherwise classify it among the three categories : 
    Create sales order, Create purchase order, or Question.
    Whenever you are unable to classify the present_input into any of the categories you  analyze the past input :\n
    past_input = {past_input}\n
    Make your judgement by giving more priority to present_input 
    """
)

trail_template_4= PromptTemplate(
    name="trail-2",
    prompt_text="""
    You are an intelligent AI assistant who looks at both the present and past input but giving more priprity to present_input to make your judgement.\n
    Your task is to classify the input into the following categories: Create sales order, Create purchase order, General Q&A, Other Q&A
    You will first anayze the present input :\n
    present_input: {present_input}\n\n
    If the present_input has one of the following keywords it must be classifed as a Question:
    Keywords: "how to", "what is","what", "which", "where"
    otherwise classify it among the three categories : 
    Create sales order, Create purchase order, or Question.
    Whenever you are unable to classify the present_input into any of the above categories you  analyze the past input but decreasing significance to the later words to decide a cateogory :\n
    past_input = {past_input}\n
    Final Classification:
    """
)

trail_template_4= PromptTemplate(
    name="trail-2",
    prompt_text="""
    You are an intelligent AI assistant who looks at both the present and past input but giving more priprity to present_input to make your judgement.\n
    Your task is to classify the input into the following categories: Create sales order, Create purchase order, General Q&A, Other Q&A
    You will first anayze the present input :\n
    present_input: {present_input}\n\n
    If the present_input has one of the following keywords it must be classifed as a Question:
    Keywords: "how to", "what is","what", "which", "where"
    otherwise classify it among the three categories : 
    Create sales order, Create purchase order, or Question.
    Whenever you are unable to classify the present_input into any of the above categories you  analyze the past input but decreasing significance to the later words to decide a cateogory :\n
    past_input = {past_input}\n
    Final Classification:
    """
)

trail_template_3 = PromptTemplate(
    name="trail-3",
    prompt_text="""
    You are an interactive and knowledgable AI assistant. Your task is to classify the follwing input 
   \n Input:\n {input}\n\n
    If the input has the exact keyword "Help me create" , then classify it into one of "Create sales order", "Create purchase order", "Sorry I currently cannot help you in this command"
    otherwise classify it as Q&A
    """
)

command_step1_data = PromptTemplate(
    name="step1-salesorder-creation",
    prompt_text="Extract the details of the following variables: Sales organizaiton, Distribution Channel, Order Type from {input}; If any of the varaibles are not availabe in the input text,extract it as NULL "
    "The final answer should be a string of extracted data in the order for Sales organization, Distribution Channel, Order Type"
)

past_inputs = []

# while True:
#     user_input = input("Hi how may i help you today: , Press '#' to exit the interface ")
#     if(user_input=="#"):
#         break
#     else: 
#         past_inputs.insert(0, user_input)  # Insert the latest input at the beginning of the list  
#         print(past_inputs)    
#         answer = prompt_node.prompt(prompt_template=trail_template_3,input=" ".join(past_inputs))
#         # if(answer=="Create sales order"):


while True:
    user_input = input("Hi how may i help you today: , Press '#' to exit the interface ")
    if(user_input=="#"):
        break
    else: 
        answer = prompt_node.prompt(prompt_template=trail_template_4,present_input=user_input,past_input= " ".join(past_inputs))
        past_inputs.insert(0, user_input)  # Insert the latest input at the beginning of the list  
        # if(answer=="Create sales order"):
        
        