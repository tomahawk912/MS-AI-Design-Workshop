from promptflow import tool
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult, AnalyzeDocumentRequest

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:

    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = '<endpoint-url>'
    key = '<api-key>'

    document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    # Analyze a document at a URL:
    # receiptUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/receipt.png"
    # Replace with your actual receiptUrl:
    # If you use the URL of a public website, to find more URLs, please visit: https://aka.ms/more-URLs 
    # If you analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-receipt",
        analyze_request=input1,
        content_type="application/octet-stream"
    )       

    # # If analyzing a local document, remove the comment markers (#) at the beginning of these 8 lines.
    # # Delete or comment out the part of "Analyze a document at a URL" above.
    # # Replace <path to your sample file>  with your actual file path.
    # path_to_sample_document = "<path to your sample file>"
    # with open(path_to_sample_document, "rb") as f:
    #     poller = document_intelligence_client.begin_analyze_document(
    #         "prebuilt-receipt", analyze_request=f, locale="en-US", content_type="application/octet-stream"
    #     )
    receipts: AnalyzeResult = poller.result()

    date = receipts['documents'][0]['fields']['TransactionDate']['valueDate']
    merchant_name = receipts['documents'][0]['fields']['MerchantName']['valueString']
    total = receipts['documents'][0]['fields']['Total']['valueCurrency']['amount']

    return date, merchant_name, total