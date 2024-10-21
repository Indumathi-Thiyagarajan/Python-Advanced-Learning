import pandas as pd

def aws_chat(question):
    # Placeholder function for aws_chat
    # Replace this with your actual implementation
    answer = "sample_answer"
    first_token_latency = 0.1
    invocation_latency = 0.2
    output_tokens = 10
    input_tokens = 5
    tokens_per_second = 50
    return answer, first_token_latency, invocation_latency, output_tokens, input_tokens, tokens_per_second

def process_excel(file_path):
    # Use a context manager to open and close the file
    with pd.ExcelFile(file_path) as xls:
        df = pd.read_excel(xls)

        # Iterate over each question in the 'question' column
        for index, row in df.iterrows():
            question = row['question']
            answer, first_token_latency, invocation_latency, output_tokens, input_tokens, tokens_per_second = aws_chat(question)
           
            # Place the values in the respective columns
            df.at[index, 'answer'] = answer
            df.at[index, 'first_token_latency'] = first_token_latency
            df.at[index, 'invocation_latency'] = invocation_latency
            df.at[index, 'output_tokens'] = output_tokens
            df.at[index, 'input_tokens'] = input_tokens
            df.at[index, 'tokens_per_second'] = tokens_per_second

        # Save the updated DataFrame back to the Excel file
        df.to_excel(file_path, index=False)

if __name__ == "__main__":
    file_path = r"C:\Users\e183066\Downloads\aws_bedrock\aws_bedrock\Vanilla GPT evaluation questions.xlsx"
    process_excel(file_path)
