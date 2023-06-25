import json

from haystack.nodes import PromptNode, PromptTemplate
prompt_node = PromptNode("gpt-3.5-turbo", api_key="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",max_length=256,  model_kwargs={"stream":True})


class SalesOrder:
    def __init__(self):
        self.order_type = None
        self.sales_organization = None
        self.distribution_channel = None
        self.sold_to_party = None
        self.ship_to_party = None
        self.po_reference_number = None
        self.order_quantity = None
        self.material = None
        self.plant = None
        self.storage_location = None
        
    def __str__(self):
        return f"Sales Order:\n" \
               f"Order Type: {self.order_type}\n" \
               f"Sales Organization: {self.sales_organization}\n" \
               f"Distribution Channel: {self.distribution_channel}\n" \
               f"Sold-To Party: {self.sold_to_party}\n" \
               f"Ship-To Party: {self.ship_to_party}\n" \
               f"PO Reference Number: {self.po_reference_number}\n" \
               f"Order Quantity: {self.order_quantity}\n" \
               f"Material: {self.material}\n" \
               f"Plant: {self.plant}" \
               f"Storage Location: {self.storage_location}"

        
        

sales_step1_data = PromptTemplate(
    name="step1-salesorder-creation",
    prompt_text="Extract the details of the following variables: Sales organizaiton ( May also be referred to as organization), Distribution Channel , Order Type;\n From the following Input: \n {input}\n\n ; If any of the varaibles are not availabe in the input text,extract it as NULL "
    "The output should be a json file"
)

sales_step2_data = PromptTemplate(
    name="step2-salesorder-creation",
    prompt_text="Extract the details of the following variables: Sold to Party, Ship to Party, PO Reference Number ;\n From the following Input: \n {input}\n\n ; If any of the varaibles are not availabe in the input text,extract it as NULL "
    "The output should be a json file"
)

sales_step3_data = PromptTemplate(
    name="step3-salesorder-creation",
    prompt_text="Extract the details of the following variables: Order quantity, Material, Plant, Storage location ;\n From the following Input: \n {input}\n\n ; If any of the varaibles are not availabe in the input text,extract it as NULL "
    "The output should be a json file"
)


def create_sales_order():
    
    new_order = SalesOrder()
    
    input_1 = input("Sure, Let me help you in creating a sales order; I need some information regarding it, Can you provide me the details of the order type, Sales organizaiton and the Distribution Channel : ")
    output_1 = prompt_node.prompt(prompt_template=sales_step1_data, input = input_1)
    print("\n\n")
    print(output_1)
    
    json_string = output_1[0]
    # Parse the JSON string
    parsed_data = json.loads(json_string)

    # Retrieve the values of sales organization, distribution channel, and order type
    sales_organization = parsed_data.get("Sales Organization")
    distribution_channel = parsed_data.get("Distribution Channel")
    order_type = parsed_data.get("Order Type")
    
    
    # Assign the extracted data to the corresponding attributes
    new_order.order_type = order_type
    new_order.sales_organization = sales_organization
    new_order.distribution_channel = distribution_channel
    
    print(new_order)
    
    input_2 = input("Great, I now need the details of the Sold-to-Party, Ship-to-Party and PO-reference-Number :  ")
    output_2 = prompt_node.prompt(prompt_template=sales_step2_data, input = input_2)
    print("\n\n")
    print(output_2)
    
    json_string = output_2[0]
    # Parse the JSON string
    parsed_data = json.loads(json_string)

    # Retrieve the values
    Sold_to_Party = parsed_data.get("Sold to Party")
    Ship_to_Party = parsed_data.get("Ship to Party")
    PO_Reference_number = parsed_data.get("PO-reference-Number")
    
    
    # Assign the extracted data to the corresponding attributes
    new_order.ship_to_party = Ship_to_Party
    new_order.sold_to_party = Sold_to_Party
    new_order.po_reference_number = PO_Reference_number
    
    input_3 = input("Great, I finally need the order quantity, Material, Plant and Storage location so that I can start creating the order :  ")
    output_3 = prompt_node.prompt(prompt_template=sales_step3_data, input = input_3)
    print("\n\n")
    print(output_3)
    
    json_string = output_3[0]
    # Parse the JSON string
    parsed_data = json.loads(json_string)

    # Retrieve the values 
    Order_quantity = parsed_data.get("order_quantity")    
    Material = parsed_data.get("material")
    plant = parsed_data.get("plant")
    storage_location = parsed_data.get("storage_location")
    
    
    # Assign the extracted data to the corresponding attributes
    new_order.order_quantity = Order_quantity
    new_order.material = Material
    new_order.plant = plant
    new_order.storage_location = storage_location
    
    print(new_order)
    
    
    


# # Call the function to create a sales order
# create_sales_order()
