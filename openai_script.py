import openai
import os


def extract_and_find_address(address_to_find):
    __EXTRACTION_PROMPT__ = "Extract the Address for Google Maps API using this" \
                            " tweet, the address will be from Turkey:\nTweet: "

    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = __EXTRACTION_PROMPT__ + address_to_find + "\nAddress: "
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.4,
        presence_penalty=0,
    )
    extracted_address = response["choices"][0]["text"]
    return extracted_address
