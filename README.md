# Briefd (Brief + Feed)

Briefd delivers personalized, AI-powered news briefings on the topics you care about.

Specify your interests - business, sports, tech, etc. Overnight, Briefd scans thousands of sources and summarizes need-to-know updates into a daily email digest.

Concise, optimized blurbs let you stay informed without wasting time browsing endless news. Briefd learns your preferences and improves briefings over time.

The goal is perfect-length summaries from credible sources - so you start each day informed on what matters most to you.

Briefd saves you time. No more overloaded feeds or searches. Just the essential facts and figures from across the web in one place.

## Features

- Fetches recent news articles from Metaphor based on user-provided categories of interest
- Summarizes each article using GPT-3 from OpenAI  
- Compiles summaries into an HTML email body
- Sends the email briefing to specified recipients

## Usage

1. Clone the repository
2. Set the following environment variables:
    - `OPENAI_API_KEY`: Your OpenAI API key
    - `METAPHOR_API_KEY`: Your Metaphor API key
    - `GMAIL_APP_PASSWORD`: An app password for your Gmail account
3. Update the script with your own sender(`sender_email`)/recipient(`receiver_email`) emails, Gmail email(`gmail_user_name`) and password(`gmail_app_password`) for SMTP server, interests, and date
4. Run `python main.py`

The script will generate summaries for the specified interests, compile them into an HTML email, and send it to the provided recipients.

## Customization

- Update the `user_interests` list to customize categories  
- Adjust `num_results` to increase/decrease articles per topic
- Modify the email subject, headers, etc.
