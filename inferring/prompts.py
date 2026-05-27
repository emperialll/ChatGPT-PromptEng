# Version 1 - Sentiment (positive/negative)
def prompt_v1(lamp_review: str) -> str:
    return f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Give your answer as a single word, either "positive"
or "negative".

Review text: '''{lamp_review}'''
"""

# Version 2 - Identify types of emotions
def prompt_v2(lamp_review: str) -> str:
    return f"""
Identify a list of emotions that the writer of the
following review is expressing. Include no more than
five items in the list. Format your answer as a list of
lower-case words separated by commas.

Review text: '''{lamp_review}'''
"""

# Version 3 - Identify anger
def prompt_v3(lamp_review: str) -> str:
    return f"""
Is the writer of the following review expressing anger?
The review is delimited with triple backticks. 
Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""

# Version 4 - Extract product and company name from customer reviews
def prompt_v4(lamp_review: str) -> str:
    return f"""
Identify the following items from the review text: 
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks.
Format your response as a JSON object with
"Item" and "Brand" as the keys. 
If the information isn't present, use "unknown"
as the value.
Make your response as short as possible.
  
Review text: '''{lamp_review}'''
"""

# Version 5 - Doing multiple tasks at once
def prompt_v5(lamp_review: str) -> str:
    return f"""
Identify the following items from the review text: 
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks.
Format your response as a JSON object with
"Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information isn't present, use "unknown"
as the value.
Make your response as short as possible.
Format the Anger value as a boolean.

Review text: '''{lamp_review}'''
"""

# Version 6 - Infer 5 topics
def prompt_v6(story: str) -> str:
    return f"""
Determine five topics that are being discussed in the
following text, which is delimited by triple backticks.

Make each item one or two words long. 

Format your response as a list of items separated by commas.

Text sample: '''{story}'''
"""

# Version 7 - Infer 5 topics
def prompt_v7(story: str, topic_list: list) -> str:
    return f"""
Determine whether each item in the following list of
topics is a topic in the text below, which
is delimited with triple backticks.

Give your answer as follows:
item from the list: 0 or 1

List of topics: {", ".join(topic_list)}

Text sample: '''{story}'''
"""