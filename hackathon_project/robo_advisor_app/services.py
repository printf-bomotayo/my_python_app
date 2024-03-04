import os
import google.generativeai as genai # importing dependencies for the AI service
# using python dotenv library to load environment variable
# from dotenv import load_dotenv
import json

# load_dotenv()  # Load variables from .env file

value = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=value)


class AiService:
    model = genai.GenerativeModel('gemini-pro')

    prompt_template = """
    I am {} years old and I live in {}. I consider myself a {} in terms of investment and I wish to invest 
    for the purpose of {} over a {}-year horizon, and have a {} risk tolerance.
    I have a sum of {} in {} to invest. Which specific financial products ( including ticker and provider 
    would a typical financial advisor recommend for investment given my circumstances? You may limit the number of recommendations to a minimum of five.
    You may also add an estimate of the expected return from each recommendation.
    Environmental factors are not important to me when I am investing. Which composition 
    (as a percentage) would he recommend for each financial product? Each recommendation should sum up to 100%. I will not consider your response personalized advice. 
    You may send the response in json format, let the key to the recommendations be given as recommendations, 
    and each key in the recommendation should be represented as ("financial_product", "ticker", "provider", "brief_description", "expected_return", "composition") and also ensure that the composition comes last in the json. 
    """

    def get_prompt(self, questionnaire):
        prompt = self.prompt_template.format(
            questionnaire.age, 
            questionnaire.location, 
            questionnaire.investment_knowledge, 
            questionnaire.investment_purpose, 
            questionnaire.investment_horizon, 
            questionnaire.risk_tolerance, 
            questionnaire.amount, 
            questionnaire.currency
        )
        return prompt
    


    def format_response(response):
        # Parse the raw JSON response
        raw = json.loads(response.text)

        # Extract the 'recommendations' data
        recommendations = raw.get('recommendations', [])

        # Initialize an empty list to store the formatted recommendations
        formatted_response = []

        # Iterate over each recommendation
        for rec in recommendations:
            # Remove leading/trailing quotes from each field
            formatted_rec = {k: v.strip('"') for k, v in rec.items()}

            # Append the formatted recommendation to the list
            formatted_response.append(formatted_rec)

        return formatted_response


    def get_recommendations(self, questionnaire):
        prompt = self.get_prompt(questionnaire)
        # Replace the following line with the actual AI model or service
        ai_response = self.model.generate(prompt)

        formatted_response = formatted_response(ai_response)
        return formatted_response
