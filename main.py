import os
import openai
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from metaphor_python import Metaphor

def get_summaries(user_interests, date) -> []:
    SYSTEM_MESSAGE_SUMMARIZER = "You are a helpful assistant that summarizes the content of a webpage. Summarize the users input."

    # Fetch latest links for each category
    summaries = []
    for interest in user_interests:
        query = f"Recent developments in {interest} news?"
        search_response = metaphor.search(
            query, use_autoprompt=True, start_published_date=date, num_results=2
        )
        print(f"Titles: {[result.title for result in search_response.results]}\n")

        # Summarize the contents
        for content in search_response.get_contents().contents:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SYSTEM_MESSAGE_SUMMARIZER},
                    {"role": "user", "content": content.extract},
                ],
            )

            summary = completion.choices[0].message.content

            summaries.append({
                "title": content.title,
                "url": content.url,
                "summary": summary
            })
    
    print("Summaries Generated")
    return summaries

def generate_email_body(summaries) -> str:
    # Create MIMEMultipart object  
    msg = MIMEMultipart()

    msg['Subject'] = 'Today\'s Brief'
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_email)


    # Create HTML string
    html = '<html><body>'
    for summary in summaries:
        html += '<h2><a href="' + summary['url'] + '">' + summary['title'] + '</a></h2>'
        html += '<p>' + summary['summary'] + '</p>'
    html += '</body></html>'

    # Attach HTML string as MIMEText object
    msg.attach(MIMEText(html, 'html'))

    print("Email body created")
    return msg.as_string()

def send_email(sender_email, receiver_email, email_body):
    # Create a secure SSL context
    context = ssl._create_unverified_context()
    
    port = 465  # For SSL
    gmail_user_name = <ADD GMAIL USER NAME>
    gmail_app_password = os.getenv("GMAIL_APP_PASSWORD") 

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        reply = server.login(gmail_user_name, gmail_app_password)
        print("Logged in!")
        resp = server.sendmail(sender_email, receiver_email, email_body)
        print('Email sent!, Resp:', resp)


openai.api_key = os.getenv("OPENAI_API_KEY")
metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

# Sample user interest categories
user_interests = ["Search engine", "LLM"] 
date = "2023-09-30"

sender_email = <ADD SENDER EMAIL>
receiver_email = <ADD RECEIVER EMAIL>

summaries = get_summaries(user_interests, date)
email_body = generate_email_body(summaries)

send_email(sender_email, receiver_email, email_body)

